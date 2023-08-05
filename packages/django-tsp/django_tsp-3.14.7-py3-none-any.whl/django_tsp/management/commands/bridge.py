from django.core.management.base import BaseCommand
from tsp_wrapper import broker, setup, tsp_solver_task


class Command(BaseCommand):
    help = 'Show all available styles'

    def handle(self, *args, **kwargs):
        setup()
        self.stdout.write(self.style.SUCCESS('Starting the Bridge.'))
        worker = broker.Worker(connection=broker.get_broker(), handler=tsp_solver_task, type="inbound")
        worker.run()