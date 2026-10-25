from PySide6.QtWidgets import QMainWindow, QStackedWidget

from ui.main_menu import create_main_menu
from ui.games_page import create_games_page
from ui.players_page import create_players_page
from ui.settings_page import create_settings_page
from ui.klikomanija_page import create_klikomanija_page

def create_main_window(app):
    window = QMainWindow()
    window.setWindowTitle("KVIZOFRENIJA")

    stack = QStackedWidget()
    window.setCentralWidget(stack)

    main_menu, games_button, players_button, settings_button, exit_button = create_main_menu()
    games_page, games_back_button, klikomanija_button = create_games_page()
    players_page, players_back_button = create_players_page()
    settings_page, settings_back_button = create_settings_page()
    klikomanija_page, klikomanija_back_button = create_klikomanija_page()

    stack.addWidget(main_menu)
    stack.addWidget(games_page)
    stack.addWidget(players_page)
    stack.addWidget(settings_page)
    stack.addWidget(klikomanija_page)
    games_button.clicked.connect(lambda: stack.setCurrentWidget(games_page))
    players_button.clicked.connect(lambda: stack.setCurrentWidget(players_page))
    settings_button.clicked.connect(lambda: stack.setCurrentWidget(settings_page))

    games_back_button.clicked.connect(lambda: stack.setCurrentWidget(main_menu))
    players_back_button.clicked.connect(lambda: stack.setCurrentWidget(main_menu))
    settings_back_button.clicked.connect(lambda: stack.setCurrentWidget(main_menu))

    def open_klikomanija():
        klikomanija_page.restart_game()
        stack.setCurrentWidget(klikomanija_page)

    klikomanija_button.clicked.connect(open_klikomanija)

    klikomanija_back_button.clicked.connect(lambda: stack.setCurrentWidget(games_page))
    klikomanija_page.quiz_finished.connect(lambda: stack.setCurrentWidget(games_page))
    exit_button.clicked.connect(app.quit)

    window.resize(1000, 500)

    return window