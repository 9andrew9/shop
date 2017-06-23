from celery import task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
# from shop.models import Product
#import psycopg2


@task
def OrderCreated(order_id, total_price, product_name):
    """
    Отправка Email сообщения о создании покупке
    """

    order = Order.objects.get(id=order_id)
    subject = 'Заказ c номером {}'.format(order.id)
    message = "Уважаемый, {} {}, вы успешно сделали заказ.\nНомер вашего заказа: {}\nПеречень Вашего заказа:\n{}\nОбщая сумма: {}\nДата рождения: {}\nГород регистрации: {}\nСерия и номер паспорта: {}\nКем и когда выдан: {}\nКод подразделения: {}\nАдрес регистрации: {}\nАдрес проживания: {}".format(
        order.first_name, order.last_name, order.id, product_name, total_price, order.dateofbirth, order.city,
        order.pasport, order.pasportreg, order.pasportcode, order.adresspeg, order.adresspegreal)
    mail_send = send_mail(subject, message, 'zakupki@europlan.ru', [order.email, 'avs85@europlan.ru'],
                          settings.EMAIL_HOST)
    return mail_send
