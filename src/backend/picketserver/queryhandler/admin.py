from django.contrib import admin
from .models import QueryDomain, QueryElse

# Register your models here.
class QueryDomainAdmin(admin.ModelAdmin):
	list_display = ['domain_url', 'original_url']
	list_filter = ['domain_url']

class QueryElseAdmin(admin.ModelAdmin):
	list_display = ['user_comment']

admin.site.register(QueryDomain, QueryDomainAdmin)
admin.site.register(QueryElse, QueryElseAdmin)
