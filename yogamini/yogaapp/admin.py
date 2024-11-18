from django.contrib import admin
from.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','firstname','email',]
    ordering=('-firstname',)
    search_fields=('firstname',)

admin.site.register(Customer,CustomerAdmin)