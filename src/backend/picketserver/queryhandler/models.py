from django.db import models

# Create your models here.

class QueryDomain(models.Model):
	original_url = models.CharField(max_length = 1024)
	domain_url = models.CharField(max_length = 128)

class QueryElse(models.Model):
	user_comment = models.CharField(max_length = 2048)
