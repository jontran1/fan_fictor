# Generated by Django 2.2.2 on 2019-07-20 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='id',
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
