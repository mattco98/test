from typing import List, Dict, Any
import json
from .node import Node, NodeKind


class NodeGraph:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes


def make_graph(array: Any) -> NodeGraph:
    nodes: Dict[int, Node] = {}

    # Create nodes
    for item in array:
        kind_json = item["kind"]
        kind = NodeKind(kind_json["name"], kind_json["controlsIn"], kind_json["controlsOut"], kind_json["valuesIn"],
                        kind_json["providesValue"])
        node = Node(kind, item.get("constant"))
        nodes[int(item["id"])] = node

    # Link nodes
    for item in array:
        node = nodes[int(item["id"])]
        for input_id in item["inputs"]:
            node.inputs.append(nodes[int(input_id)])
        for output_id in item["outputs"]:
            node.outputs.append(nodes[int(output_id)])

    return NodeGraph(nodes.values())
