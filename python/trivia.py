from random import randrange

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append(f'Pop Question {i}')
            self.science_questions.append(f'Science Question {i}')
            self.sports_questions.append(f'Sports Question {i}')
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return f'Rock Question {index}'

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + ' was added')
        print(f'They are player number {len(self.players)}')

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def rolling(self):
        roll = randrange(6) + 1

        print(f'{self.players[self.current_player]} is the current player')
        print(f'They have rolled a {roll}')

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print(f'{self.players[self.current_player]} is getting out of the penalty box')
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(f'{self.players[self.current_player]}\'s new location is ',
                      f'{self.places[self.current_player]}')

                print(f'The category is {self._current_category}')
                self._ask_question()
            else:
                print(f'{self.players[self.current_player]} is not getting out of the penalty box')
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(f'{self.players[self.current_player]}\'s new location is ',
                  f'{self.places[self.current_player]}')

            print(f'The category is {self._current_category}')
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop':
            print(self.pop_questions.pop(0))
        if self._current_category == 'Science':
            print(self.science_questions.pop(0))
        if self._current_category == 'Sports':
            print(self.sports_questions.pop(0))
        if self._current_category == 'Rock':
            print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0:
            return 'Pop'
        if self.places[self.current_player] == 4:
            return 'Pop'
        if self.places[self.current_player] == 8:
            return 'Pop'
        if self.places[self.current_player] == 1:
            return 'Science'
        if self.places[self.current_player] == 5:
            return 'Science'
        if self.places[self.current_player] == 9:
            return 'Science'
        if self.places[self.current_player] == 2:
            return 'Sports'
        if self.places[self.current_player] == 6:
            return 'Sports'
        if self.places[self.current_player] == 10:
            return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                self.in_penalty_box[self.current_player] = False
                print('Answer was correct!!!!')

                self.purses[self.current_player] += 1
                print(f'{self.players[self.current_player]} now has ',
                      f'{self.purses[self.current_player]} Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True
        else:
            print('Answer was correct!!!!')

            self.purses[self.current_player] += 1
            print(f'{self.players[self.current_player]} now has '
                  f'{self.purses[self.current_player]} Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Question was incorrectly answered')
                print(self.players[self.current_player] + ' was sent to the penalty box')
                self.in_penalty_box[self.current_player] = True

                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True
        else:
            print('Question was incorrectly answered')
            print(self.players[self.current_player] + ' was sent to the penalty box')
            self.in_penalty_box[self.current_player] = True

            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0
            return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.rolling()

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
