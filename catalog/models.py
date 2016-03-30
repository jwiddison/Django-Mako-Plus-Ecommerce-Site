from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel


## Sprint 5 Stuff:

#########################################################################################################
#######   Sale             ##############################################################################
#########################################################################################################
class Sale(models.Model):
    name = models.TextField(null=True, blank=True)

#########################################################################################################
#######   SaleItem         ##############################################################################
#########################################################################################################
class SaleItem(PolymorphicModel):
    name = models.TextField(null=True, blank=True)
    sale = models.ForeignKey('catalog.Sale', related_name='images')


#########################################################################################################
#######   Payment          ##############################################################################
#########################################################################################################
class Payment(models.Model):
    name = models.TextField(null=True, blank=True)

## Record Sale method
def record_sale():
    pass

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
