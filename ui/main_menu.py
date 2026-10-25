
from ui.components import (
    create_panel, create_page,
    create_title, create_button
)


def create_main_menu():
    panel, layout = create_panel(440)

    title, subtitle = create_title(
        "KVIZOFRENIJA",
        "Kontrolni panel voditelja"
    )

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addSpacing(24)

    games_button = create_button("Igre", "primaryButton")
    players_button = create_button("Igrači")
    settings_button = create_button("Podešavanja")
    exit_button = create_button("Izađi", "exitButton")

    for button in (
        games_button,
        players_button,
        settings_button,
        exit_button
    ):
        layout.addWidget(button)

    page = create_page(panel)

    return page, games_button, players_button, settings_button, exit_button
