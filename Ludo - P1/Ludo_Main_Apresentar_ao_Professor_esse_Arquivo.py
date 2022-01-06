################# Imports ################
import random

################# Classes ################
class Infos_do_Jogo:
    def __init__(self):
        self.percurso_normal = 56
        self.percurso_colorido = 6
        self.cores_peoes = ["Azul", "Amarelo", "Vermelho", "Verde"]
        self.numero_de_peoes = 4
        self.dificuldade_bots = 0
        self.hardocore = False


class Jogador:

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.ordem_de_jogada = 0
        self.ultima_jogada_do_dado = 0
        self.posicao_no_percurso_normal = 0
        self.percurso_colorico = False
        self.posicao_percurso_colorido = 0
        self.peoes_que_terminaram_o_trageto = 0
        self.peoes_na_zona_neutra = True
        self.bot = False
        self.primeira_jogada = 0

    def __str__(self):
        return f"Jogador: {str(self.nome).title()};Cor da peca: {str(self.cor).title()}"


################ Metodos #################
def Menu1():
    print(f"Menu Principal:\n"
          f"1. Iniciar uma partida\n"
          f"2. Ver as Regras do jogo\n"
          f"3. Tabela dos Campeoes\n"
          f"4. Encerrar o programa\n"
          f"Digite o numero da opcao desejada:")


def Menu_dificildade_dos_bots():
    print(f"Player: voce ira jogar contra bots neste jogo!\nPorvafor escolha uma dificuldade:\n"
          f"1. Facil - Os bot nao tirar numeros altos nos dados.\n"
          f"2. Medio - Os bot tem menos chances de tirar numeros altos no dados.\n"
          f"3. Dificil - Os bots tem as mesmas chances que um Player nos dados\n"
          f"4. Hardcore - O Player tem DESVANTAGEM nos dados em relacao aos bots.\n"
          )


def Regras():
    try:
        a = open("ludo_regras.txt")
    except:
        print("Problemas ao abrir o arquivo de regras")
    else:
        with open("ludo_regras.txt") as arquivo:
            print(arquivo.read() + "\n\n")


def le_quadro_de_campeoes_e_devolve_lista():
    # esse metodo so le e devolve uma lista com os negocios de cada um dos 10 campeoes
    try:
        a = open("quadro_de_campeoes_ludo.txt")
    except:
        print("Problemas ao abrir o arquivo de regras")
    else:
        with open("quadro_de_campeoes_ludo.txt") as arquivo:
            linha_do_arquivo = arquivo.read()
    finally:
        a.close()

    # bota a linha do arquivo em uma lista que vai ser passadaa diante
    lista_de_10_campeoes = []
    linha_do_arquivo.replace("\n", "")
    lista = linha_do_arquivo.split(";")
    for itens in lista:
        mini_lista_interna = []
        mini_lista_interna = itens.split(",")
        lista_de_10_campeoes.append(mini_lista_interna)
    # agora a lisat de campeoes tem 10 mini listas cada uma
    # com 2 itens sendo o 0 um nome e o 1 um numero de score

    # retira o \n e qualquer espaco em branco que eu notei que fica no fim da lista
    for elemento in lista_de_10_campeoes:
        elemento[0].replace("\n", "").replace(" ", "")
        elemento[1].replace("\n", "").replace(" ", "")

    return lista_de_10_campeoes


def Mostra_tabela_de_Campeos():
    lista_de_campeos = le_quadro_de_campeoes_e_devolve_lista()

    print("------ Tabela de Campeos ------")
    for campeoes in lista_de_campeos:
        print(f"Campeao: {campeoes[0]} --- Score: {campeoes[1]}")
    print("-------------------------------")


def tem_direito_ao_quadro_dos_campeos(lista_vencedor):
    tem_direito = False
    lista_de_campeos = le_quadro_de_campeoes_e_devolve_lista()

    if (lista_vencedor[4] == True):
        tem_direito = False

    elif (len(lista_de_campeos) < 10):
        tem_direito = True

    elif (len(lista_de_campeos) == 10):
        for campeos_na_lista in lista_de_campeos:
            if (int(lista_vencedor[2]) >= int(campeos_na_lista[1])):
                # nesse if aqui em cima eu comparo os rounds de cada campeao.
                tem_direito = True

    elif (len(lista_de_campeos) > 10):
        print("DEBUG: lista de campeos tem indice maior que 10, arruma isso ai bro heuheueh")

    return tem_direito


def Reorganiza_quadro_de_campeoes(lista_vencedor):
    lista_de_campeos = le_quadro_de_campeoes_e_devolve_lista()
    mini_lista_novo_campeao = []
    mini_lista_novo_campeao.append(lista_vencedor[1])
    # add o nome a mini lista

    mini_lista_novo_campeao.append(str(lista_vencedor[2]))
    # add round ou score

    if (len(lista_de_campeos) < 10):
        lista_de_campeos.append(mini_lista_novo_campeao)
        lista_de_campeos.sort(key=Funcion_Sort)

    elif (len(lista_de_campeos) == 10):
        lista_de_campeos.append(mini_lista_novo_campeao)
        lista_de_campeos.sort(key=Funcion_Sort)
        lista_de_campeos.pop(10)

    elif (len(lista_de_campeos) > 10):
        print("DEBUG: a lista tem 11 itens, algo aconteceu de errado, vou arrumar agora, nao se preocupe")
        lista_de_campeos.append(mini_lista_novo_campeao)
        lista_de_campeos.sort(key=Funcion_Sort)
        while (len(lista_de_campeos) != 10):
            ultimo_index = int(len(lista_de_campeos)) - 1
            lista_de_campeos.pop(int(ultimo_index))

    ############
    # agora com a lista organizada, vou jogar ela no arquivo,
    # mais nao antes de deixar ela do jeito que tem que ser
    # com virgula entre o nome e score e ponto e virgula entre os campeos
    ############

    lista_aux = []
    for Elementos_lista_com_2_itens in lista_de_campeos:
        string_aux = ""
        string_aux = str(Elementos_lista_com_2_itens[0]) + "," + Elementos_lista_com_2_itens[1]  # nome + , + score
        lista_aux.append(string_aux)
    # agr tenho uma lista com itens tipo str, vou ter que dar um join neles com ";"

    string_pronta_pra_jogar_no_arquivo = ""
    i = 0
    for elemento in lista_aux:
        if (i == 0):
            string_pronta_pra_jogar_no_arquivo = string_pronta_pra_jogar_no_arquivo + str(elemento)
        else:
            string_pronta_pra_jogar_no_arquivo = string_pronta_pra_jogar_no_arquivo + ";" + str(elemento)
        i = i + 1
    string_pronta_pra_jogar_no_arquivo = string_pronta_pra_jogar_no_arquivo + "\n"

    ####
    # agora eu jogo a string pronta no arquivo, substituindo oq estava la anteriormente
    ####

    try:
        a = open("quadro_de_campeoes_ludo.txt", 'w')
    except:
        print("DEBUG: Erro na hora de abrir o arquivo do quadro de campeos")
    else:
        a.write(string_pronta_pra_jogar_no_arquivo)

        # with open("quadro_de_campeoes_ludo.txt") as arquivo:
        #     try:
        #         arquivo.write(string_pronta_pra_jogar_no_arquivo)
        #         #sempre ter cuidado com o write pq ele apaga oq tem no arquivo antes de escrever nele
        #     except:
        #         print("DEBUG: problema na hora de tentar reescrever o arquivo quadro de campeos")
        #     else:
        #         print(">>>consegui reescrever o quandro de campeos")

    finally:
        a.close()


def Funcion_Sort(item):
    if "\n" in str(item[1]):
        item[1] = str(item[1]).replace("\n", "")
    return str(item[1])


def Funcion_Sort_Ordem_de_Jogada(jogador):
    return int(jogador.primeira_jogada)


def Cria_Objeto_Jogador(numero_de_jogadores):  # depois tem que criar um criador de BOTs maquina!!
    lista_de_jogadores = []
    n_jogador = numero_de_jogadores
    numero_do_jogador = 1
    while (numero_do_jogador <= int(n_jogador)):
        print(f"Vamos cadastrar o jogador {numero_do_jogador}, porfavor responda as perguntas a seguir:")

        # Pede o nome do jogador e ja verifica se existe um nome igual na lista de nomes de jogadores
        reescrever_nome = True  # comeca como true pra entrar no loop
        while (reescrever_nome):
            reescrever_nome = False
            '''e logo depois eu torno a variavel false, pra poder efetuar a verificaca0
            e eventualmente se o nome nao for igual a um ja existente o loop ja se encerra no primeiro ciclo'''

            nome_jogador = input("Digite o nome do jogador: ")
            while (len(nome_jogador) <= 2):
                nome_jogador = input("Digite um nome de jogador valido(minimo de 2 letras): ")

            for i in range(len(lista_de_jogadores)):
                if (nome_jogador == jogador.nome):
                    print("O nome digitado ja esta sendo utilizado, por favor tente novamente.")
                    reescrever_nome = True
            # fim do loop do nome

        # irei usar o mesmo metodo de verificacao pra cor
        reescrever_cor = True
        while (reescrever_cor):
            reescrever_cor = False

            cor_da_peca = input(f"Digite a cor da peca que voce deseja utilizar {infos_do_jogo.cores_peoes}: ")
            while (cor_da_peca not in infos_do_jogo.cores_peoes):
                print(f"Por favor digite uma cor que esteja listada em {infos_do_jogo.cores_peoes} :")
                cor_da_peca = input()

            for i in range(len(lista_de_jogadores)):
                if (cor_da_peca == lista_de_jogadores[i].cor):
                    print(
                        f"Esta cor ja esta sendo utilizada pelo jogador {lista_de_jogadores[i].nome}, por favor tente novamente:")
                    reescrever_cor = True
            # fim do loop de verificacao das cores

        jogador = Jogador(nome_jogador, cor_da_peca)

        lista_de_jogadores.append(jogador)

        numero_do_jogador = numero_do_jogador + 1

    lista_de_jogadores = Cria_bots_jogadores(lista_de_jogadores)
    return lista_de_jogadores


def Cria_bots_jogadores(lista_de_jogadores):
    if (len(lista_de_jogadores) != 4):
        numero_de_bots = 4 - len(lista_de_jogadores)
        bot_numero_tal = 1
        while (numero_de_bots > 0):
            bot_nome = ""
            bot_cor = ""
            lista_de_cores_sendo_usadas = []
            lista_de_cores_nao_usadas = []
            bot_nome = f"-BOT 0{bot_numero_tal}-"
            # para escolher a cor do bot teremos que ver as cores que ainda nao foram escolhidas
            for jogadores in lista_de_jogadores:
                lista_de_cores_sendo_usadas.append(jogadores.cor)

            for cores in infos_do_jogo.cores_peoes:
                if cores not in lista_de_cores_sendo_usadas:
                    lista_de_cores_nao_usadas.append(cores)

            bot_cor = lista_de_cores_nao_usadas[0]
            # cor escohida, sempre vai ser o primeiro item da lista de cores nao usadas
            # pq a lista toda ve que roda o while, se torna vazia denovo.

            # inserir infos nos bots
            bot_jogador = Jogador(bot_nome, bot_cor)
            bot_jogador.bot = True

            # e o mais importante add o bot a lista de jogadores
            lista_de_jogadores.append(bot_jogador)

            bot_numero_tal = bot_numero_tal + 1
            numero_de_bots = numero_de_bots - 1

    return lista_de_jogadores


def Partida_do_jogo(lista_de_jogadores):
    print("\nEntrou no jogo ...")  # depois tem que tirar isso daqui
    # variaveis para o loop da partida
    numero_do_rounds = -1
    jogando = True
    round_end = True
    vencedor = []
    debug = 0
    ninguem_venceu_todos_os_peos = True

    while (jogando):  # loop da partida
        # essa parte de codigo fica aqui pq eu quero mostrar o round(tabela) pos o cara ganhar, pra aparecer os numeros fechados do cara que ganhou.
        if (len(vencedor) > 0 and vencedor[0] == True):
            jogando = False
            print("-+-" * 26)
            print(
                f"O Jogador {vencedor[1]} ganhou a partida no round {vencedor[2]} com as pecas de cor {vencedor[3]}")
            print("-+-" * 26)
            print("\n")
            if (tem_direito_ao_quadro_dos_campeos(vencedor)):
                # faz a pergunta se ele quer que seu nome entre no quadro de campeos
                print("-+-" * 12)
                print("Parabens!, voce tem direito de colocar seu nome no quadro de campeos!!")
                resp_campeao = input("Deseja colocar seu nome no quadro de campeos?(S/N) ")
                while (resp_campeao.upper() not in "SN"):
                    resp_campeao = input("resposta invalida, tente novamente(S/N): ")
                if (resp_campeao.upper() == "S"):
                    # Reorganiza_quadro_de_campeoes(vencedor)
                    try:
                        Reorganiza_quadro_de_campeoes(vencedor)
                    except:
                        print("DEBUG: deu merda na hora da chamada do metodo Reorganiza_quadro_de_campeoes(vencedor) ")
                    else:
                        print(
                            "Pronto, agora voce ja pode acesssar o quadro de campeos no menu principal e seu nome estara la! =)\n")

                print("-+-" * 12)

        if (round_end and jogando):
            print(f"----- Round {numero_do_rounds} -----")
            for jogadoress in lista_de_jogadores:
                if(numero_do_rounds == 0):
                    print(
                        f"Player: {str(jogadoress.nome).title()};Cor da pesa: {jogadoress.cor}; Posicao no Percuso normal: {jogadoress.posicao_no_percurso_normal}/{infos_do_jogo.percurso_normal};Primeira_jogada_do_dado: {jogadoress.primeira_jogada};Peos conquistados: {jogadoress.peoes_que_terminaram_o_trageto}/{infos_do_jogo.numero_de_peoes}")
                elif (jogadoress.percurso_colorico == False):
                    print(
                        f"Player: {str(jogadoress.nome).title()};Cor da pesa: {jogadoress.cor}; Posicao no Percuso normal: {jogadoress.posicao_no_percurso_normal}/{infos_do_jogo.percurso_normal};Ultima_jogada_do_dado: {jogadoress.ultima_jogada_do_dado};Peos conquistados: {jogadoress.peoes_que_terminaram_o_trageto}/{infos_do_jogo.numero_de_peoes}")
                elif (jogadoress.peoes_na_zona_neutra == True):  # redundante
                    print(
                        f"Player: {str(jogadoress.nome).title()};Cor da pesa: {jogadoress.cor}; Posicao no Percuso normal: Esta tentando tirar um peao da zona neutra ;Ultima_jogada_do_dado: {jogadoress.ultima_jogada_do_dado};Peos conquistados: {jogadoress.peoes_que_terminaram_o_trageto}/{infos_do_jogo.numero_de_peoes}")
                else:
                    print(
                        f"Player: {str(jogadoress.nome).title()};Cor da pesa: {jogadoress.cor}; Posicao no Percurso colorido: {jogadoress.posicao_percurso_colorido}/{infos_do_jogo.percurso_colorido};Ultima_jogada_do_dado: {jogadoress.ultima_jogada_do_dado};Peos conquistados: {jogadoress.peoes_que_terminaram_o_trageto}/{infos_do_jogo.numero_de_peoes}")
            print("\n")

        if(numero_do_rounds == -1):
            for jogadoress in lista_de_jogadores:
                if(jogadoress.bot):
                    jogadoress.primeira_jogada = DADO_dos_BOTS()
                else:
                    jogadoress.primeira_jogada = DADO()

            lista_de_jogadores.sort(key=Funcion_Sort_Ordem_de_Jogada,reverse=True)
            #arruma a lista de jogadors ja na ordem de jogada, e o jogo continua

        # quando o jogo comeca de verdade
        if (numero_do_rounds >= 0):
            if (ninguem_venceu_todos_os_peos):
                for jogadoress in lista_de_jogadores:
                    if (jogadoress.peoes_que_terminaram_o_trageto == infos_do_jogo.numero_de_peoes):
                        # lista vencedor
                        vencedor = [True, jogadoress.nome, numero_do_rounds, jogadoress.cor, jogadoress.bot]
                        ninguem_venceu_todos_os_peos = False

                    # perte do nerf no dado dos bots
                    if (jogadoress.bot == True):
                        numero_do_dado = DADO_dos_BOTS()
                    else:
                        numero_do_dado = DADO()
                    jogadoress.ultima_jogada_do_dado = numero_do_dado
                    # parte nova escrita em 03/01/22
                    if (jogadoress.peoes_na_zona_neutra == True):  # redundante
                        if (int(numero_do_dado) == 6):
                            jogadoress.posicao_no_percurso_normal = 6
                            jogadoress.peoes_na_zona_neutra = False
                        elif (int(numero_do_dado) == 1):
                            jogadoress.posicao_no_percurso_normal = 1
                            jogadoress.peoes_na_zona_neutra = False
                    else:
                        if (jogadoress.posicao_no_percurso_normal >= 1):
                            # o jogador so passa dessa parte se ele conseguir tirar ou 1 ou 6, e tirar o peao da ona neutra
                            if (jogadoress.percurso_colorico == False):
                                jogadoress.posicao_no_percurso_normal = jogadoress.posicao_no_percurso_normal + numero_do_dado
                                if (jogadoress.posicao_no_percurso_normal >= infos_do_jogo.percurso_normal):
                                    jogadoress.posicao_no_percurso_normal = infos_do_jogo.percurso_normal
                                    jogadoress.percurso_colorico = True
                            elif (jogadoress.percurso_colorico == True):  # redundante mas bom de ler heuheu
                                jogadoress.posicao_percurso_colorido = jogadoress.posicao_percurso_colorido + numero_do_dado
                                if (jogadoress.posicao_percurso_colorido == infos_do_jogo.percurso_colorido):
                                    # vencedor = [True,jogadoress.nome,jogadoress.cor]
                                    jogadoress.peoes_que_terminaram_o_trageto = jogadoress.peoes_que_terminaram_o_trageto + 1
                                    jogadoress.percurso_colorico = False
                                    jogadoress.peoes_na_zona_neutra = True
                                    jogadoress.posicao_no_percurso_normal = 0
                                    jogadoress.posicao_percurso_colorido = 0
                                else:
                                    if (jogadoress.posicao_percurso_colorido < infos_do_jogo.percurso_colorido):
                                        pass
                                    elif (jogadoress.posicao_percurso_colorido > infos_do_jogo.percurso_colorido):
                                        diferenca = jogadoress.posicao_percurso_colorido - infos_do_jogo.percurso_colorido
                                        jogadoress.posicao_percurso_colorido = infos_do_jogo.percurso_colorido - diferenca

        numero_do_rounds = numero_do_rounds + 1
        debug = debug + 1


def DADO():
    if(infos_do_jogo.hardocore):
        numero_aleatorio = random.randint(1, 5)
    else:
        numero_aleatorio = random.randint(1, 6)

    return numero_aleatorio


def DADO_dos_BOTS():
    # os bots estavam ganhando muitas partidas, entao pra facilitar eu vou dar uma nerfada nos bots
    numero_aleatorio = 99
    if(int(infos_do_jogo.dificuldade_bots) == 1):
        numero_aleatorio = random.randint(1, 4)
    elif (int(infos_do_jogo.dificuldade_bots) == 2):
        numero_aleatorio = random.randint(1, 5)
    elif (int(infos_do_jogo.dificuldade_bots) == 3):
        numero_aleatorio = random.randint(1, 6)

    if(numero_aleatorio == 99):
        print("Debug no dado dos bots")
        return 999
    else:
        return numero_aleatorio


################ Main ####################
if (__name__ == "__main__"):
    infos_do_jogo = Infos_do_Jogo()  # instancio o objeto para poder usar os recursos que estao dentro dele.

    # Mensagem Inicial
    print()
    print("~" * 35)
    print(f"    Bem vindo ao jogo de Ludo!")
    print("~" * 35)
    while (True):
        Menu1()
        resposta_1 = input()
        while resposta_1 not in "1234":
            resposta_1 = input("Entrada invalida, tente novamente:")

        ###OPCOES DO MENU 1:###
        if (int(resposta_1) == 1):
            # inicia um novo jogo
            print("\n---Novo Jogo---")

            numero_de_jogadores = input("Quantos players humanos iram jogar?")  # melhorar essa pergunta ai que ta feio
            while (numero_de_jogadores not in "1234"):
                numero_de_jogadores = input("Porfavor digite um numero inteiro de 1 a 4:")
            if(int(numero_de_jogadores) < 4):
                Menu_dificildade_dos_bots()
                resposta_menu_dificuldade_bots = input("Digite a opcao escolhida: ")
                while resposta_menu_dificuldade_bots not in "1234":
                    resposta_menu_dificuldade_bots = input("Digite uma opcao valida(1 a 4): ")
                if(resposta_menu_dificuldade_bots == 4):
                    infos_do_jogo.hardocore = True
                    infos_do_jogo.dificuldade_bots = 3
                else:
                    infos_do_jogo.dificuldade_bots = resposta_menu_dificuldade_bots
            print("\n")

            # crio os objetos necessarios para a partida
            lista_de_jogadores = Cria_Objeto_Jogador(numero_de_jogadores)
            # inicio um novo jogo com a lista de objetos jogadores a criada

            ### inicia-se uma nova PARTIDA de Ludo ####
            Partida_do_jogo(lista_de_jogadores)


        # regras
        elif (int(resposta_1) == 2):
            Regras()

        # tabela dos campeos
        elif (int(resposta_1) == 3):
            Mostra_tabela_de_Campeos()

        # sair do programa
        elif (int(resposta_1) == 4):
            Sair = input("Voce deseja realmente sair?(S/N)")
            while Sair.upper() not in "SN":
                Sair = input("entrada invalida, tente novamente(S/N):")
            if (Sair.upper() == "S"):
                print("Encerrando o programa...")
                break
            else:
                pass