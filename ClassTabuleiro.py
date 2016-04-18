import tkinter as tk

class tabuleiro:
    def __init__(self):
      self.tabuleiro = tk.Tk()
      self.tabuleiro.title("TicTacToe Enjoo com Batata")
      self.tabuleiro.resizable(height = False, width=False)
      self.tabuleiro.geometry("300x300")
       
      #Colunas e fileiras:        
      for i in range (0,3):
           self.tabuleiro.rowconfigure(i, weight=1)
       
      for i in range (0,3):        
           self.tabuleiro.columnconfigure(i, weight=1)
           
      #Botões:
      matriz_botoes = [[1,2,3],
                        [4,5,6],
                        [7,8,9]]
  
      for i in range(0,3):
           for j in range(0,3):
               matriz_botoes[i][j] = tk.Button(self.tabuleiro)
               matriz_botoes[i][j].config(width = 6, height = 3, text="---", font=("Helvetica", 24))
               matriz_botoes[i][j].grid(row =  i, column = j, sticky = "nsew")    
                 
      
      
      #Label:
      label = tk.Label(text='Próxima jogada:', font=("Helvetica", 12))
      label.grid(row=3, column=0, columnspan=2, sticky="nsw")


    
    def iniciar(self):
      self.tabuleiro.mainloop()
    
    

teste = tabuleiro()
teste.iniciar()