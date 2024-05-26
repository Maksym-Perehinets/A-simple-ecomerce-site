# Generated by Django 5.0.6 on 2024-05-26 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=255)),
                ('goods_price', models.IntegerField()),
                ('goods_description', models.TextField()),
                ('goods_image', models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user_password', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('user_surname', models.CharField(max_length=255)),
                ('user_birthday', models.DateField()),
                ('user_address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsWithAttributesValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_in_warehouse', models.IntegerField()),
                ('attribute_value', models.IntegerField()),
                ('attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.attributes')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.goods')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('order_quantity', models.IntegerField()),
                ('sent_form_warehouse', models.BooleanField(default=False)),
                ('goods_with_attributes_values_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.goodswithattributesvalues')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.users')),
            ],
        ),
    ]