from django.shortcuts import render, get_object_or_404
from .models import Goods


def products_page(request):
    desired_product_id = request.GET.get('id')
    product = get_object_or_404(Goods, pk=desired_product_id)
    # TODO add comments to db and provide query for retrival
    # comment =
    print(product)
    return render(request,
                  'products/templates/product-detail.html',
                  {'product': product,
                   'comments': 'null'}
                  )
