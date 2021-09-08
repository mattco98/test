from typing import List, Any, Optional


class NodeKind:
    def __init__(self, name: str, controls_in: int, controls_out: int, values_in: int, provides_value: bool):
        self.name = name
        self.controls_in = controls_in
        self.controls_out = controls_out
        self.values_in = values_in
        self.provides_value = provides_value


class Node:
    def __init__(self, kind: NodeKind, constant: Optional[Any] = None):
        self.kind = kind
        self.constant = constant
        self.inputs: List[Node] = []
        self.outputs: List[Node] = []
