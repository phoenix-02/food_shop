from django.contrib import admin
from .models import Dish


# admin.site.register(Dish)
# регистрация модели в админке
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    # список отображаемых полей модели
    list_display = ['id', 'title', 'dish_type', 'description']
