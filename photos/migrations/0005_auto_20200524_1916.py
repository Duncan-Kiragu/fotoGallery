# Generated by Django 3.0.6 on 2020-05-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20200524_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='gallery_image',
        ),
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
