from django.contrib import admin

from .models import Product, Stock, StockProduct


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]
