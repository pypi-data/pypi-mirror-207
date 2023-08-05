from django.core.management.base import BaseCommand
from tsp_wrapper import broker, setup, OUTBOUND_QUEUE
import requests
from django_tsp.conf import conf


def socket_tsp(res):
    requests.post(conf.TSP_HOOK_URL, json = res)

class Command(BaseCommand):
    help = 'Show all available styles'

    def handle(self, *args, **kwargs):
        setup()
        self.stdout.write(self.style.SUCCESS('Starting the Reciver.'))
        worker = broker.Worker(connection=broker.get_broker(), handler=self.socket_tsp, type=OUTBOUND_QUEUE)
        worker.run()

    def socket_tsp(self, res):
        response = requests.post(conf.TSP_HOOK_URL, json = res)
        self.stdout.write(self.style.NOTICE(f'{response}'))