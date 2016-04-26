import tkinter as tk
import ClasseJogo

class tabuleiro:
    def __init__(self):
        self.meu_jogo = ClasseJogo.Jogo()
        
        #Geometry.Tabuleiro        
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Enjoo com Batata")
        self.tabuleiro.resizable(height = False, width=False)
        self.tabuleiro.geometry("300x300+500+500")
        
        #Colunas e fileiras:        
        for i in range (0,3):
           self.tabuleiro.rowconfigure(i, weight=1)
       
        for i in range (0,3):        
           self.tabuleiro.columnconfigure(i, weight=1)
           
         #LabelEstático:   
        self.label1 = tk.Label(text='Próxima jogada:', font=("Helvetica", 12))
        self.label1.grid(row=3, column=0, columnspan=2, sticky="nsw")
      
        #LabeldasJogadas:
        self.textolabel2 = tk.StringVar()        
        self.label2 = tk.Label(textvariable = self.textolabel2 , font=("Helvetica", 12))
        self.label2.grid(row = 3,column = 1, sticky = "nse")   
        self.textolabel2.set("O")
        
        #Botões:
        self.botoes = [[1,2,3],
                       [4,5,6],
                       [7,8,9]]

        import mp3play
        Somzera1 = mp3play.load('round.mp3'); play = lambda: Somzera.play()

        self.botoes[0][0] = tk.Button(self.tabuleiro)
        self.botoes[0][0].configure(width = 6, bg = "ivory4", height = 3, text = '---', font=("Helvetica", 24), command = self.botao00_clicado)
        self.botoes[0][0].grid(row =  0, column = 0, sticky = "nsew")

        self.botoes[0][1] = tk.Button(self.tabuleiro)
        self.botoes[0][1].configure(width = 6, bg = "ivory3", height = 3, text = '---', font=("Helvetica", 24), command = self.botao01_clicado)
        self.botoes[0][1].grid(row =  0, column = 1, sticky = "nsew")

        self.botoes[0][2] = tk.Button(self.tabuleiro)
        self.botoes[0][2].configure(width = 6, bg = "ivory4", height = 3, text = '---', font=("Helvetica", 24), command = self.botao02_clicado)
        self.botoes[0][2].grid(row =  0, column = 2, sticky = "nsew")          

        self.botoes[1][0] = tk.Button(self.tabuleiro)
        self.botoes[1][0].configure(width = 6,  bg = "ivory3", height = 3, text = '---', font=("Helvetica", 24), command = self.botao10_clicado)
        self.botoes[1][0].grid(row =  1, column = 0, sticky = "nsew")          

        self.botoes[1][1] = tk.Button(self.tabuleiro)
        self.botoes[1][1].configure(width = 6, bg = "ivory4", height = 3, text = '---', font=("Helvetica", 24), command = self.botao11_clicado)
        self.botoes[1][1].grid(row =  1, column = 1, sticky = "nsew")          

        self.botoes[1][2] = tk.Button(self.tabuleiro)
        self.botoes[1][2].configure(width = 6,  bg = "ivory3", height = 3, text = '---', font=("Helvetica", 24), command = self.botao12_clicado)
        self.botoes[1][2].grid(row =  1, column = 2, sticky = "nsew")

        self.botoes[2][0] = tk.Button(self.tabuleiro)
        self.botoes[2][0].configure(width = 6, bg = "ivory4", height = 3, text = '---', font=("Helvetica", 24), command = self.botao20_clicado)
        self.botoes[2][0].grid(row =  2, column = 0, sticky = "nsew")          

        self.botoes[2][1] = tk.Button(self.tabuleiro)
        self.botoes[2][1].configure(width = 6,  bg = "ivory3", height = 3, text = '---', font=("Helvetica", 24), command = self.botao21_clicado)
        self.botoes[2][1].grid(row =  2, column = 1, sticky = "nsew")          

        self.botoes[2][2] = tk.Button(self.tabuleiro)
        self.botoes[2][2].configure(width = 6, bg = "ivory4", height = 3, text = '---', font=("Helvetica", 24), command = self.botao22_clicado)
        self.botoes[2][2].grid(row =  2, column = 2, sticky = "nsew")                                       
    

    def botao00_clicado(self):
        self.meu_jogo.recebe_jogada(0,0)
        if self.meu_jogo.jogador == 1:
            self.botoes[0][0].configure(text = 'O')
            self.botoes[0][0].configure(state = 'disabled', bg = "SteelBlue1", command = play)
            self.textolabel2.set("X")
        else:
            self.botoes[0][0].configure(text = 'X')
            self.botoes[0][0].configure(state = 'disabled', bg = "IndianRed1", command = play)
            self.textolabel2.set("O")
        self.resultado()
            
    def botao01_clicado(self):
        self.meu_jogo.recebe_jogada(0,1)
        if self.meu_jogo.jogador == 1:
            self.botoes[0][1].configure(text = 'O')
            self.botoes[0][1].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")

        else:
            self.botoes[0][1].configure(text = 'X')
            self.botoes[0][1].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()      
            
    def botao02_clicado(self):
        self.meu_jogo.recebe_jogada(0,2)
        if self.meu_jogo.jogador == 1:
            self.botoes[0][2].configure(text = 'O')
            self.botoes[0][2].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")

        else:
            self.botoes[0][2].configure(text = 'X')
            self.botoes[0][2].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()
            
    def botao10_clicado(self):
        self.meu_jogo.recebe_jogada(1,0)
        if self.meu_jogo.jogador == 1:
            self.botoes[1][0].configure(text = 'O')
            self.botoes[1][0].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")
        else:
            self.botoes[1][0].configure(text = 'X')
            self.botoes[1][0].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()

    def botao11_clicado(self):
        
        self.meu_jogo.recebe_jogada(1,1)
        if self.meu_jogo.jogador == 1:
            self.botoes[1][1].configure(text = 'O')
            self.botoes[1][1].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")
        else:
            self.botoes[1][1].configure(text = 'X')
            self.botoes[1][1].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()
            
    def botao12_clicado(self):
        self.meu_jogo.recebe_jogada(1,2)
        if self.meu_jogo.jogador == 1:
            self.botoes[1][2].configure(text = 'O') 
            self.botoes[1][2].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")
        else:
            self.botoes[1][2].configure(text = 'X')
            self.botoes[1][2].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()
            
    def botao20_clicado(self):
        self.meu_jogo.recebe_jogada(2,0)
        if self.meu_jogo.jogador == 1:
            self.botoes[2][0].configure(text = 'O')
            self.botoes[2][0].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")
        else:
            self.botoes[2][0].configure(text = 'X')
            self.botoes[2][0].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()
            
    def botao21_clicado(self):
        self.meu_jogo.recebe_jogada(2,1)
        if self.meu_jogo.jogador == 1:
            self.botoes[2][1].configure(text = 'O')
            self.botoes[2][1].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")
        else:
            self.botoes[2][1].configure(text = 'X')
            self.botoes[2][1].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()
        
    
    def botao22_clicado(self):
        self.meu_jogo.recebe_jogada(2,2)
        if self.meu_jogo.jogador == 1:
            self.botoes[2][2].configure(text = 'O') 
            self.botoes[2][2].configure(state = 'disabled', bg = "SteelBlue1")
            self.textolabel2.set("X")
            
        else:
            self.botoes[2][2].configure(text = 'X')
            self.botoes[2][2].configure(state = 'disabled', bg = "IndianRed1")
            self.textolabel2.set("O")
        self.resultado()
        
    def resultado(self): 
        resultado = self.meu_jogo.verifica_ganhador()
        self.texto = "0"
        if resultado == 1:
            print("X ganhou")
            self.texto = "X ganhou"
            self.vencedor()
        elif resultado == 2:
            print("O ganhou")
            self.texto = "O ganhou"
            self.vencedor()
        elif resultado == 0:
            print("Empate")
            self.texto = "Empate"
            self.vencedor()
        else:
            return -1
            
    def vencedor(self):
        from tkinter import messagebox
        wishcontinuar = messagebox.askyesno("O jogo acabou!", "{0} . Deseja continuar jogando?".format(self.texto))
        
        if wishcontinuar == False:
            self.fechatabuleiro()
        else:
            for i in range (0,3):
                for j in range (0,3):
                    self.botoes[i][j].configure(text= "---", bg = "snow" , state = "normal")
            self.meu_jogo.limpa_jogadas()

    def fechatabuleiro(self):
        self.tabuleiro.destroy()

    def iniciar(self):
        self.tabuleiro.mainloop()




JogodaVelha = tabuleiro()
JogodaVelha.iniciar()