

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
  
#------Soma das linhas para verificar ganhador------#
        self.somalinha1 = 0 
        for j in range (0,3):
            self.somalinha1 += self.tab[0][j] 
            if self.somalinha1 == 3:
                return 1 
            elif self.somalinha1 == 6:
                return 2
            else:
                return -1
           
        self.somalinha2 = 0 
        for j in range (0,3):
            self.somalinha2 += self.tab[1][j] 
            if self.somalinha2 == 3:
                return 1 
            elif self.somalinha2 == 6:
                return 2
            else:
                return -1
              
        self.somalinha3 = 0 
        for j in range (0,3):
            self.somalinha3 += self.tab[2][j]
            if self.somalinha3 == 3:
                return 1 
            elif self.somalinha3 == 6:
                return 2
            else:
                return -1

#------Soma das colunas para verificar jogador------#
        self.somacoluna1 = 0 
        for j in range (0,3):
            self.somacoluna1 += self.tab[j][0]
            if self.somacoluna1 == 3:
                return 1 
            elif self.somacoluna1 == 6:
               return 2
            else:
                return -1

        self.somacoluna2 = 0 
        for j in range (0,3):
            self.somacoluna2 += self.tab[j][1]
            if self.somacoluna2 == 3:
                return 1 
            elif self.somacoluna2 == 6:
                return 2
            else:
                return -1

        self.somacoluna3 = 0 
        for j in range (0,3):
            self.somacoluna3 += self.tab[j][2]
            if self.somacoluna3 == 3:
                return 1 
            elif self.somacoluna3 == 6:
                return 2
            else:
                return -1

#------Soma das diagonais para verificar ganhador------#
        if self.tab[0][0] + self.tab[1][1] + self.tab[2][2] == 3:
            return 1 
        elif self.tab[0][0] + self.tab[1][1] + self.tab[2][2] == 6:
            return 2
        else:
            return -1

#------Soma das diagonais para verificar empate------#
        if somalinha1 + somalinha2 + somalinha3 + somacoluna1 + somacoluna2 + somacoluna3 == 28:
          return 0
        else:
          return -1
           
#def limpa_jogadas(self):

