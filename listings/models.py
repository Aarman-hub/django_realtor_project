from django.db import models
from datetime import datetime
from django.utils import timezone
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
	realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
	title	= models.CharField(max_length=200)
	address = models.CharField(max_length=250, null=True)
	state 	= models.CharField(max_length=150, null=True)
	city 	= models.CharField(max_length=120, null=True, default='CA')
	zipcode = models.CharField(max_length=50, null=True)
	description = models.TextField()
	price = models.IntegerField(null=True)
	badrooms = models.IntegerField(null=True)
	bathrooms = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	gerage = models.IntegerField(null=True)
	sqft = models.IntegerField(null=True)
	lot_size = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	main_image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
	image_1 = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
	image_2 = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
	image_3 = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
	image_4 = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
	image_5 = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
	image_6 = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
	list_date = models.DateTimeField(auto_now_add=True)
	is_published= models.BooleanField(default=True)

	def __str__(self):
    		return self.title
	