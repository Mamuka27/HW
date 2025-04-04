from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock', 'slug'] 
    prepopulated_fields = {'slug': ('name',)}  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'view_count', 'slug']
    prepopulated_fields = {'slug': ('name',)}
