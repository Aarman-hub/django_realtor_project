# Generated by Django 2.2.7 on 2020-05-22 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20200522_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='gerage',
            field=models.IntegerField(null=True),
        ),
    ]