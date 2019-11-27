from django.db import models

# Create your models here.
class Item(models.Model):
	domain_name = models.CharField(max_length=16, primary_key=True) 
	item_domain = models.CharField(max_length=16)
	item_name = models.CharField(max_length=255)
	item_price = models.CharField(max_length=16)
	item_image = models.CharField(max_length=255)
