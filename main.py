from Puzzle import Puzzle

p = Puzzle()

p.board = [None, None, 1, 2, 3, 4, 5, 6, 7, 8]

p.move(2)
print(p.board)
p.move(5)
print(p.board)
