import dataclasses
from typing import Dict, List, Optional


class Message:
    """Encapsulates a message in NLC.

    An NLC Message can be arbitrarily long. It can be a user query, all of a document,
    or a piece of it.

    An NLC Message can be either a user message or a system generated message (output of
    LLM, or some other Operation). Each Message object tracks its trace back to the
    leaf inputs.
    """

    def __init__(self, content: str, source_name: Optional[str] = None):
        self.content = content
        self._trace: "MessageTrace" = Leaf(source_name)


class Operation:
    """Encapsulates an operation in NLC."""
    ...


class MessageTrace:
    """A trace of a message through the NLC system."""


@dataclasses.dataclass
class Leaf(MessageTrace):
    """A leaf node in the message trace."""
    source_name: Optional[str] = None


class OperationOutput(MessageTrace):
    """Traces back to the output of an Operation.

    Args:
        operation: The Operation that generated this output.
        input: The input to the Operation that generated this output.

    """

    def __init__(self, operation: Operation, args: List[Message], kwargs: Dict[str, Message]):
        self.operation = operation
        self.input = input
