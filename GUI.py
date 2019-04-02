import tkinter
from Puzzle import Puzzle
from tkinter import messagebox


class Game:
    def __init__(self, master):

        self.master = master
        self.app_frame = tkinter.Frame(self.master, bg='white')
        self.app_frame.pack(fill=tkinter.BOTH, expand=True)

        self.create_game()
        self.build_grid()
        self.update_board()

    def create_game(self):
        self.puzzle = Puzzle()
        self.create_select_mover()

    def update_board(self):
        self.push_button = [None for i in range(10)]
        for i in range(1, len(self.puzzle.board)):
            x = int((i - 1) / 3)
            y = int((i - 1) % 3)
            self.push_button[i] = tkinter.Button(self.app_frame, text=self.puzzle.board[i],
                                                 command=self.select_mover[i])
            self.push_button[i].grid(row=x, column=y, sticky='news')
        self.check_for_victory()

    def check_for_victory(self):
        if self.puzzle.won():
            messagebox.showinfo('GAME OVER!', 'Player1 Won!')
            self.create_game()
            self.update_board()

    def build_grid(self):
        self.app_frame.columnconfigure(0, weight=1)
        self.app_frame.columnconfigure(1, weight=1)
        self.app_frame.columnconfigure(2, weight=1)
        self.app_frame.rowconfigure(0, weight=1)
        self.app_frame.rowconfigure(1, weight=1)
        self.app_frame.rowconfigure(2, weight=1)
        self.app_frame.rowconfigure(3, weight=1)

    def create_select_mover(self):
        self.select_mover = {
            1: self.move1,
            2: self.move2,
            3: self.move3,
            4: self.move4,
            5: self.move5,
            6: self.move6,
            7: self.move7,
            8: self.move8,
            9: self.move9,
        }

    def move1(self):
        try:
            self.puzzle.move(1)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move2(self):
        try:
            self.puzzle.move(2)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move3(self):
        try:
            self.puzzle.move(3)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move4(self):
        try:
            self.puzzle.move(4)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move5(self):
        try:
            self.puzzle.move(5)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move6(self):
        try:
            self.puzzle.move6(1)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move7(self):
        try:
            self.puzzle.move(7)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move8(self):
        try:
            self.puzzle.move(8)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()

    def move9(self):
        try:
            self.puzzle.move(9)
        except Exception:
            messagebox.showinfo('Invalid Move', "you can't move this tile.")
        self.update_board()


root = tkinter.Tk()
Game(master=root)
root.mainloop()
