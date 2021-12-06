from django.shortcuts import render, redirect
from .models import Category, Product, Card, Blog
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout


def deleteproduct(request):

    try:
        user_id_f = request.user
        product = Card.objects.all()
        product.delete()

        k = True

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"user_form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"user_form": form})


def index(request):
    categories = Category.objects.filter(parent_category=None)
    product = Product.objects.all()
    blog = Blog.objects.all()

    return render(request, 'index.html', {'blog': blog, 'categories': categories, 'product': product})


def card(request, card_id):
    if request.user.is_authenticated:
        user_id_f = request.user
        Card.objects.create(id_product=card_id, pk=card_id, user_id=user_id_f)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def card_out(request):
    cards = []

    if request.user.is_authenticated:

        user_id_f = request.user
        card = Card.objects.filter(user_id=user_id_f)

        for item in card:
            p = int(item.id_product)
            cards.append(p)
    cards_out = Product.objects.filter(pk__in=cards)

    return render(request, 'cart.html', {'cards_out': cards_out})


def shop(request):
    product = Product.objects.all()

    return render(request, 'shop_cart.html', {'product': product})


def blog(request, blog_id):

    blog = Blog.objects.get(pk=blog_id)

    return render(request, 'blog.html', {'blog': blog})
