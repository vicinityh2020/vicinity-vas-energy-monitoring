from __future__ import absolute_import, unicode_literals
from celery import task
from application.models import SensorUsage


@task()
def task_number_one():
    q = SensorUsage.objects.all()
    for u in q:
        print(u)

@task()
def background_task():
    print("doing some work in background")