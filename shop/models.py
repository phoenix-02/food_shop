from django.contrib import admin
from django.db import models


class Category(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    title = models.CharField(max_length=100, verbose_name='Название Категории', help_text='введите название Категория')
    description = models.CharField(max_length=500, verbose_name='Описание')

    # возвращение дефолтного значения при обращении к обьекту

    def __str__(self):
        return self.title

    # Изменение заголовка модели в админке
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Модель блюда со своими полями и методами
class Dish(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    title = models.CharField(max_length=100, verbose_name='Название блюда', help_text='введите название блюда')
    categories = models.ManyToManyField(Category, verbose_name='категория', )
    description = models.CharField(max_length=500, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='цена')

    def get_categories(self):
        return [cat.title for cat in self.categories.all()]
    get_categories.short_description = "Категории"
    display_categories = property(get_categories)
    # возвращение дефолтного значения при обращении к обьекту
    def __str__(self):
        return self.title

    # Изменение заголовка модели в админке
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
