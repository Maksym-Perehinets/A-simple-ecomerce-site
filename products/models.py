from django.db import models

# Create your models here.


class Goods(models.Model):
    """
    Represents data about goods
    """
    goods_name = models.CharField(max_length=255)
    goods_price = models.IntegerField()
    goods_description = models.TextField()

    class Meta:
        abstract = False


class Attributes(models.Model):
    attribute_name = models.CharField(max_length=255)

    class Meta:
        abstract = False


class GoodsWithAttributesValues(models.Model):
    """
    Represents data about Goods with attributes, and it's amount's in warehouse
    """
    amount_in_warehouse = models.IntegerField()
    attribute_value = models.IntegerField()
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    attribute_id = models.ForeignKey(Attributes, on_delete=models.CASCADE)

    class Meta:
        abstract = False


class Users(models.Model):
    """
    Represents data about users and their delivery information
    """
    user_email = models.EmailField()
    user_phone_number = models.CharField(max_length=20, blank=True, null=True)
    user_password = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_surname = models.CharField(max_length=255)
    user_birthday = models.DateField()
    user_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = False


class OrderedProducts(models.Model):
    order_date = models.DateField()
    order_quantity = models.IntegerField()
    sent_form_warehouse = models.BooleanField(default=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    goods_with_attributes_values_id = models.ForeignKey(GoodsWithAttributesValues, on_delete=models.CASCADE)

    class Meta:
        abstract = False
