
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame,
    QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor


def create_games_page():
    page = QWidget()
    page.setObjectName("gamesPage")

    main_layout = QVBoxLayout(page)
    main_layout.setContentsMargins(30, 30, 30, 30)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Centralna kartica
    card = QFrame()
    card.setObjectName("gamesCard")
    card.setFixedWidth(540)

    card_layout = QVBoxLayout(card)
    card_layout.setContentsMargins(35, 35, 35, 35)
    card_layout.setSpacing(16)

    # Naslov
    title = QLabel("DOSTUPNE IGRE")
    title.setObjectName("gamesTitle")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)

    subtitle = QLabel("Izaberite igru koju želite da pokrenete")
    subtitle.setObjectName("gamesSubtitle")
    subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

    card_layout.addWidget(title)
    card_layout.addWidget(subtitle)
    card_layout.addSpacing(20)

    # Kartica za Klikomaniju
    game_card = QFrame()
    game_card.setObjectName("gameItem")

    game_layout = QHBoxLayout(game_card)
    game_layout.setContentsMargins(20, 20, 20, 20)
    game_layout.setSpacing(16)

    game_info = QVBoxLayout()
    game_info.setSpacing(6)

    game_name = QLabel("KLIKOMANIJA")
    game_name.setObjectName("gameName")

    game_description = QLabel(
        "Ko prvi pritisne taster, dobija priliku da odgovori."
    )
    game_description.setObjectName("gameDescription")
    game_description.setWordWrap(True)

    game_info.addWidget(game_name)
    game_info.addWidget(game_description)

    buzzer_button = QPushButton("Pokreni")
    buzzer_button.setObjectName("playButton")
    buzzer_button.setFixedSize(115, 45)
    buzzer_button.setCursor(Qt.CursorShape.PointingHandCursor)

    game_layout.addLayout(game_info, 1)
    game_layout.addWidget(buzzer_button)

    card_layout.addWidget(game_card)
    card_layout.addSpacing(20)

    # Dugme za povratak
    back_button = QPushButton("← Nazad na glavni meni")
    back_button.setObjectName("backButton")
    back_button.setMinimumHeight(48)
    back_button.setCursor(Qt.CursorShape.PointingHandCursor)

    card_layout.addWidget(back_button)

    # Senka
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(35)
    shadow.setOffset(0, 10)
    shadow.setColor(QColor(0, 0, 0, 75))
    card.setGraphicsEffect(shadow)

    main_layout.addWidget(card)

    # Stilovi
    page.setStyleSheet("""
        QWidget#gamesPage {
            background-color: #101827;
        }

        QFrame#gamesCard {
            background-color: #1B2638;
            border: 1px solid #303E53;
            border-radius: 18px;
        }

        QLabel#gamesTitle {
            color: #F8FAFC;
            font-size: 29px;
            font-weight: 800;
            background: transparent;
        }

        QLabel#gamesSubtitle {
            color: #94A3B8;
            font-size: 14px;
            background: transparent;
        }

        QFrame#gameItem {
            background-color: #25354B;
            border: 1px solid #3B4B60;
            border-radius: 12px;
        }

        QLabel#gameName {
            color: #FFFFFF;
            font-size: 19px;
            font-weight: 700;
            background: transparent;
            border: none;
        }

        QLabel#gameDescription {
            color: #A8B7CA;
            font-size: 13px;
            background: transparent;
            border: none;
        }

        QPushButton#playButton {
            background-color: #2563EB;
            color: white;
            border: 1px solid #3B82F6;
            border-radius: 9px;
            font-size: 14px;
            font-weight: 600;
        }

        QPushButton#playButton:hover {
            background-color: #3B82F6;
        }

        QPushButton#playButton:pressed {
            background-color: #1D4ED8;
        }

        QPushButton#backButton {
            background-color: #29374B;
            color: #F1F5F9;
            border: 1px solid #3B4B60;
            border-radius: 10px;
            font-size: 14px;
        }

        QPushButton#backButton:hover {
            background-color: #354963;
            border: 1px solid #64748B;
        }
    """)

    return page, back_button, buzzer_button
