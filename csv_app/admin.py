from django.contrib import admin
from .models import keyword_info, buisness_leads

# Register your models here.
class dataAdmin(admin.ModelAdmin):
    list_display=['title', 'email', 'number']
class leadsAdmin(admin.ModelAdmin):
    list_display=['name', 'phone_number', 'address', 'website', 'status', 'rating', 'url']

admin.site.register(keyword_info,dataAdmin)
admin.site.register(buisness_leads,leadsAdmin)