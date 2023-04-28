from Tile import Tile


class Agent:
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    def __init__(self, game, color, max_depth):
        self.game = game
        self.color = color
        self.max_depth = max_depth

    def do_min_max(self, current_board):
        # alpha , beta algorithm
        move, value = self.max_move_value(current_board, self.color, 0)

        return move

    def max_move_value(self, current_board, current_color, depth, Alph=float('-inf'), Beta=float('+inf')):

        # this is our turn and if there is no move for us, we have lost the game
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, -1000)

        # estimate the evaluate func score in maximum depth
        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)

        # if we haven't lost we will search more
        all_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best_move = None

        for move in all_moves:
            careless_move, move_val = self.min_move_value(current_board.next_board(current_color, move),
                                                          self.game.opponent
                                                          , depth + 1, Alph, Beta)
            # tree pruning
            if move_val >= Beta:
                return move, move_val

            if Alph < move_val:
                best_move = move
                Alph = move_val

        return best_move, Alph

    def min_move_value(self, current_board, current_color, depth, Alph, Beta):
        return None, None
