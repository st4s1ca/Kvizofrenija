from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


def create_main_menu():
    page = QWidget()
    layout = QVBoxLayout(page)

    title = QLabel("KVIZOFRENIJA")
    layout.addWidget(title)

    games_button = QPushButton("Igre")
    layout.addWidget(games_button)

    players_button = QPushButton("Igraci")
    layout.addWidget(players_button)

    settings_button = QPushButton("Podesavanja")
    layout.addWidget(settings_button)

    exit_button = QPushButton("Izadji")
    layout.addWidget(exit_button)

    return page, games_button, players_button, settings_button, exit_button