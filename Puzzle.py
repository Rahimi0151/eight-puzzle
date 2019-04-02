import random
import Helpers


class Puzzle:

    def __init__(self):
        self.board = Helpers.shuffle([None, 1, 2, 3, 4, 5, 6, 7, 8], 10)
        self.board = [None] + self.board
        self.tries = 0
        self.init_swapable()
        self.init_neigbours()

    def init_swapable(self):
        self.swapable = [
            (1, 2), (2, 1), (2, 3), (3, 2), (4, 5), (5, 4), (5, 6), (6, 5),
            (7, 8), (8, 7), (8, 9), (9, 8), (1, 4), (4, 1), (4, 7), (7, 4),
            (2, 5), (5, 2), (5, 8), (8, 5), (3, 6), (6, 3), (6, 9), (9, 6)
        ]

    def init_neigbours(self):
        self.neighbours = {
            1: [2, 4],
            2: [1, 3, 5],
            3: [2, 6],
            4: [1, 5, 7],
            5: [2, 4, 6, 8],
            6: [3, 5, 9],
            7: [4, 8],
            8: [7, 5, 9],
            9: [8, 6]
        }

    def are_neigbours(self, first_element, second_element):
        return (first_element in self.neighbours[second_element]
                or second_element in self.neighbours[first_element])

    def are_not_neigbours(self, first_element, second_element):
        return not (first_element in self.neighbours[second_element]
                    or second_element in self.neighbours[first_element])

    def is_swapable(self, first_position, second_position):
        return (first_position, second_position) in self.swapable

    def do_the_swapping(self, first_element, second_element):
        temp = self.board[first_element]
        self.board[first_element] = self.board[second_element]
        self.board[second_element] = temp

    def swap(self, first_element, second_element):
        if (first_element, second_element) in self.swapable:
            self.do_the_swapping(first_element, second_element)

    def won(self):
        return self.board == [None, None, 1, 2, 3, 4, 5, 6, 7, 8]

    def increment_tries(self):
        self.tries += 1

    def move(self, tile):
        for x in self.neighbours[tile]:
            if self.board[x] == None:
                self.swap(x, tile)
                self.increment_tries()
                return
        raise Exception("Invalid move: there is no empty space to move this tile to")
