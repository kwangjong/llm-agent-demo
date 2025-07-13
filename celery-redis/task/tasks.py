from celery import shared_task

@shared_task
def async_add(x, y):
    return x + y

@shared_task
def async_mult(x, y):
    return x * y
