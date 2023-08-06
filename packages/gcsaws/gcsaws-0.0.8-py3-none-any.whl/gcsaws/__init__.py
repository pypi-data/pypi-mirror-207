from .nodes import *
from .helpers import *
from .visitor_procedure import *

Procedure = NodeRunInOrder


def new_procedure(name: str) -> Procedure:
    return Procedure(name=name)
