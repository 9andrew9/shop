from django.db import models

# Create your models here.


from django.db import models
from shop.models import Product
from shop.models import City


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Email')
    city = models.CharField(verbose_name='Город', max_length=100)
    dateofbirth = models.CharField(verbose_name='Дата рождения "11.11.1111"', max_length=10)
    pasport = models.CharField(verbose_name='Серия и номер паспорта', max_length=20)
    pasportreg = models.CharField(verbose_name='Кем и когда выдан', max_length=100)
    pasportcode = models.CharField(verbose_name='Код подразделения', max_length=10)
    adresspeg = models.CharField(verbose_name='Адрес регистрации', max_length=100)
    adresspegreal = models.CharField(verbose_name='Адрес проживания', max_length=100)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
