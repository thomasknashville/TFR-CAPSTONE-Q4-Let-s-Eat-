# Generated by Django 3.2.5 on 2021-07-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_tfruser_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfruser',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img/'),
        ),
    ]
