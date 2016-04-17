import tkinter as tk

class tabuleiro:
    def __init__(self):
       self.tabuleiro = tk.Tk()
       self.tabuleiro.geometry("378x340")
       
       self.tabuleiro.rowconfigure(0, minsize=0, weight=1)
       
       self.tabuleiro.rowconfigure(1, minsize=0, weight=1)
       
       self.tabuleiro.rowconfigure(2, minsize=0, weight=1)
       
       self.tabuleiro.rowconfigure(3, minsize=0, weight=1)
       
       self.tabuleiro.columnconfigure(0, minsize=0, weight=1)
       
       self.tabuleiro.columnconfigure(1, minsize=0, weight=1)
       
       self.tabuleiro.columnconfigure(2, minsize=0, weight=1)

  
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  0, column = 0, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  1, column = 0, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  2, column = 0, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  0, column = 1, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  1, column = 1, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  2, column = 1, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  0, column = 2, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  1, column = 2, sticky = "nsew")
       botão = tk.Button(self.tabuleiro)
       botão.config(width = 12, height = 6 )
       botão.grid(row =  2, column = 2, sticky = "nsew")
       
       
       label = tk.Label(self.tabuleiro)
       label.configure(font = ("Times", "24", "bold italic"))
       label.grid(row=3, column=0, columnspan=2, sticky="nsew")


    
    def iniciar(self):
        self.tabuleiro.mainloop()
    
    

teste = tabuleiro()
teste.iniciar()