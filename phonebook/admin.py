from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address')
    search_fields = ('last_name',)
    ordering = ['first_name', 'last_name', 'email']


admin.site.register(Contact, ContactAdmin)
