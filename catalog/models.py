from django.conf import settings
from django.db import models
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/',verbose_name = 'изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    creat_date = models.DateField(auto_now=True, verbose_name='дата создания')
    change_date = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')


    def __str__(self):
        return f'{self.name} '

    @property
    def active_version(self):
        return self.version_set.get(current_version=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Contacts(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    email = models.CharField(max_length=150, verbose_name='e-mail')
    message = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta():
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'



class Blog(models.Model):
    name = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.CharField(max_length=255, verbose_name='slug', unique=True)
    content = models.TextField(verbose_name='контент', **NULLABLE)
    image = models.ImageField(upload_to='blog/media/', verbose_name='превью', **NULLABLE)
    create_date = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.name}'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta():
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('create_date',)



class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт")
    version_num = models.IntegerField(default=0, verbose_name="номер версии")
    version_title = models.CharField(max_length=255, verbose_name="название версии")
    is_version = models.BooleanField(default=True)

    def __str__(self):
       return f'{self.version_title}'


    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

