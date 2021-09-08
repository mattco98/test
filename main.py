import sys
import json
from PyQt5.QtWidgets import *
from reevis.gui.node import NodeWidget
from reevis.nodes.node_graph import make_graph


JSON_PATH = "/home/matthew/code/reeva/demo/graph_foo.json"


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Reevis")

    with open(JSON_PATH) as f:
        graph = make_graph(json.load(f))

    for node in graph.nodes:
        NodeWidget(node, w)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
