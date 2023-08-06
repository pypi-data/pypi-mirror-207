import re
from typing import Union

from gcscore.mod import Visitor
from gcscore.mod.validation import VisitorStateValidation, validation_error_value, validate_string

from gcsaws.nodes import *

__all__ = ['setup_validation_visitor']


def setup_validation_visitor(visitor: Visitor):
    visitor.register('visit_wait', _visit_wait)
    visitor.register('visit_pause', _visit_pause)
    visitor.register('visit_script', _visit_script)
    visitor.register('visit_script_template', _visit_script)
    visitor.register('visit_step_function', _visit_step_function)
    visitor.register('visit_change_instance_state', _visit_change_instance_state)
    visitor.register('visit_run_in_order', _visit_composed_node)
    visitor.register('visit_run_in_parallel', _visit_composed_node)


PATTERN_NAME = re.compile(r'^[a-zA-Z0-9_\-]+$')


def _validate_targets(state: VisitorStateValidation, node: HasTargets):
    if not node.gcsaws_targets_initialized:
        validation_error_value(state, 'targets', None, 'on_targets(...) must be called')


ComposedNode = Union[NodeRunInOrder, NodeRunInParallel]


def _visit_composed_node(visitor: Visitor, node: ComposedNode, state: VisitorStateValidation):
    state = state.concat(node.gcscore_name)
    validate_string(state, 'name', node.gcscore_name, PATTERN_NAME)
    for child in node.gcscore_children:
        visitor.visit(child, state)


def _visit_wait(_visitor: Visitor, node: NodeWait, state: VisitorStateValidation):
    state = state.concat(node.gcscore_name)
    validate_string(state, 'name', node.gcscore_name, PATTERN_NAME)
    if node.gcsaws_duration <= 0:
        validation_error_value(state, 'duration', node.gcsaws_duration, 'Must be greater than 0')


def _visit_pause(_visitor: Visitor, node: NodePause, state: VisitorStateValidation):
    state = state.concat(node.gcscore_name)
    validate_string(state, 'name', node.gcscore_name, PATTERN_NAME)


def _visit_script(visitor: Visitor, node: NodeScript, state: VisitorStateValidation):
    state = state.concat(node.gcscore_name)
    validate_string(state, 'name', node.gcscore_name, PATTERN_NAME)
    _validate_targets(state, node)
    if node.gcsaws_script_type is None:
        validation_error_value(state, 'script_type', None, 'shell() or powershell() must be called')
    if node.gcsaws_command is None:
        validation_error_value(state, 'command', None, 'command("your command") must be called')


def _visit_step_function(_visitor: Visitor, node: NodeStepFunction, state: VisitorStateValidation):
    state = state.concat(node.gcscore_name)
    validate_string(state, 'name', node.gcscore_name, PATTERN_NAME)
    if node.gcsaws_function_name is None:
        validation_error_value(state, 'stepfuntion', None, 'stepfunction("sf-name") must be called')
    if node.gcsaws_payload is None:
        validation_error_value(state, 'payload', None, 'payload({"key": "value") must be called')


def _visit_change_instance_state(_visitor: Visitor, node: NodeChangeInstanceState, state: VisitorStateValidation):
    state = state.concat(node.gcscore_name)
    validate_string(state, 'name', node.gcscore_name, PATTERN_NAME)
    _validate_targets(state, node)
    if node.gcsaws_instance_state is None:
        validation_error_value(state, 'instance_state', node.gcsaws_instance_state, 'power_on() or power_off() must be called')
