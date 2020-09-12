from celery.task import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер {order_id}'
    message = f'Уважаемый {order.first_name}, \n\n' \
              f'Ваш заказ успешно обработан.' \
              f'ID вашего заказа {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@arty-shop.com', [order.email])
    return mail_sent
