# from django.contrib import admin

# Register your models here.



# ------
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
        'status',
        'date_creation'
    )

    list_filter = ('status', 'date_creation')
    search_fields = ('first_name', 'last_name', 'phone_number')

    ordering = ('-date_creation',)
