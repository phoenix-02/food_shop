from django.shortcuts import render
from .models import Dish


def view_dishes(request):
    all_dishes = Dish.objects.all()
    return render(request, 'index.html', {'dishes': all_dishes})
