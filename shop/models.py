from django.db import models
from django.utils.translation import ugettext_lazy


# Модель блюда со своими полями и методами
class Dish(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    title = models.CharField(max_length=100, verbose_name='Название блюда', help_text='введите название блюда')
    dish_type = models.CharField(max_length=100, verbose_name='Тип блюда')
    description = models.CharField(max_length=500, verbose_name='Описание')

    # возвращение дефолтного значения при обращении к обьекту
    def __str__(self):
        return self.title

    # Изменение заголовка модели в админке
    class Meta:
        verbose_name = ugettext_lazy("Блюдо")
        verbose_name_plural = ugettext_lazy("Блюда")
