from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:by_category', args=[self.url])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductAbstract(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', db_index=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    short_description = models.CharField(max_length=200, verbose_name='Короткое описание', blank=True)
    url = models.SlugField(db_index=True, unique=True)
    image = models.ImageField('Картинка', upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(verbose_name='В наличии', default=False)
    category = models.ForeignKey(Category, models.CASCADE, 'products')
    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:detail', args=[self.id, self.url])

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
        ordering = ('title',)
        index_together = (('id', 'url'),)
        abstract = True


# Классы для ноутбука ..............................
class Laptop(ProductAbstract):
    core = models.ForeignKey('LaptopCore', on_delete=models.CASCADE, related_name='laptops',
                             verbose_name='Процессор')
    diagonal = models.ForeignKey('LaptopScreenDiagonal', on_delete=models.CASCADE, related_name='laptops',
                                 verbose_name='Диагональ экрана')
    refresh_rate = models.ForeignKey('LaptopRefreshRate', on_delete=models.CASCADE, related_name='laptops',
                                     verbose_name='Частота обновлений экрана')
    ram = models.ForeignKey('LaptopRAM', on_delete=models.CASCADE, related_name='laptops',
                            verbose_name='Оперативная память (ОЗУ)')

    storage = models.ForeignKey('LaptopStorage', on_delete=models.CASCADE, related_name='laptops',
                                verbose_name='Тип хранилища')
    os = models.ForeignKey('LaptopOS', on_delete=models.CASCADE, related_name='laptops',
                           verbose_name='Операционная система')
    color = models.ForeignKey('LaptopColor', on_delete=models.CASCADE, related_name='laptops',
                              verbose_name='Цвет', blank=True, null=True)


class LaptopScreenDiagonal(models.Model):
    value = models.CharField(verbose_name='Диагональ', max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ('value',)
        verbose_name = 'Диагональ экрана (Ноутбук)'
        verbose_name_plural = 'Список диагоналей (Ноутбуки)'


class LaptopCore(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Процессор (Ноутбук)'
        verbose_name_plural = 'Процессоры (Ноутбуки)'

    def __str__(self):
        return self.name


class LaptopRefreshRate(models.Model):
    value = models.CharField(verbose_name='Частота обновлений экрана', max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ('value',)
        verbose_name = 'Частота обновлений экрана (Ноутбук)'
        verbose_name_plural = 'Список частот обновлений (Ноутбуки)'


class LaptopRAM(models.Model):
    name = models.CharField(verbose_name='Полное название', max_length=50, blank=True, null=True)
    value = models.CharField(verbose_name='Кол-во оперативной памяти (ОЗУ)', max_length=50)
    ram_type = models.ForeignKey('LaptopRAMType', on_delete=models.CASCADE, verbose_name='Тип ОЗУ')

    def __str__(self):
        return f'{self.value} {self.ram_type}'

    class Meta:
        ordering = ('value',)
        verbose_name = 'Оперативная память (ОЗУ) (Ноутбук)'
        verbose_name_plural = 'Список ОЗУ (Ноутбуи)'


class LaptopRAMType(models.Model):
    ram_type = models.CharField(verbose_name='Тип ОЗУ', max_length=50)

    def __str__(self):
        return self.ram_type

    class Meta:
        ordering = ('ram_type',)
        verbose_name = 'Тип ОЗУ (Ноутбук)'
        verbose_name_plural = "Типы ОЗУ (Ноутбуки)"


class LaptopColor(models.Model):
    name = models.CharField(verbose_name='Цвет', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цвет (Ноутбук)'
        verbose_name_plural = 'Цвета (Ноутбуки)'


class LaptopOS(models.Model):
    name = models.CharField(verbose_name='Операционная система (ОС)', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Операционная система (Ноутбук)'
        verbose_name_plural = 'Операционные системы (Ноутбуки)'


class LaptopStorage(models.Model):
    name = models.CharField(verbose_name='Полное название', max_length=150)
    storage_type = models.ForeignKey('LaptopStorageType', on_delete=models.CASCADE, verbose_name='Тип хранилища')
    storage_size = models.ForeignKey('LaptopStorageSize', on_delete=models.CASCADE, verbose_name='Размер хранилища')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Хранилище (Ноутбук)'
        verbose_name_plural = "Хранилища (Ноутбуки)"


class LaptopStorageSize(models.Model):
    size = models.PositiveSmallIntegerField(verbose_name='Размер хранилища')

    def __str__(self):
        return str(self.size)

    class Meta:
        ordering = ('size',)
        verbose_name = 'Размер хранилища (Ноутбук)'
        verbose_name_plural = 'Размеры хранилищ (Ноутбуки)'


class LaptopStorageType(models.Model):
    storage_type = models.CharField(verbose_name='Тип хранилища', max_length=50)

    def __str__(self):
        return self.storage_type

    class Meta:
        ordering = ('storage_type',)
        verbose_name = 'Тип хранилища (Ноутбук)'
        verbose_name_plural = 'Типы хранилищ (Ноутбуки)'

# ..................................................................................
