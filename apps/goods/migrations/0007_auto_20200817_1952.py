# Generated by Django 2.2 on 2020-08-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_goodcategories_is_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='是否热销'),
        ),
        migrations.AddField(
            model_name='goods',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='是否新品'),
        ),
    ]