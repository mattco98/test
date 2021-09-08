from random import randint
from typing import Optional

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPaintEvent, QPainter, QPen, QFont
from PyQt5.QtWidgets import QWidget
from ..nodes.node import Node


class NodeWidget(QWidget):
    def __init__(self, node: Node, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.node = node
        self.x: Optional[int] = None
        self.y: Optional[int] = None

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.BLACK, 5, Qt.SolidLine))

        painter.setFont(painter.font().setPixelSize(24))
        text_rect = painter.fontMetrics().boundingRect(self.node.name)

        if not self.x:
            self.x = randint(0, self.window().width())
            self.y = randint(0, self.window().height())

        text_rect.setX(self.x)
        text_rect.setY(self.y)

        draw_rect = QRect(text_rect)
        draw_rect.setLeft(draw_rect.left() - 20)
        draw_rect.setRight(draw_rect.right() + 20)
        draw_rect.setTop(draw_rect.top() - 20)
        draw_rect.setBottom(draw_rect.bottom() + 20)

        painter.drawRect(draw_rect)
        painter.drawText(text_rect, self.node.name)
