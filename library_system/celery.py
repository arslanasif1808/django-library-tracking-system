import os
from datetime import timezone

from celery import Celery
from library.models import Loan
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def mark_overdue_loans():
    today= timezone.now().date()

    overdue_loans = Loan.objects.filter(
        is_returned=False,
        due_date__lt= today
    )

    count = overdue_loans.update(status="overdue")

    return f"{count} loans marked as overdue"


@app.task
def data_crawl(base_path):

    link_pattern= re.compile(r"/[")
    files_data= {

    }
    outgoing_graph= {}
    backlink_graph = {}

    for root, __, files in os.walk(base_path):
        for file in files:
            if file.endswith((".md", "txt"))

