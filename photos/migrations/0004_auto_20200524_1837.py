# Generated by Django 3.0.6 on 2020-05-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20200524_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
    ]