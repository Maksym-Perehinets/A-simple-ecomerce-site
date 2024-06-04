from django.shortcuts import render
from products.models import Goods, GoodsWithAttributesValues


def main(request):
    suitable_items = GoodsWithAttributesValues.objects.filter(amount_in_warehouse__gt=0)
    products = Goods.objects.filter(
        pk__in=(
            suitable_items.values_list('goods_id', flat=True)
        )
    )[:8]
    return render(request, "templates/index.html", {'products': products})
