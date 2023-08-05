from channels.layers import get_channel_layer
from tsp_wrapper import broker, INBOUND_QUEUE
from asgiref.sync import async_to_sync
import secrets 


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
    data["id"] = secrets.token_hex(5)
    notify_event(data)
    broker.send_data(connection=broker.get_broker(), message=data, routing_key=INBOUND_QUEUE)
