# Generated by Django 2.2 on 2020-08-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_actions', '0003_auto_20200818_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userleavemsg',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='message/files', verbose_name='留言文件'),
        ),
    ]
