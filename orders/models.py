from django.db import models

from product.models import Laptop


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(verbose_name='Адрес', max_length=250)
    postal_code = models.CharField(verbose_name='Почтовый индекс', max_length=20)
    city = models.CharField(verbose_name='Город', max_length=100)
    created = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлено', auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item  in self.items.all())

    class Meta:
        ordering = ('-created',)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказчик')
    product = models.ForeignKey(Laptop, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
