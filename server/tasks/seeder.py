from ..utils import SeederUtil

@shared_task
def seed_db():
    seeder = SeederUtil()
    seeder.seed()
