
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QPushButton, QFrame, QGraphicsDropShadowEffect
)


def create_panel(width=540):
    panel = QFrame()
    panel.setObjectName("panel")
    panel.setFixedWidth(width)

    layout = QVBoxLayout(panel)
    layout.setContentsMargins(35, 35, 35, 35)
    layout.setSpacing(16)

    shadow = QGraphicsDropShadowEffect(panel)
    shadow.setBlurRadius(35)
    shadow.setOffset(0, 10)
    shadow.setColor(QColor(0, 0, 0, 75))
    panel.setGraphicsEffect(shadow)

    return panel, layout


def create_page(panel):
    page = QWidget()
    layout = QVBoxLayout(page)
    layout.setContentsMargins(24, 24, 24, 24)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(panel)

    return page


def create_title(text, subtitle=None):
    title = QLabel(text)
    title.setObjectName("pageTitle")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)

    if subtitle is None:
        return title

    description = QLabel(subtitle)
    description.setObjectName("subtitle")
    description.setAlignment(Qt.AlignmentFlag.AlignCenter)
    description.setWordWrap(True)

    return title, description


def create_button(text, style=None):
    button = QPushButton(text)
    button.setCursor(Qt.CursorShape.PointingHandCursor)

    if style:
        button.setObjectName(style)

    return button
