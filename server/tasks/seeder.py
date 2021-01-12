from celery import shared_task
from ..utils import SeederUtil

@shared_task
def seed_db():
    seeder = SeederUtil()
    seeder.seed()

seed_db.delay()
