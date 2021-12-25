################ Regras do Jogo ##########
"""
-->Video para instrucoes: https://www.youtube.com/watch?v=m8NHoIqFg4A
Ludo
Instruções e regras do jogo

1. começo: Os peões de cada jogador começam na base de mesma cor.
O objetivo do jogo é ser o primeiro a levar seus 4 peões a dar
uma volta no tabuleiro e a chegar no ponto final marcado com sua cor.

2. movimentos: Os peões movem-se pelo percurso no sentido horário.
Para transportar um peão de sua base para seu ponto de partida
é necessário tirar 6. Quando o jogador já tem pelo menos um peão
no percurso, ele pode mover o peão o número de casas tirado no dado.
Se tirar 6, além de usar esse resultado, ele pode jogar novamente o dado.

3. final: Após dar a volta no tabuleiro o peão avança pela reta final,
de sua própria cor. A chegada ao ponto final só pode ser obtida por um
número exato nos dados. Se o jogador tirar mais que o necessário,
ele vai ate o fim e volta, tendo que aguardar sua próxima jogada.
O vencedor é o primeiro a levar os seus quatro peões ao ponto de
chegada da sua cor.
"""

######## infos adicionais ##########

#sao 56 casas no todal do percurso.
#quando chega no percurso colorido, existem mais 6 casa para serem avancadas.

################# Imports ################
import random
################# Classes ################
class Infos_do_Jogo:
    def __init__(self):
        self.percurso_normal = 56
        self.percurso_colorido = 6
        self.cores_peoes = ["Azul","Amarelo","Vermelho","Verde"]


class Jogador:

    def __Init__(self, nome, cor):
        self.nome = nome.title()
        self.cor = cor.title()
        self.posicao_no_percurso_normal = 0
        self.percurso_colorico = False
        self.posicao_percurso_colorido = 0

    #setters and getters
    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self,novo_nome):
        self.nome = novo_nome.title()
    @property
    def cor(self):
        return self.cor
    @cor.setter
    def cor(self,nova_cor):
        self.cor = nova_cor.title()
    @property
    def posicao_no_percurso_normal(self):
        return self.posicao_no_percurso_normal
    @property
    def percurso_colorico(self):
        return self.percurso_colorico
    @property
    def posicao_percurso_colorido(self):
        return self.posicao_percurso_colorido
    @posicao_no_percurso_normal.setter
    def posicao_no_percurso_normal(self,nova_posicao):
        self.posicao_no_percurso_normal = nova_posicao
    @percurso_colorico.setter
    def percurso_colorico(self, bool_percurso_colorido):
        if(bool_percurso_colorido == True):
            self.percurso_colorico = True
        elif(bool_percurso_colorido == False):
            self.percurso_colorico = False
        else:
            return f"A variavel #bool_percurso_colorido# so aceita estados booleanos."

    def Apresentacao_do_jogador(self):
        print(f"O jogador {self.nome} esta participando com as pecas de cor {self.cor}")

    #acoes do jogador
    def jogada(self):
        pass
        #chama o dado


################ Metodos #################
def Menu1():
    print(f"Bem vindo ao jogo de Ludo!\n"
          f"Menu Principal:\n"
          f"1. Iniciar uma partida\n"
          f"2. Ver as Regras do jogo\n"
          f"3. Encerrar o programa\n"
          f"Digite o numero da opcao desejada:")
    #implementar um score board depois, tipo dos jogos de antigamente, se uma pessoa ganha o jogo e esta entre os 10 primeiros da tabela ja existenete ela pode colocar seu nome la ao lado do seu score.
    #o score consiste an soma dos roudns que ela jogou para ganhar, menos rounds remete a um score melhor.
    #um round consiste em uma jogada de cada jgador no jogo sendo ele maquina ou nao.
    #implementar o score board com arquivos
def Regras():
    print("")
    #printa as regras, to com preguisa de arrumar o texto pra ficar bonito na tela.

def Menu2():
    pass

def Cria_Objeto_Jogador(lista_de_jogadores = []): #depois tem que criar um criador de BOTs maquina!!
    n_jogador = lista_de_jogadores[0]
    numero_do_jogador = 1
    while(numero_do_jogador <= n_jogador):
        print(f"Vamos cadastrar o jogador {numero_do_jogador}, porfavor resposda as perguntas a seguir:")

        #Pede o nome do jogador e ja verifica se existe um nome igual na lista de nomes de jogadores
        reescrever_nome = True #comeca como true pra entrar no loop
        while(reescrever_nome):
            reescrever_nome = False
            '''e logo depois eu torno a variavel false, pra poder efetuar a verificaca0
            e eventualmente se o nome nao for igual a um ja existente o loop ja se encerra no primeiro ciclo'''

            nome_jogador = input("Digite o nome do jogador: ")
            while (len(nome_jogador) <= 2):
                nome_jogador = input("Digite um nome de jogador valido(minimo de 2 letras): ")

            for i in range(len(lista_de_jogadores)):
                if(i!=0):
                    if(nome_jogador.title() == jogador.nome):
                        print("O nome digitado ja esta sendo utilizado, por favor tente novamente.")
                        reescrever_nome = True
            #fim do loop do nome

        #irei usar o mesmo metodo de verificacao pra cor
        reescrever_cor = True
        while(reescrever_cor):
            reescrever_cor = False

            cor_da_peca = input(f"Digite a cor da peca que voce deseja utilizar [{infos_do_jogo.cores_peoes}]: ")
            while(cor_da_peca.title() not in infos_do_jogo.cores_peoes):
                print(f"Por favor digite uma cor que esteja listada em {infos_do_jogo.cores_peoes} :")
                cor_da_peca = input()

            for i in range(len(lista_de_jogadores)):
                if(i != 0):
                    if(cor_da_peca.title() == lista_de_jogadores[i].nome):
                        print(f"Esta cor ja esta sendo utilizada pelo jogador {lista_de_jogadores[i].nome}, por favor tente novamente:")


        #cria um jogador com o nome digitado e a cor solicitada
        try:
            jogador = Jogador()
            jogador.nome = nome_jogador
            jogador.cor = cor_da_peca

        except:
            print("deu merda")
        else:
            lista_de_jogadores.append(jogador)
            print("deu certo")

    numero_do_jogador = numero_do_jogador + 1 #add 1 ao numero do jogador que vai ser criado no momento


def Partida_do_jogo():
    print("entrou no jogo ...")


################ Main ####################
if(__name__ == "__main__"):
    infos_do_jogo = Infos_do_Jogo() #instacio o objeto para poder usar os recursos que estao dentro dele.

    while(True):
        Menu1()
        resposta_1 = input()
        while resposta_1 not in "123":
            resposta_1 = input("Entrada invalida, tente novamente:")

        ###OPCOES DO MENU 1:###
        if(int(resposta_1) == 1):
            #inicia um novo jogo
            print("\n---Novo Jogo---")
            lista_de_jogadores = []
            numero_de_jogadores = input("Quantos players humanos iram jogar?")#melhorar essa pergunta ai que ta feio
            while(numero_de_jogadores not in "1234"):
                numero_de_jogadores = input("Porfavor digite um numero inteiro de 1 a 4:")

            #adiciono o numero de jogadores ao indice ZERO da lista
            lista_de_jogadores.append(numero_de_jogadores)
            #crio os objetos necessarios para a partida
            lista_de_jogadores = Cria_Objeto_Jogador(lista_de_jogadores)
            #inicio um novo jogo com a lista de objetos jogadores a criada

            jogando = True
            while(jogando):
                Partida_do_jogo()
                break #break de debug

        #regras
        elif(int(resposta_1) == 2):
            Regras()
        #sai do programa
        elif(int(resposta_1) == 3):
            Sair = input("Voce deseja realmente sair?(S/N)")
            while Sair.upper() not in "SN":
                Sair = input("entrada invalida, tente novamente(S/N):")
            if(Sair == "S"):
                print("Encerrando o programa...")
                break
            else:
                pass
