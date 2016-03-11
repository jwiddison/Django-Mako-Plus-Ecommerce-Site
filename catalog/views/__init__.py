from catalog.models import Product

def translate_product(request):
    '''Translates list of product ids to product objects.'''
    pList = []
    for p_id in request.session.get('recently_viewed', []):
        pList.append(Product.objects.get(id=p_id))
    pList.reverse()
    return pList
