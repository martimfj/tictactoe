

<<<<<<< HEAD
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
     
=======
#receber jogada por botao, verificar se jogo terminou, 
#alterar jogadores
    
class Jogo:
    def __init__(self):
        self.tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jogador = 1 #1 = Jogador X

    def recebe_jogada(self, linha, coluna): #receber e registrar a jogada, deve alterar os jogadores e não retorna nada.
        self.tabuleiro[linha][coluna] = self.jogador
        if self.jogador == 1:
        	self.jogador = 2
        else: 
        	self.jogador = 1
    
    def verifica_ganhador(self): #Retorna 0 em empate, 1 se X vencer, 2 se O vencer, -1 caso contrário.
    	for 
    	if self.tabuleiro: 		#O venceu
            return 2 
        elif  	:		#X venceu
            return 1
        elif    :		#Empate
            return 0
        else:			#Jogo não acabou
        	return -1 	
>>>>>>> d5e67ae9ae46c8e2d96a5ccac49180f1859a413b

#def limpa_jogadas(self):