from django.contrib import admin
from .models import Category, Car, Booking


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'price', 'year', 'condition', 'availability']
    list_editable = ['price', 'condition', 'availability']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


admin.site.register(Car, CarAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'car']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


admin.site.register(Booking, BookingAdmin)

