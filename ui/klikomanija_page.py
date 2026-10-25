
import json
from pathlib import Path

from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame,
    QDialog
)

from games.klikomanija import Klikomanija


class KlikomanijaPage(QWidget):
    quiz_finished = Signal()
    def __init__(self):
        super().__init__()

        self.setObjectName("klikomanijaPage")

        # Privremeni igraci
        players = ["Marko", "Ana", "Nikola"]

        # Ucitavanje pitanja
        path = Path(__file__).resolve().parents[1]
        path = path / "data" / "questions.json"

        with open(path, encoding="utf-8") as file:
            questions = json.load(file)

        if not questions:
            raise ValueError("JSON ne sadrzi pitanja.")

        for question in questions:
            if not all(
                isinstance(question.get(key), str)
                and question[key].strip()
                for key in ("question", "answer")
            ):
                raise ValueError("Pitanje mora imati question i answer.")

        self.game = Klikomanija(players, questions)

        self.setup_ui()
        self.setup_dialog()
        self.setup_shortcuts()
        self.refresh()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(35, 30, 35, 30)
        layout.setSpacing(20)

        # Zaglavlje
        header = QHBoxLayout()

        title = QLabel("KLIKOMANIJA")
        title.setObjectName("pageTitle")

        self.round_label = QLabel()
        self.round_label.setObjectName("subtitle")

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.round_label)

        layout.addLayout(header)

        # Pitanje
        question_card = QFrame()
        question_card.setObjectName("panel")

        question_layout = QVBoxLayout(question_card)
        question_layout.setContentsMargins(30, 35, 30, 35)

        self.question_label = QLabel()
        self.question_label.setObjectName("questionText")
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_label.setWordWrap(True)

        self.answer_label = QLabel()
        self.answer_label.setObjectName("answerText")
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.answer_label.setWordWrap(True)

        question_layout.addWidget(self.question_label)
        question_layout.addWidget(self.answer_label)

        layout.addWidget(question_card)

        # Kartice igraca
        players_layout = QHBoxLayout()
        players_layout.setSpacing(16)

        self.player_cards = []
        self.player_scores = []
        self.player_statuses = []


        for index, player in enumerate(self.game.players):
            card = QFrame()
            card.setObjectName("playerCard")

            card_layout = QVBoxLayout(card)
            card_layout.setSpacing(12)

            avatar = QLabel(player["name"][0].upper())
            avatar.setObjectName("playerAvatar")
            avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)

            name = QLabel(player["name"])
            name.setObjectName("cardTitle")
            name.setAlignment(Qt.AlignmentFlag.AlignCenter)

            score = QLabel()
            score.setAlignment(Qt.AlignmentFlag.AlignCenter)

            status = QLabel()
            status.setAlignment(Qt.AlignmentFlag.AlignCenter)

            for element in (avatar, name, score, status):
                card_layout.addWidget(element)

            players_layout.addWidget(card)

            self.player_cards.append(card)
            self.player_scores.append(score)
            self.player_statuses.append(status)
        layout.addLayout(players_layout)

        # Kontrole voditelja
        self.current_label = QLabel()
        self.current_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.current_label)

        self.queue_label = QLabel()
        self.queue_label.setObjectName("subtitle")
        self.queue_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.queue_label)

        controls = QHBoxLayout()

        self.judge_button = QPushButton("Oceni odgovor")
        self.judge_button.clicked.connect(self.show_judge_dialog)

        self.reveal_button = QPushButton("Otkrij odgovor")
        self.reveal_button.clicked.connect(self.reveal_answer)

        self.next_button = QPushButton("Sledeće pitanje")
        self.next_button.setObjectName("primaryButton")
        self.next_button.clicked.connect(self.next_question)

        controls.addWidget(self.judge_button)
        controls.addWidget(self.reveal_button)
        controls.addWidget(self.next_button)

        layout.addLayout(controls)

        layout.addStretch()

        self.back_button = QPushButton("← Nazad na igre")
        layout.addWidget(self.back_button)

    def setup_dialog(self):
        # Nemodalni dijalog: ostali igraci i dalje mogu da se prijave
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Ocena odgovora")
        self.dialog.setModal(False)
        self.dialog.setMinimumWidth(350)

        dialog_layout = QVBoxLayout(self.dialog)

        self.dialog_label = QLabel()
        self.dialog_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(self.dialog_label)

        buttons = QHBoxLayout()

        correct_button = QPushButton("Tačno")
        correct_button.setObjectName("correctButton")
        correct_button.clicked.connect(lambda: self.judge(True))

        wrong_button = QPushButton("Netačno")
        wrong_button.setObjectName("wrongButton")
        wrong_button.clicked.connect(lambda: self.judge(False))

        buttons.addWidget(correct_button)
        buttons.addWidget(wrong_button)

        dialog_layout.addLayout(buttons)

    def setup_shortcuts(self):
        self.shortcuts = []

        for index in range(len(self.game.players)):
            shortcut = QShortcut(QKeySequence(str(index + 1)), self)
            shortcut.setContext(Qt.ShortcutContext.ApplicationShortcut)

            shortcut.activated.connect(
                lambda i=index: self.register_buzz(i)
            )

            self.shortcuts.append(shortcut)

    def register_buzz(self, player_id):
        accepted = self.game.buzz(player_id)

        if not accepted:
            return

        self.refresh()

        if self.game.current_player == player_id:
            self.show_judge_dialog()

    def show_judge_dialog(self):
        player_id = self.game.current_player

        if player_id is None or self.game.finished:
            return

        name = self.game.players[player_id]["name"]
        self.dialog_label.setText(f"Da li je {name} tačno odgovorio?")

        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()

    def judge(self, correct):
        self.dialog.hide()

        if correct:
            self.game.answer_correct()
        else:
            self.game.answer_wrong()

        self.refresh()

        if not correct and self.game.current_player is not None:
            self.show_judge_dialog()

    def reveal_answer(self):
        self.game.reveal_answer()
        self.dialog.hide()
        self.refresh()

    def next_question(self):
        if not self.game.finished:
            return

        # Poslednje pitanje je zavrseno
        if self.game.question_index == len(self.game.questions) - 1:
            self.dialog.hide()
            self.quiz_finished.emit()
            return

        # Postoji sledece pitanje
        if self.game.next_question():
            self.dialog.hide()
            self.refresh()
    def refresh(self):
        game = self.game

        self.round_label.setText(
            f"Pitanje {game.question_index + 1} / {len(game.questions)}"
        )

        question = game.current_question()
        self.question_label.setText(question["question"])

        self.answer_label.setText(
            f'ODGOVOR ZA VODITELJA: {question["answer"]}'
        )
        self.answer_label.setVisible(True)
        queue_names = [
            game.players[i]["name"] for i in game.queue
        ]

        self.queue_label.setText(
            "Red čekanja: " + (
                " → ".join(queue_names) if queue_names else "Prazan"
            )
        )

        if game.finished:
            if game.winner is not None:
                name = game.players[game.winner]["name"]
                self.current_label.setText(f"TAČNO! {name} osvaja bodove.")
            else:
                self.current_label.setText("Pitanje je završeno.")
        elif game.current_player is not None:
            name = game.players[game.current_player]["name"]
            self.current_label.setText(f"Odgovara: {name}")
        else:
            self.current_label.setText("Čekamo prijavljivanje igrača...")

        for i, player in enumerate(game.players):
            self.player_scores[i].setText(
                f'{player["score"]} bodova'
            )

            if game.winner == i:
                state, status = "correct", "TAČNO"

            elif i in game.attempted:
                state, status = "wrong", "NETAČNO"

            elif game.current_player == i:
                state, status = "active", "1. NA REDU"

            elif i in game.queue:
                position = game.queue.index(i) + 2
                state, status = "queued", f"{position}. U REDU"

            else:
                state, status = "idle", "SPREMAN"

            card = self.player_cards[i]
            card.setProperty("state", state)
            card.style().unpolish(card)
            card.style().polish(card)

            self.player_statuses[i].setText(status)

        self.judge_button.setEnabled(
            not game.finished and game.current_player is not None
        )
        self.reveal_button.setEnabled(not game.finished)
        self.next_button.setEnabled(game.finished)

        if game.finished:
            self.next_button.setText(
                "Završi kviz"
                if game.question_index == len(game.questions) - 1
                else "Sledeće pitanje"
            )
        else:
            self.next_button.setText("Sledeće pitanje")

    def hideEvent(self, event):
        if hasattr(self, "dialog"):
            self.dialog.hide()
        super().hideEvent(event)

    def restart_game(self):
        self.dialog.hide()

        self.game = Klikomanija(
            [player["name"] for player in self.game.players],
            self.game.questions,
            self.game.points
        )

        self.refresh()


def create_klikomanija_page():
    page = KlikomanijaPage()
    return page, page.back_button
