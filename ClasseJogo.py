

class Jogo:  
    def __init__(self):
        
        #tabuleiro e jogador atual
    
        self.tab = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]

        self.jogador = 1 


    def recebe_jogada(self, linha, coluna): #receber e registrar a jogada, deve alterar os jogadores e não retorna nada.
        self.tab[linha][coluna] = self.jogador    
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1

#def verifica_ganhador(self): #Retorna 0 em empate, 1 se X vencer, 2 se O vencer, -1 caso contrário.
     

#def limpa_jogadas(self):