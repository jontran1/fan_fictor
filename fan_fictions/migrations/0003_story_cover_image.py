# Generated by Django 2.2.2 on 2019-06-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fan_fictions', '0002_auto_20190603_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='cover_image',
            field=models.CharField(default='https://i.imgur.com/LRoLTlK.jpg', max_length=200),
            preserve_default=False,
        ),
    ]