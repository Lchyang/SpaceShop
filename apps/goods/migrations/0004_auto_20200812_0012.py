# Generated by Django 2.2 on 2020-08-12 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goods_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='商品描述'),
        ),
    ]
