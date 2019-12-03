from django.db import models

# Create your models here.
class Tag(models.Model):
	domain_name = models.CharField(max_length=16, primary_key=True) 
	tag_domain = models.CharField(max_length=16)
	tag_name = models.CharField(max_length=255)
	tag_price = models.CharField(max_length=255)
	tag_image = models.CharField(max_length=255)
