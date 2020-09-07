from random import randint


class Game:
    def __init__(self):
        self.cells = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.player = randint(0, 1)
        self.plays_left = 9

    def register_play(self, row: int, col: int):
        self.cells[row][col] = self.player + 4
        self.plays_left -= 1
        self.change_player_turn()

    def change_player_turn(self):
        self.player = not self.player

    def check_winner(self):
        win_arrange = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                       [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                       [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

        for possibility in win_arrange:
            possibility_sum = 0
            for position in possibility:
                possibility_sum += self.cells[position[0]][position[1]]
            if possibility_sum == 12:
                return 1
            elif possibility_sum == 15:
                return 2

        if self.plays_left:
            return -1
        else:
            return 0

    def clean_cells(self):
        self.plays_left = 9
        self.cells = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
