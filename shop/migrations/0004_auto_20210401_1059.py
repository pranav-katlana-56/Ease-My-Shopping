# Generated by Django 3.1.7 on 2021-04-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210330_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='Price_Amazon',
            field=models.CharField(default='10,000', max_length=12435),
        ),
        migrations.AddField(
            model_name='mobile',
            name='Price_flipkart',
            field=models.CharField(default=20000, max_length=10000),
        ),
        migrations.AddField(
            model_name='mobile',
            name='origin',
            field=models.CharField(default='Made in India', max_length=122),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='Brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='GSM',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='gadgets',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='kyg',
            field=models.IntegerField(),
        ),
    ]
