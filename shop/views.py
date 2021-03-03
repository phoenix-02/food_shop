from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Dish, Category
from .forms import SearchForm, LoginForm, RegisterForm, EditForm
from django.contrib.postgres.search import SearchVector
from django.db.models import Q


def search_dishes(request):
    all_dishes = Dish.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        search = request.POST.get('search')
        if form.is_valid() and search:
            search_vector = SearchVector('title',
                                         'description',
                                         'categories__title',
                                         'company__title', )
            all_dishes = Dish.objects.annotate(search=search_vector).filter(search=search)
            # альтернатива, без использования annotate и SearchVector
            # all_dishes = Dish.objects.filter(
            #     Q(title__icontains=search) |
            #     Q(categories__title__icontains=search))

    else:
        form = SearchForm()

    return render(request, 'base.html',
                  {'dishes': all_dishes, 'form': form, 'user': request.user})


def view_category(request):
    category_id = request.GET.get("category_id")
    category = Category.objects.filter(id=category_id)
    return render(request, 'category.html', {'category': category})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditForm(instance=request.user)
    return render(request, 'login.html', {'form': form, 'submit_text': 'Изменить', 'auth_header': 'Изменение профиля'})


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

    return render(request, 'login.html', {'form': form, 'submit_text': 'Войти', 'auth_header': 'Вход'})


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
    return render(request, 'login.html',
                  {'form': form, 'submit_text': 'Зарегистрироваться', 'auth_header': 'Регистрация'})


def log_out(request):
    logout(request)
    return redirect('/')
