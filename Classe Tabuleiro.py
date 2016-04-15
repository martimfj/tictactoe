import tkinter as tk


tabuleiro= tk.Tk()
tabuleiro.geometry("300x400")
tabuleiro.rowconfigure(0, minsize=100, weight=1)
tabuleiro.rowconfigure(3, weight=1)
tabuleiro.columnconfigure(0, minsize=100, weight=1)
tabuleiro.columnconfigure(3, weight=1)
tabuleiro.mainloop()

botão = tk.Button(tabuleiro, bg = 'blue')
botão.grid(row = 2, column = 2, sticky = 'W')
