from django.db import models
from .common.model_common import default_meta
# Create your models here.


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


@default_meta
class Users(models.Model):
    user_email = models.EmailField()
    user_phone_number = models.CharField(max_length=20, blank=True, null=True)
    user_password = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_surname = models.CharField(max_length=255)
    user_birthday = models.DateField()
    user_address = models.CharField(max_length=255, blank=True, null=True)


@default_meta
class OrderedProducts(models.Model):
    order_date = models.DateField()
    order_quantity = models.IntegerField()
    sent_form_warehouse = models.BooleanField(default=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    goods_with_attributes_values_id = models.ForeignKey(GoodsWithAttributesValues, on_delete=models.CASCADE)
