from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from news.models import Post

import datetime
from django.utils import timezone
from django.template.loader import render_to_string
from django.conf import settings


# D7
@shared_task
def send_notification(arg_id):
    instance = Post.objects.get(id=arg_id)
    emails = User.objects.filter(
        subscriptions__category__in=instance.category_post_many.all()
    ).values_list('email', flat=True)

    subject = f'Новая публикация в категории {instance.category_post_many.all()}'

    text_content = (
        f'Новая публикация: {instance.title}\n'
        f'Ссылка: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новая публикация: {instance.title}<br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task
def my_job():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    new_posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(new_posts.values_list('category_post_many__name', flat=True))
    subscribers = set(User.objects.filter(subscriptions__category__name__in=categories).values_list('email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'new_posts': new_posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
