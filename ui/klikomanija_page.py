
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

from ui.components import (
    create_panel, create_page,
    create_title, create_button
)


def create_klikomanija_page():
    panel, layout = create_panel(650)

    title, subtitle = create_title(
        "KLIKOMANIJA",
        "Ko prvi pritisne?"
    )

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addSpacing(30)

    question = QLabel("Ovde će se prikazivati pitanje")
    question.setAlignment(Qt.AlignmentFlag.AlignCenter)
    question.setWordWrap(True)
    layout.addWidget(question)

    layout.addSpacing(30)

    back_button = create_button("← Nazad na igre")
    layout.addWidget(back_button)

    page = create_page(panel)

    return page, back_button
