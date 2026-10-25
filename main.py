
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from ui.main_window import create_main_window


def main():
    app = QApplication(sys.argv)

    styles_path = Path(__file__).resolve().parent / "styles.qss"

    with open(styles_path, "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    window = create_main_window(app)
    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
