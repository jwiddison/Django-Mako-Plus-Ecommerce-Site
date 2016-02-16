from django.db import models
from django.contrib import admin


##################################
####### Base Product Class #######
##################################
class Product(models.Model):
    # Attributes
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)

    # Methods



##################################
#######   Rental Product   #######
##################################
class RentalProduct(Product):
    status = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'RentalProduct: %s (%s)' % (self.get_full_name(), self.name)

admin.site.register(RentalProduct)


##################################
####### Individual Product #######
##################################
class IndividualProduct(Product):
    creator = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'IndividualProduct: %s (%s)' % (self.get_full_name(), self.name)

admin.site.register(IndividualProduct)



##################################
#######    Bulk Product    #######
##################################
class BulkProduct(Product):
    quantity = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'BulkProduct: %s (%s)' % (self.get_full_name(), self.name)

admin.site.register(BulkProduct)
