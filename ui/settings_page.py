from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


def create_settings_page():
    page = QWidget()
    layout = QVBoxLayout(page)

    title = QLabel("PODESAVANJA")
    layout.addWidget(title)

    back_button = QPushButton("Nazad")
    layout.addWidget(back_button)

    return page, back_button