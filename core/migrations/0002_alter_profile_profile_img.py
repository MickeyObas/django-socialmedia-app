# Generated by Django 4.0.5 on 2022-07-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='media\\wink.wink.png', upload_to='profile_images'),
        ),
    ]
