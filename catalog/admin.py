from django.contrib import admin

from catalog.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price','category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'is_published', 'view_count', 'slug')
    list_filter = ('view_count',)
    search_fields = ('name', 'content',)
    prepopulated_fields = {"slug": ("name",)}