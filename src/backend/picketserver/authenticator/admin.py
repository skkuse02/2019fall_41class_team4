from django.contrib import admin
from .models import User, Item

# Register your models here.
#admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'user_pw', 'user_email']

class ItemAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'item_domain', 'item_name']

admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
