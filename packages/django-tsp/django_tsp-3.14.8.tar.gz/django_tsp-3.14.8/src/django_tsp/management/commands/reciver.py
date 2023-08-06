from django.core.management.base import BaseCommand
from tsp_wrapper import broker, OUTBOUND_QUEUE
from django_tsp.services import prepare_broker
import requests
from django_tsp.conf import conf


class Command(BaseCommand):
    help = 'Consume the tsp sloution and bordcast it to the /ws/tsp socket'

    def handle(self, *args, **kwargs):
        prepare_broker()
        self.stdout.write(self.style.SUCCESS('Starting the Reciver.'))
        worker = broker.Worker(connection=broker.get_broker(), handler=self.socket_tsp, type=OUTBOUND_QUEUE)
        worker.run()

    def socket_tsp(self, res):
        """
        our costume task for notifing the sloution to the web socket client
        """
        response = requests.post(conf.TSP_HOOK_URL, json = res)
        self.stdout.write(self.style.NOTICE(f'socket_tsp task response --> {response}'))