from celery import Celery
from doom.settings import get_config


config = get_config()
worker = Celery('tasks', broker=config.CELERY_BROKER)


@worker.task
def async_add_task(arg1, arg2):
    print("async_add_task running")
    print("result: ", arg1 + arg2)

