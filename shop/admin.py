# Register your models here.
from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    repopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Device, DeviceAdmin)


class ApartmentLayoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ApartmentLayout, ApartmentLayoutAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(City, CityAdmin)

class CampusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Campus, CampusAdmin)


class Administrative_divisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Administrative_division, Administrative_divisionAdmin)


class UpdownAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Updown, UpdownAdmin)

class LayoutAdmin(admin.ModelAdmin):
    list_display = ['bedroom_count', 'bashroom_count', 'livingroom_count']
    prepopulated_fields = {'slug': ('bedroom_count', 'bashroom_count', 'livingroom_count')}
admin.site.register(Layout,LayoutAdmin)