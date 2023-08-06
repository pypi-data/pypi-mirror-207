from django.core.management.base import BaseCommand
from tsp_wrapper import broker, tsp_solver_task
from django_tsp.services import prepare_broker

class Command(BaseCommand):
    help = 'This command will activate tsp_wrapper solver task'

    def handle(self, *args, **kwargs):
        prepare_broker()
        self.stdout.write(self.style.SUCCESS('Starting the Bridge.'))
        worker = broker.Worker(connection=broker.get_broker(), handler=tsp_solver_task, type="inbound")
        worker.run()