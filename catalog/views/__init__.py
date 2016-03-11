from catalog.models import Product

def translate_product(request):

    # # Create a list of products
    # products = Product.objects.all()
    pList = []

    for p_id in request.session['recently_viewed']:
        pList.append(Product.objects.get(id=p_id))

    pList.reverse()

    return pList
