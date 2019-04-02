from Puzzle import Puzzle
import os
import time


def print_game_board(puzzle):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("tries: " + str(puzzle.tries))
    for x in range(1, len(puzzle.board)):
        if (x % 3 == 1):
            print()
        print(puzzle.board[x], end="\t")
    print("\n\n\n\n\n\n")


def print_win_message(puzzle, star_time):
    end_time = time.time()
    print("\n\n\n\n\n")
    print("You won in " + str(puzzle.tries) + " tries!")
    print("time played: " + str(int(end_time - star_time)) + " seconds")


puzzle = Puzzle()
puzzle.board = [None, 1, None, 2, 3, 4, 5, 6, 7, 8]
star_time = time.time()

while not (puzzle.won()):
    print_game_board(puzzle)

    try:
        tile = int(input("Enter a number: "))
        puzzle.move(tile)
    except Exception as e:
        print(e)

print_win_message(puzzle, star_time)
