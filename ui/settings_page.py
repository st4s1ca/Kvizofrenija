
from ui.components import (
    create_panel, create_page,
    create_title, create_button
)


def create_settings_page():
    panel, layout = create_panel()

    title, subtitle = create_title(
        "PODEŠAVANJA",
        "Prilagodite kviz svojim potrebama"
    )

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addSpacing(30)

    back_button = create_button("← Nazad")
    layout.addWidget(back_button)

    page = create_page(panel)

    return page, back_button
