# Generated by Django 3.2.6 on 2021-08-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_iris_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
