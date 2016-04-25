

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
          self.jogador = 2 #O
        else: 
        	self.jogador = 1 #X

    def verifica_ganhador(self): #Retorna 0 em empate, 1 se X vencer, 2 se O vencer, -1 caso contrário.
  
#------verificar ganhador------#
        self.multlinha1 = self.tab[0][0] * self.tab[0][1] * self.tab[0][2] 
        self.multlinha2 = self.tab[1][0] * self.tab[1][1] * self.tab[1][2] 
        self.multlinha3 = self.tab[2][0] * self.tab[2][1] * self.tab[2][2] 
        self.multcoluna1 = self.tab[0][0] * self.tab[1][0] * self.tab[2][0] 
        self.multcoluna2 = self.tab[0][1] * self.tab[1][1] * self.tab[2][1] 
        self.multcoluna3 = self.tab[0][2] * self.tab[1][2] * self.tab[2][2]
        self.multdiagonal = self.tab[0][0] * self.tab[1][1] * self.tab[2][2]
        self.multdiagonal2 = self.tab[0][2] * self.tab[1][1] * self.tab[2][0]
        
        if self.multcoluna1 == 1:
            return 1
        elif self.multcoluna1 == 8:
            return 2
        elif self.multcoluna2 == 1:
            return 1
        elif self.multcoluna2 == 8:
            return 2
        elif self.multcoluna3 == 1:
            return 1
        elif self.multcoluna3 == 8:
            return 2
        elif self.multlinha1 == 1:
            return 1
        elif self.multlinha1 == 8:
            return 2
        elif self.multlinha2 == 1:
            return 1
        elif self.multlinha2 == 8:
            return 2
        elif self.multlinha3 == 1:
            return 1
        elif self.multlinha3 == 8:
            return 2
        elif self.multdiagonal == 1:
            return 1
        elif self.multdiagonal == 8:
            return 2
        elif self.multdiagonal2 == 1:
            return 1
        elif self.multdiagonal2 == 8:
            return 2
        elif self.multlinha1 == 0 or self.multlinha2 == 0 or self.multlinha3 == 0 or self.multcoluna1 == 0 or self.multcoluna2 == 0 or self.multcoluna3 == 0:
            return -1
        else:
            return 0

    def limpa_jogadas(self):
        for i in range (0,3):
            for j in range(0,3):
                self.tab[i][j] = 0
