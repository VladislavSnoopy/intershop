from django.db import models
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    parent_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.CharField(max_length=600, verbose_name='Описание')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовать?')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.CharField(max_length=600, verbose_name='Описание')
    price = models.CharField(max_length=30, verbose_name='Цена')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовать?')
    Top = models.BooleanField(default=True, verbose_name='Лучший товар')
    New = models.BooleanField(default=True, verbose_name='Новый товар')
    Featured = models.BooleanField(default=True, verbose_name='Рекомендуемое')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class Card(models.Model):
    id_product = models.CharField(max_length=150, verbose_name='Наименование')
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.id_product

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
