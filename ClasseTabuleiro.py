import tkinter as tk
import ClasseJogo
import tkinter.messagebox as tkm

class tabuleiro:
    def __init__(self):
        self.meu_jogo = ClasseJogo.Jogo()
        
        #Geometry.Tabuleiro        
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Enjoo com Batata")

        self.tabuleiro.geometry("300x300+0+0")
        
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
                       
        self.botoes[0][0] = tk.Button(self.tabuleiro)
        self.botoes[0][0].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao00_clicado)
        self.botoes[0][0].grid(row =  0, column = 0, sticky = "nsew")

        self.botoes[0][1] = tk.Button(self.tabuleiro)
        self.botoes[0][1].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao01_clicado)
        self.botoes[0][1].grid(row =  0, column = 1, sticky = "nsew")

        self.botoes[0][2] = tk.Button(self.tabuleiro)
        self.botoes[0][2].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao02_clicado)
        self.botoes[0][2].grid(row =  0, column = 2, sticky = "nsew")          

        self.botoes[1][0] = tk.Button(self.tabuleiro)
        self.botoes[1][0].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao10_clicado)
        self.botoes[1][0].grid(row =  1, column = 0, sticky = "nsew")          

        self.botoes[1][1] = tk.Button(self.tabuleiro)
        self.botoes[1][1].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao11_clicado)
        self.botoes[1][1].grid(row =  1, column = 1, sticky = "nsew")          

        self.botoes[1][2] = tk.Button(self.tabuleiro)
        self.botoes[1][2].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao12_clicado)
        self.botoes[1][2].grid(row =  1, column = 2, sticky = "nsew")

        self.botoes[2][0] = tk.Button(self.tabuleiro)
        self.botoes[2][0].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao20_clicado)
        self.botoes[2][0].grid(row =  2, column = 0, sticky = "nsew")          

        self.botoes[2][1] = tk.Button(self.tabuleiro)
        self.botoes[2][1].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao21_clicado)
        self.botoes[2][1].grid(row =  2, column = 1, sticky = "nsew")          

        self.botoes[2][2] = tk.Button(self.tabuleiro)
        self.botoes[2][2].configure(width = 6, height = 3, text = '---', font=("Helvetica", 24), command = self.botao22_clicado)
        self.botoes[2][2].grid(row =  2, column = 2, sticky = "nsew")                                       
    

    def botao00_clicado(self):
        self.meu_jogo.recebe_jogada(0,0)
        if self.meu_jogo.jogador == 1:
            self.botoes[0][0].configure(text = 'X')
            self.botoes[0][0].configure(state = 'disabled')
            self.textolabel2.set("O")
        else:
            self.botoes[0][0].configure(text = 'O')
            self.botoes[0][0].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 8:
            print("X ganhou") 
        elif resultado == 0:
            return 0
        else:
            print("Empate")
            
    def botao01_clicado(self):
        self.meu_jogo.recebe_jogada(0,1)
        if self.meu_jogo.jogador == 1:
            self.botoes[0][1].configure(text = 'X')
            self.botoes[0][1].configure(state = 'disabled')
            self.textolabel2.set("O")

        else:
            self.botoes[0][1].configure(text = 'O')
            self.botoes[0][1].configure(state = 'disabled')
            self.textolabel2.set("x")

        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate")        
            
    def botao02_clicado(self):
        self.meu_jogo.recebe_jogada(0,2)
        if self.meu_jogo.jogador == 1:
            self.botoes[0][2].configure(text = 'X')
            self.botoes[0][2].configure(state = 'disabled')
            self.textolabel2.set("O")

        else:
            self.botoes[0][2].configure(text = 'O')
            self.botoes[0][2].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate")
            
    def botao10_clicado(self):
        self.meu_jogo.recebe_jogada(1,0)
        if self.meu_jogo.jogador == 1:
            self.botoes[1][0].configure(text = 'X')
            self.botoes[1][0].configure(state = 'disabled')
            self.textolabel2.set("O")
        else:
            self.botoes[1][0].configure(text = 'O')
            self.botoes[1][0].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate")
    def botao11_clicado(self):
        
        self.meu_jogo.recebe_jogada(1,1)
        if self.meu_jogo.jogador == 1:
            self.botoes[1][1].configure(text = 'X')
            self.botoes[1][1].configure(state = 'disabled')
            self.textolabel2.set("O")
        else:
            self.botoes[1][1].configure(text = 'O')
            self.botoes[1][1].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate")
            
    def botao12_clicado(self):
        self.meu_jogo.recebe_jogada(1,2)
        if self.meu_jogo.jogador == 1:
            self.botoes[1][2].configure(text = 'X') 
            self.botoes[1][2].configure(state = 'disabled')
            self.textolabel2.set("O")
        else:
            self.botoes[1][2].configure(text = 'O')
            self.botoes[1][2].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate") 
            
    def botao20_clicado(self):
        self.meu_jogo.recebe_jogada(2,0)
        if self.meu_jogo.jogador == 1:
            self.botoes[2][0].configure(text = 'X')
            self.botoes[2][0].configure(state = 'disabled')
            self.textolabel2.set("O")
        else:
            self.botoes[2][0].configure(text = 'O')
            self.botoes[2][0].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate")
    
    def botao21_clicado(self):
        self.meu_jogo.recebe_jogada(2,1)
        if self.meu_jogo.jogador == 1:
            self.botoes[2][1].configure(text = 'X')
            self.botoes[2][1].configure(state = 'disabled')
            self.textolabel2.set("O")
        else:
            self.botoes[2][1].configure(text = 'O')
            self.botoes[2][1].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate")
        
    
    def botao22_clicado(self):
        self.meu_jogo.recebe_jogada(2,2)
        if self.meu_jogo.jogador == 1:
            self.botoes[2][2].configure(text = 'X') 
            self.botoes[2][2].configure(state = 'disabled')
            self.textolabel2.set("O")
            
        else:
            self.botoes[2][2].configure(text = 'O')
            self.botoes[2][2].configure(state = 'disabled')
            self.textolabel2.set("X")
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
            print("O ganhou")
        elif resultado == 2:
            print("X ganhou")
        elif resultado == 0:
            return 0
        else:
            print("Empate")
        
    def resultado(self): 
        resultado = self.meu_jogo.verifica_ganhador()
        if resultado == 1:
                print("O ganhou")
        elif resultado == 2:
                print("X ganhou")
        elif resultado == 0:
                return 0
        else:
                print("Empate")


    def vencedor(self, verifica_ganhador):
        continuar = tkm.askquestion("Alerta: {0}".format(self.resultado), "Gostaria de jogar outra?", icon='warning')
        
    def limpa_jogadas(self):
        if continuar == "no":
            self.tabuleiro.destroy()   

    def iniciar(self):
        self.tabuleiro.mainloop()



JogodaVelha = tabuleiro()
JogodaVelha.iniciar()