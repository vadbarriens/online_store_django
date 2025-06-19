from django.db import models

from users.models import User
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name='описание категории', help_text='опишите категорию')
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование продукта',
                            help_text='введите наименование продукта')
    description = models.TextField(verbose_name='описание продукта', help_text='опишите продукт')
    image = models.ImageField(upload_to='products/photo', blank=True, null=True, verbose_name='изображение',
                              help_text='загрузите изображение продукта')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.FloatField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publication_status = models.BooleanField(default=False)

    owner = models.ForeignKey(User, verbose_name='Владелец', help_text='Укажите владельца продукта', blank=True,
                              null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['price', 'name', 'category']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

    def __str__(self):
        return f'{self.name}: {self.description}'
