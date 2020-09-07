import tkinter as tk
from tkinter import messagebox

from Game import Game


class GameUI:
    def __init__(self):
        self.game = Game()
        self.GameUI = tk.Tk()
        self.GameUI.title("Tic Tac Toe")
        self.GameUI.resizable(height=False, width=False)
        self.GameUI.geometry("300x300+00+00")

        for i in range(3):
            self.GameUI.rowconfigure(i, weight=1)
            self.GameUI.columnconfigure(i, weight=1)

        self.info_label = tk.Label(text='Próxima jogada:', font=("Helvetica", 12))
        self.info_label.grid(row=3, column=0, columnspan=2, sticky="nsw")

        self.label_text = tk.StringVar()
        self.turn_label = tk.Label(textvariable=self.label_text, font=("Helvetica", 12))
        self.turn_label.grid(row=3, column=1, sticky="nse")
        self.label_text.set("O")

        button = tk.Button(self.GameUI, width=6, font=("Helvetica", 24), bg="ivory4", height=3, text='---')
        self.buttons = [[button for i in range(3)] for j in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(command=lambda row=row, col=col: self.button_pressed(row, col))
                self.buttons[row][col].grid(row=row, column=col, sticky="nsew")

    def reset_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(font=("Helvetica", 24), text="---", bg="snow", state="normal")

    def button_pressed(self, row, col):
        self.game.register_play(row, col)
        if self.game.player == 1:
            self.buttons[row][col].configure(text='O')
            self.buttons[row][col].configure(state='disabled', bg="SteelBlue1")
            self.label_text.set("X")
        else:
            self.buttons[row][col].configure(text='X')
            self.buttons[row][col].configure(state='disabled', bg="IndianRed1")
            self.label_text.set("O")
        self.check_winner()

    def check_winner(self):
        result = self.game.check_winner()
        result_map = {1: "X", 2: "O", 0: "Empate"}
        if result in result_map.keys():
            result_text = result_map[result]
            self.end_game_popup(result_text)

    def end_game_popup(self, winner_name):
        if winner_name == "Empate":
            response = messagebox.askyesno(title="O jogo empatou",
                                           message="Desejam continuar jogando?")
        else:
            response = messagebox.askyesno(title=f"Jogador '{winner_name}' ganhou o jogo",
                                           message="Desejam continuar jogando?")

        if not response:
            self.close_game()
        else:
            self.reset_buttons()
            self.game.clean_cells()

    def close_game(self):
        self.GameUI.destroy()

    def open_game(self):
        self.GameUI.mainloop()


TicTacToe = GameUI()
TicTacToe.open_game()
