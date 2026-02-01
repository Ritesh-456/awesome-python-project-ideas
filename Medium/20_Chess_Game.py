class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'white'

    def initialize_board(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]

        # Place pawns
        for i in range(8):
            board[1][i] = 'P'  # White pawns
            board[6][i] = 'p'  # Black pawns

        # Place other pieces
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i, piece in enumerate(pieces):
            board[0][i] = piece  # White pieces
            board[7][i] = piece.lower()  # Black pieces

        return board

    def print_board(self):
        print("  a b c d e f g h")
        print(" +----------------")
        for i in range(7, -1, -1):
            print(f"{i+1}|", end="")
            for j in range(8):
                print(f"{self.board[i][j]}|", end="")
            print(f"{i+1}")
        print(" +----------------")
        print("  a b c d e f g h")

    def is_valid_move(self, start, end):
        start_row, start_col = self.algebraic_to_coords(start)
        end_row, end_col = self.algebraic_to_coords(end)

        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        piece = self.board[start_row][start_col]
        if piece == ' ':
            return False

        # Check if it's the correct player's turn
        if self.current_player == 'white' and piece.islower():
            return False
        if self.current_player == 'black' and piece.isupper():
            return False

        # Basic move validation (simplified)
        if piece.upper() == 'P':  # Pawn
            return self.is_valid_pawn_move(start_row, start_col, end_row, end_col, piece)
        elif piece.upper() == 'R':  # Rook
            return self.is_valid_rook_move(start_row, start_col, end_row, end_col)
        elif piece.upper() == 'N':  # Knight
            return self.is_valid_knight_move(start_row, start_col, end_row, end_col)
        elif piece.upper() == 'B':  # Bishop
            return self.is_valid_bishop_move(start_row, start_col, end_row, end_col)
        elif piece.upper() == 'Q':  # Queen
            return self.is_valid_queen_move(start_row, start_col, end_row, end_col)
        elif piece.upper() == 'K':  # King
            return self.is_valid_king_move(start_row, start_col, end_row, end_col)

        return False

    def is_valid_pawn_move(self, start_row, start_col, end_row, end_col, piece):
        direction = 1 if piece.isupper() else -1
        start_rank = 1 if piece.isupper() else 6

        # Forward move
        if start_col == end_col:
            if end_row == start_row + direction and self.board[end_row][end_col] == ' ':
                return True
            if start_row == start_rank and end_row == start_row + 2 * direction and self.board[end_row][end_col] == ' ' and self.board[start_row + direction][end_col] == ' ':
                return True
        # Capture
        elif abs(start_col - end_col) == 1 and end_row == start_row + direction:
            if self.board[end_row][end_col] != ' ':
                return True

        return False

    def is_valid_rook_move(self, start_row, start_col, end_row, end_col):
        if start_row != end_row and start_col != end_col:
            return False
        return self.is_path_clear(start_row, start_col, end_row, end_col)

    def is_valid_knight_move(self, start_row, start_col, end_row, end_col):
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    def is_valid_bishop_move(self, start_row, start_col, end_row, end_col):
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False
        return self.is_path_clear(start_row, start_col, end_row, end_col)

    def is_valid_queen_move(self, start_row, start_col, end_row, end_col):
        if not (start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col)):
            return False
        return self.is_path_clear(start_row, start_col, end_row, end_col)

    def is_valid_king_move(self, start_row, start_col, end_row, end_col):
        return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1

    def is_path_clear(self, start_row, start_col, end_row, end_col):
        row_step = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        col_step = 0 if start_col == end_col else (1 if end_col > start_col else -1)

        current_row, current_col = start_row + row_step, start_col + col_step
        while current_row != end_row or current_col != end_col:
            if self.board[current_row][current_col] != ' ':
                return False
            current_row += row_step
            current_col += col_step
        return True

    def make_move(self, start, end):
        if not self.is_valid_move(start, end):
            return False

        start_row, start_col = self.algebraic_to_coords(start)
        end_row, end_col = self.algebraic_to_coords(end)

        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = ' '

        self.current_player = 'black' if self.current_player == 'white' else 'white'
        return True

    def algebraic_to_coords(self, algebraic):
        col = ord(algebraic[0].lower()) - ord('a')
        row = int(algebraic[1]) - 1
        return row, col

def main():
    board = ChessBoard()

    while True:
        board.print_board()
        print(f"\n{board.current_player.capitalize()}'s turn")

        move = input("Enter move (e.g., e2e4) or 'quit' to exit: ").strip()

        if move.lower() == 'quit':
            break

        if len(move) != 4:
            print("Invalid move format. Use format like e2e4.")
            continue

        start, end = move[:2], move[2:]

        if board.make_move(start, end):
            print("Move made successfully.")
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()