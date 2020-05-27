# Generated by Django 2.2.7 on 2020-05-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]