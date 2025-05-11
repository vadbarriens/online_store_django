from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name='описание категории', help_text='опишите категорию')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование продукта',
                            help_text='введите наименование продукта')
    description = models.TextField(verbose_name='описание продукта', help_text='опишите продукт')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='изображение',
                              help_text='загрузите изображение продукта')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.FloatField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['category']

    def __str__(self):
        return f'{self.name}: {self.description}'
