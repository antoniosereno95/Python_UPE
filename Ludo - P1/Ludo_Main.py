################ Regras do Jogo ##########
"""
-->Video para instrucoes: https://www.youtube.com/watch?v=m8NHoIqFg4A

Instruções e regras do jogo Ludo:

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

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.ordem_de_jogada = 0
        self.ultima_jogada_do_dado = 0
        self.posicao_no_percurso_normal = 0
        self.percurso_colorico = False
        self.posicao_percurso_colorido = 0

    def __str__(self):
        return f"Jogador: {str(self.nome).title()};Cor da peca: {str(self.cor).title()}"


'''--> fiz um debug e essa parte [e onde o erro estava nessa classe criada por mim, 
vou deixar aqui pra poder corrigir depois =)
-- o erro que mostrava na tela era um erro de recursao pq eu tinha colocado o .title()
ali no propety do atributo nome --

# class Jogador:
#
#     def __init__(self, nome:str, cor:str):
#         self.nome = nome
#         self.cor = cor
#         self.posicao_no_percurso_normal = 0
#         self.percurso_colorico = False
#         self.posicao_percurso_colorido = 0
#
#     #setters and getters
#     @property
#     def nome(self):
#         self.nome = str(self.nome).title()
#         return self.nome
#     @nome.setter
#     def nome(self, novo_nome):
#         self.nome = novo_nome
#     @property
#     def cor(self):
#         return self.cor
#     @cor.setter
#     def cor(self,nova_cor):
#         self.cor = str(nova_cor).title()
#     @property
#     def posicao_no_percurso_normal(self):
#         return self.posicao_no_percurso_normal
#     @property
#     def percurso_colorico(self):
#         return self.percurso_colorico
#     @property
#     def posicao_percurso_colorido(self):
#         return self.posicao_percurso_colorido
#     @posicao_no_percurso_normal.setter
#     def posicao_no_percurso_normal(self,nova_posicao):
#         self.posicao_no_percurso_normal = nova_posicao
#     @percurso_colorico.setter
#     def percurso_colorico(self, bool_percurso_colorido):
#         if(bool_percurso_colorido == True):
#             self.percurso_colorico = True
#         elif(bool_percurso_colorido == False):
#             self.percurso_colorico = False
#         else:
#             return f"A variavel #bool_percurso_colorido# so aceita estados booleanos."
#
#     def __str__(self):
#         return f"Jogador: {self.nome};Cor da peca:{self.cor}"
#
#     #acoes do jogador
#     def jogada(self):
#         pass
#         #chama o dado
'''

################ Metodos #################
def Menu1():
    print(f"Menu Principal:\n"
          f"1. Iniciar uma partida\n"
          f"2. Ver as Regras do jogo\n"
          f"3. Encerrar o programa\n"
          f"Digite o numero da opcao desejada:")
    #implementar um score board depois, tipo dos jogos de antigamente, se uma pessoa ganha o jogo e esta entre os 10 primeiros da tabela ja existenete ela pode colocar seu nome la ao lado do seu score.
    #o score consiste an soma dos roudns que ela jogou para ganhar, menos rounds remete a um score melhor.
    #um round consiste em uma jogada de cada jgador no jogo sendo ele maquina ou nao.
    #implementar o score board com arquivos
def Regras():
    try:
        a = open("ludo_regras.txt")
    except:
        print("Problemas ao abrir o arquivo de regras")
    else:
        with open("ludo_regras.txt") as arquivo:
            print(arquivo.read() + "\n\n")

def Cria_Objeto_Jogador(numero_de_jogadores): #depois tem que criar um criador de BOTs maquina!!
    lista_de_jogadores = []
    n_jogador = numero_de_jogadores
    numero_do_jogador = 1
    while(numero_do_jogador <= int(n_jogador)):
        print(f"Vamos cadastrar o jogador {numero_do_jogador}, porfavor responda as perguntas a seguir:")

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
                    if(nome_jogador == jogador.nome):
                        print("O nome digitado ja esta sendo utilizado, por favor tente novamente.")
                        reescrever_nome = True
            #fim do loop do nome

        #irei usar o mesmo metodo de verificacao pra cor
        reescrever_cor = True
        while(reescrever_cor):
            reescrever_cor = False

            cor_da_peca = input(f"Digite a cor da peca que voce deseja utilizar {infos_do_jogo.cores_peoes}: ")
            while(cor_da_peca not in infos_do_jogo.cores_peoes):
                print(f"Por favor digite uma cor que esteja listada em {infos_do_jogo.cores_peoes} :")
                cor_da_peca = input()

            for i in range(len(lista_de_jogadores)):
                    if(cor_da_peca == lista_de_jogadores[i].cor):
                        print(f"Esta cor ja esta sendo utilizada pelo jogador {lista_de_jogadores[i].nome}, por favor tente novamente:")
                        reescrever_cor = True
            #fim do loop de verificacao das cores

        #-->o debug acabou virando o codigo principal heuehuehu
        ##debug
        jogador = Jogador(nome_jogador, cor_da_peca)

        lista_de_jogadores.append(jogador)
        print(lista_de_jogadores)

        ##fim do debug
        ''' --> fiz um debug aqui e essa parte do codigo ficou ~obsoleta~, mas vou
        deixar aqui pq eu quero ver depois oq atav errada nela.
        #cria um jogador com o nome digitado e a cor solicitada
        # try:
        #     jogador = Jogador()
        #     jogador.nome = nome_jogador
        #     jogador.cor = cor_da_peca
        #
        # except:
        #     print("deu merda")
        # else:
        #     lista_de_jogadores.append(jogador)
        #     print("deu certo")
        '''
        numero_do_jogador = numero_do_jogador + 1

    return lista_de_jogadores


def Partida_do_jogo(lista_de_jogadores):
    print("entrou no jogo ...")#depois tem que tirar isso daqui
    #variaveis para o loop da partida
    numero_de_rounds = -1
    jogando = True
    round_end  = True
    vencedor = []
    debug = 0
    while(jogando):#loop da partida
        #se quiser tirar onda, da pra fazer um sort nos jogdores pra tabela de final de round ja mostrar na ordem da posicao em que o jogador esta.
        if(round_end):
            print(f"----- Round {numero_de_rounds} -----\n")
            for jogadoress in lista_de_jogadores:
                if(jogadoress.percurso_colorico == False):
                    print(f"Player: {str(jogadoress.nome).title()};Cor da pesa: {jogadoress.cor}; Posicao: {jogadoress.posicao_no_percurso_normal}/{infos_do_jogo.percurso_normal};Ultima_jogada_do_dado: {jogadoress.ultima_jogada_do_dado}")
                else:
                    print(f"Player: {str(jogadoress.nome).title()};Cor da pesa: {jogadoress.cor}; Posicao no Percurso colorido: {jogadoress.posicao_percurso_colorido}/{infos_do_jogo.percurso_colorido};Ultima_jogada_do_dado: {jogadoress.ultima_jogada_do_dado}")

        #essa parte de codigo fica aqui pq eu quero mostrar o round(tabela) pos o cara ganhar, pra aparecer os numeros fechados do cara que ganhou.
        if (len(vencedor) > 0 and vencedor[0] == True):
            jogando = False
            print("-+-"*26)
            print(f"O Jogador {vencedor[1]} ganhou a partida no round {numero_de_rounds} com as pecas de cor {vencedor[2]}")
            print("-+-" * 26)
            print("\n\n")

        #define e organiza a lista por quem vai jogar primeiro
        '''--> falta pensar como fazer essa questao aqui...
        if(numero_de_rounds == -1):
            for jogadoress in lista_de_jogadores:
                jogadoress.ultima_jogada_do_dado = DADO()

            for i in range(len(lista_de_jogadores)):
                if(lista_de_jogadores[i].ultima_jogada_do_dado > infos_do_jogo.):
                    pass
        '''
        #quando o jogo comeca de verdade
        if(numero_de_rounds >= 0):
            for jogadoress in lista_de_jogadores:
                numero_do_dado = DADO()
                jogadoress.ultima_jogada_do_dado = numero_do_dado
                if(jogadoress.percurso_colorico == False):
                    jogadoress.posicao_no_percurso_normal = jogadoress.posicao_no_percurso_normal + numero_do_dado
                    if(jogadoress.posicao_no_percurso_normal >= infos_do_jogo.percurso_normal):
                        jogadoress.posicao_no_percurso_normal = infos_do_jogo.percurso_normal
                        jogadoress.percurso_colorico = True
                elif(jogadoress.percurso_colorico == True):#redundante mas bom de ler heuheu
                    jogadoress.posicao_percurso_colorido = jogadoress.posicao_percurso_colorido + numero_do_dado
                    if(jogadoress.posicao_percurso_colorido == infos_do_jogo.percurso_colorido):
                        vencedor = [True,jogadoress.nome,jogadoress.cor]
                    else:
                        if(jogadoress.posicao_percurso_colorido < infos_do_jogo.percurso_colorido):
                            pass
                        elif(jogadoress.posicao_percurso_colorido > infos_do_jogo.percurso_colorido):
                            diferenca = jogadoress.posicao_percurso_colorido - infos_do_jogo.percurso_colorido
                            jogadoress.posicao_percurso_colorido = infos_do_jogo.percurso_colorido - diferenca
        numero_de_rounds = numero_de_rounds + 1
        debug = debug + 1
        if(debug >= 50):
            break
        #fim do loop do jogo.

def DADO():
    numero_aleatorio = random.randint(1,6)
    return numero_aleatorio

################ Main ####################
if(__name__ == "__main__"):
    infos_do_jogo = Infos_do_Jogo() #instancio o objeto para poder usar os recursos que estao dentro dele.
    ##-->debug
    #player_eu = Jogador("antonio","Azul")
    ##-fim do debug

    #Mensagem Inicial
    print()
    print("~"*35)
    print(f"    Bem vindo ao jogo de Ludo!")
    print("~" * 35)
    while(True):
        Menu1()
        resposta_1 = input()
        while resposta_1 not in "123":
            resposta_1 = input("Entrada invalida, tente novamente:")

        ###OPCOES DO MENU 1:###
        if(int(resposta_1) == 1):
            #inicia um novo jogo
            print("\n---Novo Jogo---")

            numero_de_jogadores = input("Quantos players humanos iram jogar?")#melhorar essa pergunta ai que ta feio
            while(numero_de_jogadores not in "1234"):
                numero_de_jogadores = input("Porfavor digite um numero inteiro de 1 a 4:")

            #crio os objetos necessarios para a partida
            lista_de_jogadores = Cria_Objeto_Jogador(numero_de_jogadores)
            #inicio um novo jogo com a lista de objetos jogadores a criada

            ##debug34
            print(lista_de_jogadores[0])
            print(lista_de_jogadores[1])
            ##--> o debug deu certo =)

            ### inicia-se uma nova PARTIDA de Ludo ####
            Partida_do_jogo(lista_de_jogadores)


        #regras
        elif(int(resposta_1) == 2):
            Regras()

        #sair do programa
        elif(int(resposta_1) == 3):
            Sair = input("Voce deseja realmente sair?(S/N)")
            while Sair.upper() not in "SN":
                Sair = input("entrada invalida, tente novamente(S/N):")
            if(Sair.upper() == "S"):
                print("Encerrando o programa...")
                break
            else:
                pass




