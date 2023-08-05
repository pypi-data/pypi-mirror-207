from django.conf import settings
from typing import Sequence
from django_tsp.defaults import default_names
from tsp_wrapper import BROKER_URL

class Settings:
    """
    Shadow Django's settings with a little logic
    """
    @property
    def TSP_BROKER_URL(self) -> str:
        return getattr(settings, "TSP_BROKER_URL", BROKER_URL)

    @property
    def TSP_HOOK_URL(self) -> str:
        return getattr(settings, "TSP_HOOK_URL", "http://localhost:8000/api/tsp/hook/")

conf = Settings()