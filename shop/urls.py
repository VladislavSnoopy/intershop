from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('card_products/', card_out, name='card_products'),
    path('shop/', shop, name='shop'),
    path('blog/<int:blog_id>/', blog, name='blog'),
    path('card/<int:card_id>/', card, name='card'),
    path('deleteproduct/', deleteproduct, name='deleteproduct'),

]
