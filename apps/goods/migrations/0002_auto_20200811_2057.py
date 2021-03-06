# Generated by Django 2.2 on 2020-08-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategorys',
            name='code',
            field=models.CharField(default='', max_length=30, verbose_name='商品类别编号'),
        ),
        migrations.AddField(
            model_name='goodscategorys',
            name='desc',
            field=models.TextField(default='', help_text='类别描述', verbose_name='类别描述'),
        ),
        migrations.AlterField(
            model_name='goodscategorys',
            name='name',
            field=models.CharField(default='', max_length=60, verbose_name='商品类别名称'),
        ),
    ]
