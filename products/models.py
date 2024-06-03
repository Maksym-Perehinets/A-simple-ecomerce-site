from django.db import models
from .common.model_common import default_meta


@default_meta
class Goods(models.Model):
    goods_name = models.CharField(max_length=255)
    goods_price = models.IntegerField()
    goods_description = models.TextField()
    goods_image = models.URLField(max_length=500, blank=True)


@default_meta
class Attributes(models.Model):
    attribute_name = models.CharField(max_length=255)


@default_meta
class GoodsWithAttributesValues(models.Model):
    amount_in_warehouse = models.IntegerField()
    attribute_value = models.IntegerField()
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    attribute_id = models.ForeignKey(Attributes, on_delete=models.CASCADE)
