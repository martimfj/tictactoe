import tkinter as tk

class tabuleiro:
    def __init__(self):
       self.tabuleiro = tk.Tk()
       self.tabuleiro.geometry("378x340")
       self.tabuleiro.rowconfigure(0, minsize=113, weight=1)
       self.tabuleiro.rowconfigure(0, weight=1)
       self.tabuleiro.rowconfigure(0, minsize=113, weight=1)
       self.tabuleiro.rowconfigure(1, weight=1)
       self.tabuleiro.rowconfigure(0, minsize=113, weight=1)
       self.tabuleiro.rowconfigure(2, weight=1)
       self.tabuleiro.rowconfigure(0, minsize=37, weight=1)
       self.tabuleiro.rowconfigure(3, weight=1)
       self.tabuleiro.columnconfigure(0, minsize=113, weight= 113)
       self.tabuleiro.columnconfigure(0, weight=1)
       self.tabuleiro.columnconfigure(0, minsize=113, weight= 113)
       self.tabuleiro.columnconfigure(1, weight=1)
       self.tabuleiro.columnconfigure(0, minsize=113, weight= 113)
       self.tabuleiro.columnconfigure(2, weight=1)

  
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 9, height = 3 )
       botão.grid(row =  1, column = 1)
    
    def iniciar(self):
        self.tabuleiro.mainloop()

teste = tabuleiro()
teste.iniciar()