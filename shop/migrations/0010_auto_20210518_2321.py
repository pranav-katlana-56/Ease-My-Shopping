# Generated by Django 3.1.7 on 2021-05-18 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210403_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='Price',
            field=models.IntegerField(max_length=50),
        ),
    ]
