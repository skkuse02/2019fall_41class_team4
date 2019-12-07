from django.contrib import admin
from .models import Tag, RTag

# Register your models here.
class TagAdmin(admin.ModelAdmin):
	list_display = ['tag_domain']

class RTagAdmin(admin.ModelAdmin):
	list_display = ['domain_name']

admin.site.register(Tag, TagAdmin)
admin.site.register(RTag, RTagAdmin)
