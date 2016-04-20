

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
#        if self.tab[0][0] + self.tab[0][1] + self.tab[0][2] == 3:
#            return 1 
#        elif self.tab[1][0] + self.tab[1][1] + self.tab[1][2] == 3: 
#           return 1
#        elif self.tab[2][0] + self.tab[2][1] + self.tab[2][2] == 3: 
      self.somalinha1 = 0 
        for j in range (0,3):
          self.somalinha1 += self.tab[0][j] 
            if self.somalinha1 == 3:
              return 1 
            elif self.somalinha1 == 6:
              return 2 
           
           
      self.somalinha2 = 0 
        for j in range (0,3):
          self.somalinha2 += self.tab[1][j] 
            if self.somalinha2 == 3:
              return 1 
            elif self.somalinha2 == 6:
              return 2 
           
           
      self.somalinha3 = 0 
      for j in range (0,3):
          self.somalinha3 += self.tab[2][j]
            if self.somalinha3 == 3:
              return 1 
            elif self.somalinha3 == 6:
              return 2 
           
      print(self.somalinha1, self.somalinha2, self.somalinha3)

#def limpa_jogadas(self):