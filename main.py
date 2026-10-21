import sys

from PySide6.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QLabel, QPushButton
)

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Kvizomanija")

    layout = QVBoxLayout()

    question = QLabel("Koji je glavni grad Francuske?")
    score = QLabel("Igrač 1: 0 bodova")

    button = QPushButton("Tačan odgovor +10")

    def add_score():
        score.setText("Igrač 1: 10 bodova")

    button.clicked.connect(add_score)

    layout.addWidget(question)
    layout.addWidget(score)
    layout.addWidget(button)

    window.setLayout(layout)
    window.resize(1000, 500)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
