from celery import shared_task
from mail_templated import send_mail

# from django.core.mail import send_mail  # for MailDev


# @shared_task
# def notify_order_saved(order_pk, promocode):
#     from time import sleep
#     sleep(3)
#
#     send_mail(
#         f"Order #{order_pk} saved",
#         f"Here is the message. Order #{order_pk}, promocode: {promocode}",
#         "from@example.com",
#         ["to@example.com"],
#         fail_silently=True,  # НЕ показываем ошибку юзеру
#     )

@shared_task
def notify_order_saved(order_pk, promocode):

    # from time import sleep
    # sleep(8)

    # send_mail(
    #     f"Order #{order_pk} saved!!!!!!!!!!!!!!",
    #     f"Here is the message. Order #{order_pk}, promocode: {promocode}",
    #     "from@example.com",
    #     ["to@example.com"],
    #     fail_silently=False,
    # )

    send_mail(
        "email/order-updated.html",
        {
            "order_pk": order_pk,
            "promocode": promocode,
        },
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )