# Generated by Django 3.2.5 on 2021-07-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_alter_restaurant_pic_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='pic_icon',
            field=models.ImageField(height_field=200, upload_to='rest_images/', width_field=200),
        ),
    ]
