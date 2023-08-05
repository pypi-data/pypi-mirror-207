from __future__ import annotations

from typing import TypeVar, Optional

from gcscore.mod import *

T = TypeVar('T')

__all__ = ['HasIdentifier', 'HasCompaction', 'HasCommand', 'HasTargets', 'HasPayload', 'HasScriptType',
           'HasInstanceState', 'HasFunctionName', 'HasInstanceState', 'HasDurationSeconds', 'AcceptChildScript',
           'AcceptMerge', 'AcceptAnonymousChild', 'AcceptChildPause', 'AcceptChildWait', 'AcceptChildScriptTemplate',
           'AcceptChildStepFunction', 'AcceptChildRunInOrder', 'AcceptChildRunInParallel', 'NodeRunInOrder',
           'NodeRunInParallel', 'NodeWait', 'NodePause', 'NodeScript', 'NodeScriptTemplate', 'NodeStepFunction',
           'NodeChangeInstanceState']


# <editor-fold desc="Trait attributes">

class HasDurationSeconds:
    v_duration: int = 5

    def duration(self: T, duration_seconds: int) -> T:
        """
        Sets the duration in seconds for the node.
        :param duration_seconds: the duration in seconds
        :return: self
        """
        self.v_duration = duration_seconds
        return self


class HasIdentifier:
    v_identifier: str = ''

    def identifier(self: T, identifier_: str) -> T:
        """
        Sets the identifier in order to make it clearly identified in the resume tool.
        :param identifier_: the identifier
        :return: self
        """
        self.v_identifier = identifier_
        return self


class HasScriptType:
    v_script_type: str = 'shell'

    def shell(self: T) -> T:
        """
        Makes the node run a shell script/command.
        :return: self
        """
        self.v_script_type = 'shell'
        return self

    def powershell(self: T) -> T:
        """
        Make the node run a powershell script/command.
        :return: self
        """
        self.v_script_type = 'powershell'
        return self


class HasCommand:
    v_command: Optional[str] = None

    def command(self: T, cmd: str) -> T:
        """
        Sets the node command or script.
        :param cmd:
        :return:
        """
        self.v_command = cmd
        return self


class HasTargets:
    v_targets: list[dict]

    def __init__(self):
        self.v_targets = []

    def on_targets(self: T, targets: list[dict]) -> T:
        """
        Adds the targets to the node.
        :param targets: list of the targets
        :return: self
        """
        self.v_targets.extend(targets)
        return self


class HasCompaction:
    v_compaction: bool = False

    def compact(self: T) -> T:
        """
        Indicate that the content of the node (scripts...) should be compacted.
        :return: self
        """
        self.v_compaction = True
        return self


class HasFunctionName:
    v_function_name: str

    def function_name(self: T, name: str) -> T:
        """
        Sets the name of the function called by the node.
        :param name: function's name
        :return: self
        """
        self.v_function_name = name
        return self


class HasPayload:
    v_payload: dict

    def payload(self: T, payload: dict) -> T:
        """
        Sets the payload of the node.
        :param payload: the payload dictionary
        :return: self
        """
        self.v_payload = payload
        return self


class HasInstanceState:
    v_instance_state: str

    def power_on(self: T) -> T:
        """
        Mark the wanted state as "running"
        :return: self
        """
        self.v_instance_state = 'running'
        return self

    def power_off(self: T) -> T:
        """
        Mark the wanted state as "stopped"
        :return: self
        """
        self.v_instance_state = 'stopped'
        return self


# </editor-fold>

# <editor-fold desc="Traits for children">

class AcceptChildWait:
    def wait(self: HasChildren, name: str) -> NodeWait:
        """
        Waits a certain amount of seconds before continuing the execution.
        :param name: node's name
        :return: the child node wait
        """
        return add_child(self, NodeWait, name)


class AcceptChildPause:
    def pause(self: HasChildren, name: str) -> NodePause:
        """
        Waits for the user to resume the automation.
        :param name: node's name
        :return: the child node pause
        """
        return add_child(self, NodePause, name)


class AcceptChildRunInOrder:
    def run_in_order(self: HasChildren, name: str) -> NodeRunInOrder:
        """
        Starts a new in order procedure part.
        :param name: node's name
        :return: the child node
        """
        return add_child(self, NodeRunInOrder, name)


class AcceptChildRunInParallel:
    def run_in_parallel(self: HasChildren, name: str) -> NodeRunInParallel:
        """
        Starts a new parallelized nodes procedure part.
        :param name: node's name
        :return: the child node
        """
        return add_child(self, NodeRunInParallel, name)


class AcceptMerge:
    def merge(self: HasChildren, other: HasChildren) -> HasChildren:
        """
        Merges the other's children in its own (the order is kept).
        :param other: other node with children
        :return: self
        """
        self.v_children.extend(other.v_children)
        return self


class AcceptAnonymousChild:
    def child(self: HasChildren, other: HasName) -> HasChildren:
        """
        Adds the other as its own child.
        :param other: any kind of node
        :return: self
        """
        self.v_children.append(other)
        return self


class AcceptChildScript:
    def run_script(self: HasChildren, name: str) -> NodeScript:
        """
        Runs a script on the given servers.
        :param name: node's name
        :return: the child node
        """
        return add_child(self, NodeScript, name)


class AcceptChildScriptTemplate:
    def run_script_template(self: HasChildren, name: str) -> NodeScriptTemplate:
        """
        Renders the script command and runs it on the servers.
        :param name: node's name
        :return: the child node
        """
        return add_child(self, NodeScriptTemplate, name)


class AcceptChildStepFunction:
    def run_step_function(self: HasChildren, name: str) -> NodeStepFunction:
        """
        Run a step function.
        :param name: node's name
        :return: the child node
        """
        return add_child(self, NodeStepFunction, name)


# </editor-fold>

# <editor-fold desc="Nodes">
class _ComposedNode(
    HasName,
    HasDescription,
    HasChildren,
    AcceptAnonymousChild,
    AcceptMerge,
    AcceptChildWait,
    AcceptChildPause,
    AcceptChildRunInOrder,
    AcceptChildRunInParallel,
    AcceptChildScript,
    AcceptChildScriptTemplate,
    AcceptChildStepFunction
):
    def __init__(self, name: str):
        HasName.__init__(self, name)
        HasChildren.__init__(self)


class NodeRunInParallel(_ComposedNode):
    __visitor_method__ = 'visit_run_in_parallel'


class NodeRunInOrder(_ComposedNode):
    __visitor_method__ = 'visit_run_in_order'


class NodeWait(
    HasName,
    HasDescription,
    HasDurationSeconds
):
    __visitor_method__ = 'visit_wait'


class NodePause(
    HasName,
    HasDescription,
    HasIdentifier
):
    __visitor_method__ = 'visit_pause'


class NodeScript(
    HasName,
    HasDescription,
    HasScriptType,
    HasCommand,
    HasTargets,
    HasCompaction
):
    __visitor_method__ = 'visit_script'

    def __init__(self, name: str):
        HasName.__init__(self, name)
        HasTargets.__init__(self)


class NodeScriptTemplate(
    HasName,
    HasDescription,
    HasScriptType,
    HasCommand,
    HasTargets,
    HasCompaction
):
    __visitor_method__ = 'visit_script_template'

    def __init__(self, name: str):
        HasName.__init__(self, name)
        HasTargets.__init__(self)


class NodeStepFunction(
    HasName,
    HasDescription,
    HasFunctionName,
    HasPayload
):
    __visitor_method__ = 'visit_step_function'


class NodeChangeInstanceState(
    HasName,
    HasDescription,
    HasTargets,
    HasInstanceState
):
    __visitor_method__ = 'visit_change_instance_state'

    def __init__(self, name: str):
        HasName.__init__(self, name)
        HasTargets.__init__(self)
# </editor-fold>
