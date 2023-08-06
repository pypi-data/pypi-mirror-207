from .nodes import *
from .helpers import * # NOQA
from .visitor_procedure import * # NOQA
from .visitor_validation import * # NOQA

Procedure = NodeRunInOrder


def new_procedure(name: str) -> Procedure:
    return Procedure(name=name)
