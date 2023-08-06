from channels.layers import get_channel_layer
from tsp_wrapper import broker, INBOUND_QUEUE, setup
from asgiref.sync import async_to_sync
import secrets 
from kombu import Connection
from django_tsp.conf import conf


channel_layer = get_channel_layer()

def notify_event(event:dict) -> None:
    """
    call sockets
    """
    async_to_sync(channel_layer.group_send)('tsp', {'type': 'add_event', 'event': event})


def publish_tsp_sloution(data):
    data["type"] = "answer"
    notify_event(data)

def create_tsp_problem(data):
    data["type"] = "question"
    data["id"] = secrets.token_hex(5)  # TODO: store the task ids 
    notify_event(data)
    broker.send_data(connection=broker.get_broker(), message=data, routing_key=INBOUND_QUEUE)


def prepare_broker():
    """
        changing the broker url with settings.py variables
        and connecting to the broker
        and setting up the middlewares
    """
    broker.set_broker(Connection(conf.TSP_BROKER_URL))
    setup()