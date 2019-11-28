from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.CharField(max_length=1024, primary_key=True)
	user_pw = models.CharField(max_length=1024)
	user_email = models.CharField(max_length=1024)

class Item(models.Model):
	item_id = models.CharField(max_length=1024, primary_key=True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	item_url = models.CharField(max_length=1024)
	item_domain = models.CharField(max_length = 16)
	item_name = models.CharField(max_length=1024)
	item_price = models.CharField(max_length=1024)
	item_image = models.CharField(max_length=1024)
