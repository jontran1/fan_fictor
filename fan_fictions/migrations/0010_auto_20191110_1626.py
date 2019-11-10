# Generated by Django 2.2.2 on 2019-11-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fan_fictions', '0009_entry_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='chapter_cover',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/9/9b/No_cover.JPG', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='story_cover',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/9/9b/No_cover.JPG', max_length=100),
            preserve_default=False,
        ),
    ]