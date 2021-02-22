from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Dish
from .forms import SearchForm, LoginForm, RegisterForm


def add_dish(request):
    some_dish = Dish(title='рамен2', image='img.jpg', price=500, )
    some_dish.save()

    Dish.objects.create(title='рамен', image=' ', price=500, )
    return redirect('index')


def view_dishes(request):
    all_dishes = Dish.objects.all()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = request.POST.get('search')
            all_dishes = all_dishes.filter(title=search)
    else:
        form = SearchForm()

    return render(request, 'base.html',
                  {'dishes': all_dishes, 'form': form,'user':request.user})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # if request.GET and 'next' in request.GET:
                #     return redirect(request.GET['next'])
                return redirect('/')
            else:
                form.add_error('login', 'Bad login or password')
                form.add_error('password', 'Bad login or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'login.html', {'form': form})
