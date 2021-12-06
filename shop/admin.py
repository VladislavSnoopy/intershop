from django.contrib import admin

from .models import Category, Product, Card, Blog

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Card)
admin.site.register(Blog)
