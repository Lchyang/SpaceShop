# Generated by Django 2.2 on 2020-08-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20200813_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodcategories',
            name='is_tab',
            field=models.BooleanField(default=False, verbose_name='是否导航'),
        ),
    ]