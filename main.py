import sys

from PySide6.QtWidgets import QApplication
from ui.main_window import create_main_window


def main():
    app = QApplication(sys.argv)

    window = create_main_window(app)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()