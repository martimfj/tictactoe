import tkinter as tk

class tabuleiro:
    def __init__(self):
       self.tabuleiro = tk.Tk()
       self.tabuleiro.geometry("378x340")
       
       #Colunas e fileiras:        
       for i in range (0,3):
           self.tabuleiro.rowconfigure(i, minsize=0, weight=1)
       
       for i in range (0,3):        
           self.tabuleiro.columnconfigure(i, minsize=0, weight=1)
           
       #Botões:
       for i in range (0,3):
           for j in range(0,3):    
                   botão = tk.Button(self.tabuleiro)
                   botão.config(width = 12, height = 6 )
                   botão.grid(row =  i, column = j, sticky = "nsew")       
       
       
       label = tk.Label(text='Próxima jogada:')
       label.grid(row=3, column=0, columnspan=2, sticky="nsw")


    
    def iniciar(self):
        self.tabuleiro.mainloop()
    
    

teste = tabuleiro()
teste.iniciar()