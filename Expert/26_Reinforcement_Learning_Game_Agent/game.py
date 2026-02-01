import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for X, -1 for O
        self.winner = None
        self.game_over = False

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.winner = None
        self.game_over = False
        return self.get_state()

    def get_state(self):
        return self.board.flatten()

    def get_available_actions(self):
        return [i for i in range(9) if self.board[i//3, i%3] == 0]

    def make_move(self, action):
        if self.game_over:
            return self.get_state(), 0, True

        row, col = action // 3, action % 3
        if self.board[row, col] != 0:
            return self.get_state(), -10, True  # Invalid move penalty

        self.board[row, col] = self.current_player

        if self.check_winner():
            self.winner = self.current_player
            self.game_over = True
            return self.get_state(), 1, True
        elif len(self.get_available_actions()) == 0:
            self.game_over = True
            return self.get_state(), 0.5, True  # Draw
        else:
            self.current_player = -self.current_player
            return self.get_state(), 0, False

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3 or abs(sum(self.board[:, i])) == 3:
                return True
        if abs(self.board[0, 0] + self.board[1, 1] + self.board[2, 2]) == 3:
            return True
        if abs(self.board[0, 2] + self.board[1, 1] + self.board[2, 0]) == 3:
            return True
        return False

    def print_board(self):
        symbols = {0: ' ', 1: 'X', -1: 'O'}
        for i in range(3):
            print(' | '.join(symbols[self.board[i, j]] for j in range(3)))
            if i < 2:
                print('---------')

    def get_human_move(self):
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if move in self.get_available_actions():
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 0-8.")