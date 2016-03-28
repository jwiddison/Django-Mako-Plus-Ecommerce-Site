# from catalog.models import Product
from catalog.models import Category

# def translate_product(request):
#
#     '''Sprint 4 stuff (Depricated) '''
#     '''Translates list of product ids to product objects.'''
#     pList = []
#     for p_id in request.session.get('recently_viewed', []):
#         pList.append(Product.objects.get(id=p_id))
#     pList.reverse()
#
#     '''Sprint 5 Stuff'''
#     template_vars = {}
#     template_vars['categories'] = Category.objects.order_by('name')
#
#     return pList

def initialize_template_vars(request):
    '''Initializes the template vars with the categories and last 5 items viewed'''
    template_vars = {}

    # add the catgories
    template_vars['categories'] = Category.objects.order_by('name')

    # return
    return template_vars
