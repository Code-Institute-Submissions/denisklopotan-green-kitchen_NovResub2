from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'created_on')
    search_fields = ('fname', 'lname', 'email', 'subject', 'body')
    list_filter = ('fname', 'lname', 'email')
