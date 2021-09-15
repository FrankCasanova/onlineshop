from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Product)
class ProducAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'aviable', 'created', 'updated']
    list_filter = ['aviable', 'created', 'updated']
    list_editable = ['price', 'aviable']
    prepopulated_fields = {'slug': ('name',)}
