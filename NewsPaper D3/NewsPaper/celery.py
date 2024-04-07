import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# для запуска период. задач, после запуска celery,
# в отдельном окне терминала внести "celery -A PROJECT beat -l INFO"
app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.my_job',
        'schedule': crontab(hour='8', minute='0', day_of_week='monday'),
    },
}
