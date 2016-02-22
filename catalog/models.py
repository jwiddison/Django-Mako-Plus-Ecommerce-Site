from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel

# Includes classes for all the types of products in the system

#########################################################################################################
####### Base Product Class ##############################################################################
#########################################################################################################
class Product(PolymorphicModel):
    '''Superclass for all other product types '''
    name = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    add_date = models.DateField(null=True, blank=True, auto_now_add=True)
    image = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Product (abstract): %s (%s)' % (self.name(), self.add_date)

admin.site.register(Product)

RENTAL_STATUS_CHOICES = (
    ('current', 'Rentable'),
    ('damaged', 'Damaged'),
    ('retired', 'No Long Rentable'),
)
RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)

#########################################################################################################
#######   Rental Product   ##############################################################################
#########################################################################################################
class RentalProduct(Product):
    className = "Rental Product"
    status = models.TextField(null=True, blank=True, choices=RENTAL_STATUS_CHOICES)
    purchase_date = models.DateField(null=True, blank=True, auto_now_add=True)
    # rental = models.ForeignKey('Rental', null=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Rental Product: %s (%s): %s' % (self.name, self.add_date, self.status)

admin.site.register(RentalProduct)


#########################################################################################################
####### Individual Product ##############################################################################
#########################################################################################################
class IndividualProduct(Product):
    className = "Individual Product"
    creator = models.ForeignKey('account.User')
    create_date = models.DateField(null=True, blank=True, auto_now_add=True)

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
