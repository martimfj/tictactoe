import tkinter as tk

class tabuleiro:
    def __init__(self):
        
        #Geometry.Tabuleiro        
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("TicTacToe Enjoo com Batata")
        self.tabuleiro.resizable(height = False, width=False)
        self.tabuleiro.geometry("300x300+0+0")
       
        #Colunas e fileiras:        
        for i in range (0,3):
           self.tabuleiro.rowconfigure(i, weight=1)
       
        for i in range (0,3):        
           self.tabuleiro.columnconfigure(i, weight=1)
        
        #Botões:
        self.botoes = [[1,2,3],
                       [4,5,6],
                       [7,8,9]]
        for i in range(0,3):
            for j in range(0,3):
                self.botoes[i][j] = tk.Button(self.tabuleiro)
                self.botoes[i][j].config(width = 6, height = 3, text="---", font=("Helvetica", 24))
                self.botoes[i][j].grid(row =  i, column = j, sticky = "nsew")          
                
        #LabelEstático:
        self.label1 = tk.Label(text='Próxima jogada:', font=("Helvetica", 12))
        self.label1.grid(row=3, column=0, columnspan=2, sticky="nsw")
      
        #LabeldasJogadas:
        self.label2 = tk.Label(text = "X", font=("Helvetica", 12))
        self.label2.grid(row = 3,column = 1, sticky = "nse")
    
    def iniciar(self):
        self.tabuleiro.mainloop()
    
    

JogodaVelha = tabuleiro()
JogodaVelha.iniciar()