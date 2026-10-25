
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QPushButton, QFrame, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor


def create_main_menu():
    page = QWidget()
    page.setObjectName("mainMenu")

    main_layout = QVBoxLayout(page)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Centralna kartica
    card = QFrame()
    card.setObjectName("menuCard")
    card.setFixedWidth(440)

    card_layout = QVBoxLayout(card)
    card_layout.setContentsMargins(40, 38, 40, 38)
    card_layout.setSpacing(14)

    # Naslov
    title = QLabel("KVIZOFRENIJA")
    title.setObjectName("menuTitle")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)

    subtitle = QLabel("By: Staša Stamenković and Ignjatije Ignjatović")
    subtitle.setObjectName("menuSubtitle")
    subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

    card_layout.addWidget(title)
    card_layout.addWidget(subtitle)
    card_layout.addSpacing(28)

    # Dugmad
    games_button = QPushButton("Igre")
    players_button = QPushButton("Igrači")
    settings_button = QPushButton("Podešavanja")
    exit_button = QPushButton("Izađi")

    buttons = [
        games_button,
        players_button,
        settings_button,
        exit_button
    ]

    for button in buttons:
        button.setMinimumHeight(54)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        card_layout.addWidget(button)

    games_button.setObjectName("primaryButton")
    exit_button.setObjectName("exitButton")

    # Senka kartice
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(35)
    shadow.setOffset(0, 10)
    shadow.setColor(QColor(0, 0, 0, 75))
    card.setGraphicsEffect(shadow)

    main_layout.addWidget(card)

    # Stil
    page.setStyleSheet("""
        QWidget#mainMenu {
            background-color: #101827;
        }

        QFrame#menuCard {
            background-color: #1B2638;
            border: 1px solid #303E53;
            border-radius: 18px;
        }

        QLabel#menuTitle {
            color: #F8FAFC;
            font-size: 30px;
            font-weight: 800;
            letter-spacing: 2px;
            background: transparent;
        }

        QLabel#menuSubtitle {
            color: #94A3B8;
            font-size: 14px;
            background: transparent;
        }

        QPushButton {
            background-color: #29374B;
            color: #F1F5F9;
            border: 1px solid #3B4B60;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            text-align: center;
        }

        QPushButton:hover {
            background-color: #354963;
            border: 1px solid #64748B;
        }

        QPushButton:pressed {
            background-color: #233247;
        }

        QPushButton#primaryButton {
            background-color: #2563EB;
            border: 1px solid #3B82F6;
            color: white;
        }

        QPushButton#primaryButton:hover {
            background-color: #3B82F6;
        }

        QPushButton#exitButton:hover {
            background-color: #713044;
            border: 1px solid #C25A75;
        }
    """)

    return (
        page,
        games_button,
        players_button,
        settings_button,
        exit_button
    )
