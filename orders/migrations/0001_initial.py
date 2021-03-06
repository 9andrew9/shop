# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('dateofbirth', models.CharField(max_length=10, verbose_name='Дата рождения "11.11.1111"')),
                ('pasport', models.CharField(max_length=20, verbose_name='Серия и номер паспорта')),
                ('pasportreg', models.CharField(max_length=100, verbose_name='Кем и когда выдан')),
                ('pasportcode', models.CharField(max_length=10, verbose_name='Код подразделения')),
                ('adresspeg', models.CharField(max_length=100, verbose_name='Адрес регистрации')),
                ('adresspegreal', models.CharField(max_length=100, verbose_name='Адрес проживания')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачен')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
            ],
        ),
    ]
