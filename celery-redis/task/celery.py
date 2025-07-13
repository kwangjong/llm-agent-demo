from celery import Celery

# Initialize the Celery application
app = Celery(
    'async_calls',
    broker='redis://localhost:6379/0',  #queue
    backend='redis://localhost:6379/0',  #result store
    result_expires=3600,  # Task result expiration time
)

# Load tasks from a module
app.autodiscover_tasks(['task'])