from catalog import models as cmod
import datetime, decimal, operator

#################################################################################
###   Shopping Cart middleware that adds a shopping cart to the current request.
#################################################################################

# the key we use for the shopping cart list
SHOPPING_CART_KEY = 'shopping_cart'

### STUDENTS ###
# the key we use for the last viewed items
# LAST_VIEWED_PROD_KEY = 'last_viewed_products'
LAST_VIEWED_ID_KEY = 'last_viewed_ids'
LAST_VIEWED_COUNT = 5  # keep only the last 5

TAX_RATE = decimal.Decimal(0.0725)  # just using a default rate
SHIPPING_AMOUNT = decimal.Decimal(10.00)


class ShoppingCartMiddleware:
    '''Adds shopping cart methods to the request.'''

    def process_request(self, request):
        '''Called when the request starts in Django'''
        # attach a ShoppingCart instance to the request object
        request.shopping_cart = ShoppingCart(request.session)

    def process_response(self, request, response):
        '''Called when the response goes back to the browser.'''
        # save the shopping cart
        request.shopping_cart.save(request.session)

        # return the response per Django docs
        return response



class ShoppingCart(object):
    '''The user's shopping cart.  One of these is created for each request.
       Note that I haven't added any efficiency code yet, such as lazy loading/saving
       the shopping cart object (only when/if it gets accessed) or using a
       set for faster item lookup.  I'm keeping it simple for class purposes.
    '''

    def __init__(self, session):
        '''Constructor.  This is called from process_request() above.'''
        self.session = session

        # load the cart from the session, and check and make sure its a list.
        self.cart = self.session.get(SHOPPING_CART_KEY, [])
        if not isinstance(self.cart, list):
            self.cart = []

        # load the last 5 ids list from the session, into a list attribute of the shopping cart.
        self.last_5_ids = self.session.get(LAST_VIEWED_ID_KEY, [])
        if not isinstance(self.last_5_ids, list):
            self.last_5_ids = []


    def save(self, session):
        '''Saves the current shopping cart to the session.
           This is called from the middleware above.'''
        # sort the cart by name
        self.cart.sort(key=operator.attrgetter('name'))

        # set the cart, and list of IDs into session
        self.session[SHOPPING_CART_KEY] = self.cart
        self.session[LAST_VIEWED_ID_KEY] = self.last_5_ids

    ###  SHOPPING CART

    def get_items(self):
        '''Returns the items in the shopping cart'''
        return self.cart

    def get_full_cart(self):
        '''Returns full-on product objects for all items in cart'''
        cart_items = self.cart
        cart_products = [cmod.Product.objects.get(id=pid) for pid in cart_items]
        return cart_products


    def check_availability(self, product, desired_quantity=1):
        '''Checks that the product is available at the given quantity.  Raises a ValueError if we don't have enough.'''
        # Get quantity from Database
        if isinstance(product, cmod.BulkProduct):
            quantity_available = product.quantity
        else:
            desired_quantity = 1
            quantity_available = 1

        # decrease the available amount by any in our cart
        for cart_item in self.cart:
            if cart_item.product_id == product.id:
                if isinstance(product, cmod.IndividualProduct):
                    raise ValueError('This product is already in your cart!')
                else:
                    quantity_available -= cart_item.quantity
                    break

        # Just in case, make sure it didn't go negative
        quantity_available = max(quantity_available, 0)

        # check the available amount and raise ValueError if not enough
        if quantity_available < desired_quantity:
            raise ValueError("Not enough available.  Please select %s or less" % quantity_available)



    def add_item(self, product, quantity=1):
        '''Adds the product to the current cart.  If the item already exists in the cart, it adds to the quantity of the item.'''
        # check the availability
        self.check_availability(product, quantity)

        # see if it is in our cart
        for p in self.cart:
            if product.id == p.product_id:
                p.quantity += quantity
                break
        else:
            newItem = ShoppingItem(product)
            if isinstance(product, cmod.IndividualProduct):
                quantity = 1
            newItem.quantity = quantity
            self.cart.append(newItem)


    def remove_item(self, product):
        '''Removes the given item id from the cart
           The product can be a real product instance or a product id.
        '''
        for item in self.cart:
            if item.product_id == product.id:
                self.cart.remove(item)

    def clear_items(self):
        '''Clears all items from the shopping cart'''
        self.cart = []

    def get_item_count(self):
        '''Returns the item count'''
        # return len(self.cart)
        count = decimal.Decimal(0)
        for p in self.cart:
            count += p.quantity
        return count

    ###   FINANCIAL METHODS

    def calc_subtotal(self):
        '''Returns the subtotal (sum of product) cost'''
        subtotal = decimal.Decimal(0)
        for p in self.cart:
        	subtotal += p.calc_extended()
        return subtotal.quantize(decimal.Decimal('.01'), rounding = decimal.ROUND_UP)

    def calc_tax(self):
        '''Returns the tax on the current cart'''
        return (self.calc_subtotal() * TAX_RATE).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_UP)

    def calc_shipping(self):
        '''Returns the shipping cost on the current cart'''
        return SHIPPING_AMOUNT.quantize(decimal.Decimal('.01'), rounding = decimal.ROUND_UP)

    def calc_total(self):
        '''Returns the total cost on the current cart'''
        return self.calc_subtotal() + self.calc_tax() + self.calc_shipping()

    def calc_stripe_total(self):
        '''Returns the total in a format that stripe is going to know how to use'''
        return (self.calc_total() * 100).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_UP)


    ###   LAST VIEWED PRODUCT METHODS

    # Called by detail.py
    def item_viewed(self, product):
        '''Adds an item to the last-viewed items'''
        # Create local list from list of IDs in shopping cart
        local_last5 = self.last_5_ids
        # delete from the list if currently there (so it isn't listed twice)
        try:
            local_last5.remove(product.id)
        except ValueError:
            pass
        # add the id to the last viewed list
        local_last5.insert(0, product.id)
        # Prune the list to length
        local_last5 = local_last5[:LAST_VIEWED_COUNT]
        # Save list back into shopping cart's last_viewed_ids list.
        self.last_5_ids = local_last5

    def get_viewed_items(self):
        '''Returns a Django query object of the last items viewed'''
        # Store list of IDs in a local list
        last5 = self.last_5_ids

        # Create a new local list of products by iterating through list of ids
        last5products = [cmod.Product.objects.get(id=pid) for pid in last5]

        # This is how Dr. Albrecht did it.  I don't like it as much.
        # last5products = list(cmod.Product.objects.filter(id__in=self.last_5_ids))
        # last5products.sort(key=lambda p: self.last_5_ids.index(p.id))

        return last5products

    def get_last5_ids(self):
        '''Just returns a list of the id numbers of items in the cart'''
        return self.last_5_ids


class ShoppingItem(object):
    '''A shopping cart item. Each of these objects represents a product in the shopping cart.  In
       other words, the shopping cart is a list of these objects (ShoppingItem objects).

       This class cannot contain any pointers because it is serialized to the user's session object.
       That's why it references product.id instead of product directly.
    '''
    def __init__(self, product):
        '''Constructor.  Starts the quantity at 0, so be sure to set it.'''
        self.product_id = product.id
        self.filename = product.get_image_filename()
        self.name = product.name
        self.price = product.price
        self.quantity = decimal.Decimal(0)

    def calc_extended(self):
        return self.price * self.quantity

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'ShoppingItem: %s Quantity: %s ' % (self.name, self.quantity)
