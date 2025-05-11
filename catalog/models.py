from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование продукта',
                            help_text='введите наименование продукта')
    discription = models.TextField(verbose_name='описание продукта', help_text='опишите продукт')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='изображение',
                              help_text='загрузите изображение продукта')
    category = models.CharField(max_length=150, verbose_name='категория', help_text='введите категорию продукта')
    price = models.FloatField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}: {self.discription}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['category']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='категория', help_text='введите категорию')
    discription = models.TextField(verbose_name='описание категории', help_text='опишите категорию')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
