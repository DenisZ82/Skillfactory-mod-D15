from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post, PostCategory
from django.conf import settings
from .tasks import send_notification


@receiver(m2m_changed, sender=PostCategory, weak=False)
def news_created(instance, **kwargs):
    if kwargs['action'] == 'post_add':
        send_notification.delay(instance.pk)


# D6
# @receiver(m2m_changed, sender=PostCategory)
# def news_created(sender, instance, action, **kwargs):
#     if action == 'post_add':
#         emails = User.objects.filter(
#             subscriptions__category__in=instance.category_post_many.all()
#         ).values_list('email', flat=True)
#
#         subject = f'Новая публикация в категории {instance.category_post_many.all()}'
#
#         text_content = (
#             f'Новая публикация: {instance.title}\n'
#             f'Ссылка: http://127.0.0.1:8000{instance.get_absolute_url()}'
#         )
#         html_content = (
#             f'Новая публикация: {instance.title}<br>'
#             f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
#             f'Ссылка</a>'
#         )
#         for email in emails:
#             msg = EmailMultiAlternatives(subject, text_content, None, [email])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()
#
#     return
