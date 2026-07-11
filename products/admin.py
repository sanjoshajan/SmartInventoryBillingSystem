from django.contrib import admin
from .models import Brand, Unit, Product


admin.site.register(Brand)

admin.site.register(Unit)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "stock",
        "selling_price",
    )

    list_filter = (
        "category",
        "brand",
    )

    search_fields = (
        "name",
        "barcode",
    )