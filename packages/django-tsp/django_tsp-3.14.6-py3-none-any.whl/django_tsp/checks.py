from collections.abc import Sequence
from typing import Any

from django.conf import settings
from django.core.checks import CheckMessage
from django.core.checks import Error

from django_tsp.conf import conf


def check_settings(**kwargs: Any) -> list[CheckMessage]:
    errors: list[CheckMessage] = []

    if not isinstance(conf.TSP_BROKER_URL, str):
        errors.append(
            Error("TSP_BROKER_URL should be a string.", id="django_tsp.E009")
        )

    if not isinstance(conf.TSP_HOOK_URL, str):
        errors.append(
            Error("TSP_HOOK_URL should be a string.", id="django_tsp.E009")
        )


    if not hasattr(settings, "TSP_HOOK_URL"):
        errors.append(
            Error(
                (
                    "The TSP_HOOK_URL setting has been removed"
                    + " - see django_tsp' CHANGELOG."
                ),
                id="django_tsp.E013",
            )
        )

    return errors

def is_sequence(thing: Any, type_or_types: type[Any] | tuple[type[Any], ...]) -> bool:
    return isinstance(thing, Sequence) and all(
        isinstance(x, type_or_types) for x in thing
    )