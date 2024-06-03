from django.contrib import admin
from .models import Products

# Register your models here.
# admin.site.register(Products)
@admin.register(Products)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["company","name"]
    list_display_links = ["company", "name"]
    list_filter = ["end_date"]
    search_fields = ["name"]
    class Meta:
        model = Products