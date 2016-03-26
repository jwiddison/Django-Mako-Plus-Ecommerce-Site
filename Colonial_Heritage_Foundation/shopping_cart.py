from catalog import models as cmod
import datetime, decimal

########################################################################
###   Shopping Cart middleware that adds a shopping cart to the
###   current request.
###
###   Installation:
###      1. Since this code uses decimal.Decimal() objects, it cannot use the regular JSON serializer
###         that sessions default to.  Switch to pickle-based sessions by adding this to settings.py:
###
###         SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
###
###      2. Enable this middleware by adding the following to settings.py:
###         (assuming you have this file in the /CHF/ directory, of course)
###
###         MIDDLEWARE_CLASSES = [
###             ...
###             'CHF.shopping_cart.ShoppingCartMiddleware',
###             ...
###         ]
###
###         The above line must come after SessionAuthenticationMiddleware in the list because it uses sessions.
###

# the key we use for the shopping cart list
SHOPPING_CART_KEY = 'shopping_cart'

### STUDENTS ###
# the key we use for the last viewed items
LAST_VIEWED_KEY = 'shopping_cart_last_viewed'
LAST_VIEWED_COUNT = 5  # keep only the last 5

TAX_RATE = decimal.Decimal(0.0725)  # just using a default rate
SHIPPING_AMOUNT = decimal.Decimal(10)


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
        # load the cart from the session
        # self.last5ids = session.get...
        # load the last 5 items
        # self.cart = session.get...

    def save(self, session):
        '''Saves the current shopping cart to the session.
           This is called from the middleware above.
        '''
        # sort the cart by name

        # set the cart in the session (this saves it to disk so we can access it again next request)

        # set the shopping_last_viewed in the session


    ###  SHOPPING CART  (self in this context = shopping_cart)

    def get_items(self):
        '''Returns the items in the shopping cart'''


    def check_availability(self, product, desired_quantity=1):
        '''Checks that the product is available at the given quantity.  Raises a ValueError if we don't have enough.'''
        # get the available per the database for Individual or Bulk
        quantity = product.quantity
        # decrease the available amount by any in our cart

        # check the available amount and raise ValueError if not enough



    def add_item(self, product, quantity=1):
        '''Adds the product to the current cart.  If the item already exists in the
           cart, it adds to the quantity of the item.
        '''
        # check the availability

        # ensure it is in our cart

        # update the quantity


    def remove_item(self, product):
        '''Removes the given item id from the cart
           The product can be a real product instance or a product id.
        '''


    def clear_items(self):
        '''Clears all items from the shopping cart'''


    def get_item_count(self):
        '''Returns the item count'''


    ###   FINANCIAL METHODS

    def calc_subtotal(self):
        '''Returns the subtotal (sum of product) cost'''


    def calc_tax(self):
        '''Returns the tax on the current cart'''


    def calc_shipping(self):
        '''Returns the shipping cost on the current cart'''


    def calc_total(self):
        '''Returns the total cost on the current cart'''
        return self.calc_subtotal() + self.calc_tax() + self.calc_shipping()


    ###   LAST VIEWED PRODUCT METHODS

    def item_viewed(self, product):
        '''Adds an item to the last-viewed items'''
        # delete from the list if currently there (so it isn't listed twice)

        # add the id to the last viewed list

        # ensure the list isn't too long - right now we do 5 items max


    def get_viewed_items(self):
        '''Returns a Django query object of the last items viewed'''
        # create the list of products from the ids in our last 5 viewed




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
