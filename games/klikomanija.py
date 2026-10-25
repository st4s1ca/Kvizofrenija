
class Klikomanija:
    def __init__(self, players, questions, points=10):
        self.players = [
            {"name": name, "score": 0}
            for name in players
        ]

        self.questions = questions
        self.points = points
        self.question_index = 0

        self.reset_question()

    def reset_question(self):
        self.queue = []
        self.attempted = set()
        self.current_player = None
        self.winner = None
        self.finished = False

    def current_question(self):
        return self.questions[self.question_index]

    def buzz(self, player_id):
        if self.finished:
            return False

        if player_id in self.attempted:
            return False

        if player_id == self.current_player:
            return False

        if player_id in self.queue:
            return False

        self.queue.append(player_id)

        if self.current_player is None:
            self.next_player()

        return True

    def next_player(self):
        if self.queue:
            self.current_player = self.queue.pop(0)
        else:
            self.current_player = None

        return self.current_player

    def answer_correct(self):
        if self.current_player is None or self.finished:
            return

        self.players[self.current_player]["score"] += self.points
        self.winner = self.current_player
        self.finished = True

    def answer_wrong(self):
        if self.current_player is None or self.finished:
            return

        self.attempted.add(self.current_player)
        self.current_player = None
        self.next_player()

    def reveal_answer(self):
        self.finished = True
        self.current_player = None

    def next_question(self):
        if not self.finished:
            return False

        if self.question_index + 1 >= len(self.questions):
            return False

        self.question_index += 1
        self.reset_question()
        return True
