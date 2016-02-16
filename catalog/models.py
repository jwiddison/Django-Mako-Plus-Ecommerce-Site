from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel

#########################################################################################################
####### Base Product Class ##############################################################################
#########################################################################################################
class Product(models.Model):
    '''Superclass for all other product types '''
    # Attributes
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    add_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    image = models.TextField(null=True, blank=True)

    # Methods
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
    status = models.TextField(null=True, blank=True, choices=RENTAL_STATUS_CHOICES)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'RentalProduct: %s (%s): %s' % (self.name, self.add_date, self.status)

admin.site.register(RentalProduct)


#########################################################################################################
####### Individual Product ##############################################################################
#########################################################################################################
class IndividualProduct(Product):
    creator = models.ForeignKey('account.User')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'IndividualProduct: %s (%s): %s' % (self.name, self.add_date, self.creator.get_full_name())

admin.site.register(IndividualProduct)



#########################################################################################################
#######    Bulk Product    ##############################################################################
#########################################################################################################
class BulkProduct(Product):
    quantity = models.IntegerField(default=0)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'BulkProduct: %s (%s): %s' % (self.name, self.add_date, self.quantity)

admin.site.register(BulkProduct)
