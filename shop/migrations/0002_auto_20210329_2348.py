# Generated by Django 3.1.7 on 2021-03-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='Amazon_Link',
            field=models.CharField(default='amazon', max_length=3000),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='Flipkart_Link',
            field=models.CharField(default='flipkart', max_length=3000),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='category',
            field=models.CharField(default='Android', max_length=122),
        ),
    ]
