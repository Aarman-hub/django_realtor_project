# Generated by Django 2.2.7 on 2020-05-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_auto_20200522_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(),
        ),
    ]
