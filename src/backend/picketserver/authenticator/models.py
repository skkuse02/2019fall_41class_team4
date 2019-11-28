from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.CharField(max_length=1024, primary_key=True)
	user_pw = models.CharField(max_length=1024)
	user_email = models.CharField(max_length=1024)

class Cart_items(models.Model):
	item_id = models.CharField(max_length=1024, primary_key=True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.CharField(max_length=1024)
	price = models.CharField(max_length=1024)
	img_url = models.CharField(max_length=1024)
	item_name = models.CharField(max_length=1024)
