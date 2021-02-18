from django.shortcuts import render
from .models import Dish
from .forms import SearchForm


def view_dishes(request):
    search = ""
    try:
        form = SearchForm(request.POST)
        if form.is_valid():
            search = request.POST.get('search')
    except Exception:
        form = SearchForm()
    all_dishes = Dish.objects.filter(title=search)

    return render(request, 'index.html',
                  {'dishes': all_dishes, 'form': form})
