# Generated by Django 2.2.7 on 2020-05-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20200522_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='main_image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
