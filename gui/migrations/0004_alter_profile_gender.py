# Generated by Django 3.2.6 on 2021-08-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0003_alter_profile_profile_iris_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], default=1, max_length=6),
        ),
    ]
