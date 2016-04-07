from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel
import datetime, random, string


## Sprint 5 Stuff:

#########################################################################################################
#######   Sale             ##############################################################################
#########################################################################################################
class Sale(models.Model):
    OrderDate = models.DateField(null=True, blank=True, auto_now_add=True)
    ShipDate = models.DateField(null=True, blank=True, auto_now_add=True)
    TrackingNumber = models.TextField(null=True, blank=True)
    TotalPrice = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    ShipName = models.TextField(null=True, blank=True)
    ShipAddress = models.TextField(null=True, blank=True)
    ShipCity = models.TextField(null=True, blank=True)
    ShipState = models.TextField(null=True, blank=True)
    ShipZipCode = models.TextField(null=True, blank=True)
    Buyer = models.ForeignKey('account.User')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Sale -> Price: %s, Buyer: %s' % (self.TotalPrice, self.Buyer)

    def get_saleitems(self):
        return SaleItem.objects.all().filter(sale=self.id)


admin.site.register(Sale)


#########################################################################################################
#######   SaleItem         ##############################################################################
#########################################################################################################
class SaleItem(PolymorphicModel):
    Description = models.TextField(null=True, blank=True)
    Price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    Quantity = models.TextField(null=True, blank=True)
    Extended = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    sale = models.ForeignKey('catalog.Sale', related_name='saleitems')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'SaleItem -> Description: %s' % (self.Description)

admin.site.register(SaleItem)

#########################################################################################################
#######   Payment          ##############################################################################
#########################################################################################################
class Payment(models.Model):
    PaymentDate = models.DateField(null=True, blank=True, auto_now_add=True)
    Amount = models.TextField(null=True, blank=True)
    ValidationCode = models.TextField(null=True, blank=True)
    Payer = models.ForeignKey('account.User')
    sale = models.ForeignKey('catalog.Sale', related_name='payments')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Payment -> Amount: %s, Payer: %s' % (self.Amount, self.Payer)

admin.site.register(Payment)


## Record Sale method
def record_sale(user, address_list, cart, stripe_id):
    # Create a sale object

    print(address_list)

    s = Sale(
        OrderDate = datetime.datetime.now(),
        ShipDate = datetime.datetime.now(),
        TrackingNumber = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(0,9)),
        TotalPrice = cart.calc_total(),
        ShipName = address_list[0],
        ShipAddress = address_list[1],
        ShipCity = address_list[2],
        ShipState = address_list[3],
        ShipZipCode = address_list[4],
        Buyer = user,
    )
    s.save()
    print(s)

    # Create saleitem objects for each item in the cart
    for item in cart.get_items():
        si = SaleItem(
            Description = item.name,
            Price = item.price,
            Quantity = item.quantity,
            Extended = item.calc_extended(),
            sale = s,
        )
        si.save()

        print(si)

        p = Product.objects.get(id = item.product_id)
        if isinstance(p, BulkProduct):
            p.quantity -= item.quantity
            p.save()
        elif isinstance(p, IndividualProduct):
            p.status = 'sold'
            p.save()

    # create saleitem objects for the tax and for the shipping amounts
    tax_si = SaleItem(
        Description = 'Tax',
        Price = cart.calc_tax(),
        Quantity = '1',
        Extended = cart.calc_tax(),
        sale = s,
    )
    tax_si.save()

    shipping_si = SaleItem(
        Description = 'Shipping',
        Price = cart.calc_shipping(),
        Quantity = '1',
        Extended = cart.calc_shipping(),
        sale = s,
    )
    shipping_si.save()

    # Create a payment object
    payment = Payment(
        PaymentDate = datetime.datetime.now(),
        Amount = cart.calc_total(),
        ValidationCode = stripe_id,
        Payer = user,
        sale = s,
    )
    payment.save()

    return s


## Sprint 4 Stuff:
#########################################################################################################
#######    Category        ##############################################################################
#########################################################################################################
class Category(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Category: %s' % (self.name)

admin.site.register(Category)


#########################################################################################################
#######    Product Image        #########################################################################
#########################################################################################################
class ProductImage(models.Model):
    filename = models.TextField(null=True, blank=True)
    product = models.ForeignKey('catalog.Product', related_name='images')

    def __str__(self):
        '''Prints for debugging purposes'''
        return self.filename

admin.site.register(ProductImage)

## Sprint 3 Stuff:

#########################################################################################################
####### Base Product Class ##############################################################################
#########################################################################################################
class Product(PolymorphicModel):
    '''Superclass for all other product types '''
    name = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    add_date = models.DateField(null=True, blank=True, auto_now_add=True)
    # Removed for Sprint 4
    # image = models.TextField(null=True, blank=True)
    category = models.ForeignKey('catalog.Category')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Product (abstract): %s (%s)' % (self.name(), self.add_date)

    def get_image_filename(self):
        '''Returns the filename of the first image, or the unavailable image if no images have been added.'''
        first_image = self.images.first()
        return first_image.filename if first_image != None else 'image_unavailable.gif'

admin.site.register(Product)

RENTAL_STATUS_CHOICES = (
    ('current', 'Rentable'),
    ('damaged', 'Damaged'),
    ('retired', 'No Longer Rentable'),
)
RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)

#########################################################################################################
#######   Rental Product   ##############################################################################
#########################################################################################################
class RentalProduct(Product):
    className = "Rental Product"
    status = models.TextField(null=True, blank=True, choices=RENTAL_STATUS_CHOICES)
    purchase_date = models.DateField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Rental Product: %s (%s): %s' % (self.name, self.add_date, self.status)

admin.site.register(RentalProduct)


#########################################################################################################
####### Individual Product ##############################################################################
#########################################################################################################
INDIVIDUAL_STATUS_CHOICES = (
  ( 'current', 'For Sale'),
  ( 'sold', 'Sold'),
  ( 'retired', 'No Long For Sale'),
)
INDIVIDUAL_STATUS_CHOICES_MAP = dict(INDIVIDUAL_STATUS_CHOICES)

class IndividualProduct(Product):
    className = "Individual Product"
    creator = models.ForeignKey('account.User')
    create_date = models.DateField(null=True, blank=True, auto_now_add=True)
    status = models.TextField(null=True, blank=True, choices=INDIVIDUAL_STATUS_CHOICES)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Individual Product: %s (%s): %s' % (self.name, self.add_date, self.creator.get_full_name())

admin.site.register(IndividualProduct)



#########################################################################################################
#######    Bulk Product    ##############################################################################
#########################################################################################################
class BulkProduct(Product):
    className = "Bulk Product"
    quantity = models.IntegerField(default=0)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Bulk Product: %s (%s): %s' % (self.name, self.add_date, self.quantity)

admin.site.register(BulkProduct)


#########################################################################################################
#######    Venue           ##############################################################################
#########################################################################################################
class Venue(models.Model):
    name = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zip_code = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Venue: %s (%s)' % (self.name, self.address)

admin.site.register(Venue)

#########################################################################################################
#######    Event           ##############################################################################
#########################################################################################################
class Event(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date =  models.DateField(null=True, blank=True)
    end_date =  models.DateField(null=True, blank=True)
    venue = models.ForeignKey('catalog.Venue')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Event: %s (%s)' % (self.name, self.description)

admin.site.register(Event)


#########################################################################################################
#######    Area            ##############################################################################
#########################################################################################################
class Area(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    place_number = models.TextField(null=True, blank=True)
    event = models.ForeignKey('catalog.Event')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Area: %s (%s)' % (self.name, self.description)

admin.site.register(Area)
