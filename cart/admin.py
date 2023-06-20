from typing import List

from django.contrib import admin

from .models import (
    Product,
    OrderItem,
    Order,
    ColourVariation,
    SizeVariation,
    Address,
    Payment,
    Category,
    StripePayment,
    ProductImage
)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display: List[str] = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(SizeVariation)
admin.site.register(StripePayment)
admin.site.register(ColourVariation)
admin.site.register(ProductImage)
