from django.contrib import admin

from .models import Item, Brand, Category, Body, Posts

admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Body)
admin.site.register(Posts)