from django.contrib import admin
from .models import User

# Register your models here.
#admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'user_pw', 'user_email']

admin.site.register(User, UserAdmin)
