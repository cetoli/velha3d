# -*- coding: utf-8 -*-
from glow import *
from __random import choice
from browser import doc
#from urllib import unquote
def unquote(txt):
    return txt.replace("&quot;", "\"")
TAM = (-1, 0, 1)
SP = 9
SZ = 4
print("oi")
# equação geral da reta y = a*x + b
# equação da nossa reta (b=0) y = a*x
# melhore o código de TIRAS para que teste mais possibilidades de ganhar
TIRAS = [[(x*SP, y*SP, z*SP) for x in TAM] for y in TAM for z in TAM]+[
        [(x*SP, y*SP, z*SP) for z in TAM] for x in TAM for y in TAM]+[
    [(x*SP, y*SP, z*SP) for y in TAM] for x in TAM for z in TAM]+[
        [(-9,9,z),(0,0,z),(9,-9,z)] for z in [-9,0,9]]+[
        [(9,9,z),(0,0,z),(-9,-9,z)] for z in [-9,0,9]]+[
        [(x,-9,9),(x,0,0),(x,9,-9)] for x in [-9,0,9]]+[
        [(x,9,9),(x,0,0),(x,-9,-9)] for x in [-9,0,9]]+[
        [(-9,y,9),(0,y,0),(9,y,-9)] for y in [-9,0,9]]+[
        [(9,y,9),(0,y,0),(-9,y,-9)] for y in [-9,0,9]]

TIRASD = {
    casa: [tiras for tiras in TIRAS if casa in tiras]
    for casa in [(x*SP, y*SP, z*SP) for x in TAM for y in TAM for z in TAM]}


pecas = [box, sphere] * 14
cores = [color.red, color.blue] * 14


class Casa:
    CASAS = {}  # esta coleção serve para achar o objeto casa a partir de sua posicão

    def __init__(self, x, y, z):
        self.pos = (x*SP, y*SP, z*SP)
        self.e_casa = sphere(pos=self.pos, size=(SZ, SZ, SZ), opacity=0.2)
        Casa.CASAS[self.pos] = self  # adiciona esta casa na coleção de casas
        self.peca = None

    def recebe(self, algo3d):
        self.peca = algo3d
        vencedores = self.testa_ganhou()
        if vencedores:
            print("ganhou")
            #self.pinta_vencedores(vencedores)
            TABULEIRO.ganhou(vencedores)
            return True
        return False

    def tipo_peca(self):
        #print("tipo_peca", self.peca.tipo if self.peca is not None else 0)
        return self.peca.tipo if self.peca else 0

    def clicou(self):
        coluna, linha, camada = self.pos  # aposição da peça vai ser a posição da casa
        TABULEIRO.registra_jogada_na_historia(self.pos)
        #peca = Peca(pecas.pop(), coluna, linha, camada, cores.pop())  # cria uma peça aqui
        peca = TABULEIRO.joga(coluna, linha, camada)  # cria uma peça aqui
        #Casa.CASAS.pop(self.pos)  # remove esta da lista de casas para não ser clicada
        return self.recebe(peca)  # avisa a casa que ela esta é a peça que está nela
        #print(self.pos)

    def testa_ganhou(self):
        def casas_ganhadoras(tira):
            tipo_tira = [Casa.CASAS[casa].tipo_peca() for casa in tira if isinstance(casa, tuple)]
            return tipo_tira == [1, 1, 1] or tipo_tira == [2, 2, 2]
        tiras = [tira for tira in TIRASD[self.pos] if casas_ganhadoras(tira)]  # crie aqui um teste para saber se alguem venceu
        #print("testa_ganhou", tiras,  casas_ganhadoras(tiras))
        return tiras


class Peca:
    def __init__(self, tipo_peca, x, y, z, cor):
        self.e_peca = tipo_peca(pos=(x, y, z), color=cor,  size=(SZ, SZ, SZ), opacity=0.6)
        self.tipo = 1 if tipo_peca == box else 2

    def esconde(self):
        self.e_peca.visible = False

    def move_e_mostra(self, x, y, z):
        self.e_peca.visible = True
        self.e_peca.pos = (x, y, z)
        return self


class Tabuleiro:
    # um dicionário que coleta movimentos ganhadores.
    # O valor de cada chave é uma lista de tuplas onde cada tupla é:
    # (número de vitórias com essa jogada, índice da jogada em Tabuleiro.CASAS)
    # a chave é uma string com a lista de jogadas até agora separadas por espaço em branco
    # exemplo: {'_':[(1, 1)],'_ 1':[],'_ 1 8':[(1, 18)],'_ 1 8 18 17':[(1, 26)]}
    HISTORY = {'_':[]}
    CASAS = []
    def __init__(self, cena):
        self.jogada_robo = (0, 0, 0)
        self.peca_robo = 2
        self.cena = cena
        self._casas = [Casa(coluna, linha, camada)
                 for coluna in TAM for linha in TAM for camada in TAM]
        Tabuleiro.CASAS = [(coluna*SP, linha*SP, camada*SP)
                 for coluna in TAM for linha in TAM for camada in TAM]
        self._pecas = [Peca(peca, 0, 0, 0, cores.pop()) for peca in pecas]
        SM = SZ+1
        self._marcadores = [box(pos=(0, 0, 0), color=color.yellow,
            size=(SM, SM, SM), opacity=0.3) for x in range(9)]
        #print([casa.tipo_peca() for casa in Casa.CASAS.values()])
        self.inicia()

    def registra_jogada_na_historia(self, jogada):
        #cria uma chave que é um texto com os indices das casas jogadas separadas por brancos
        self.jogadas += " %d" % Tabuleiro.CASAS.index(jogada)
        # recupera as vitórias na história referentes a estas jogadas, inicia com [] se não acha
        self.vitorias_nesta_jogada = Tabuleiro.HISTORY.setdefault(self.jogadas, [])  # {"0":0, "1":0, "2":0})

    def remove(self, casa):
        self.casas.remove(casa)

    def inicia(self, ev=0):
        print(Tabuleiro.HISTORY)
        self.jogadas = "_"
        self.vitorias_nesta_jogada = Tabuleiro.HISTORY["_"]
        self._clica = self.clicou
        self.casas = self._casas[:]
        self.pecas = self._pecas[:]
        self.marcadores = self._marcadores[:]
        for casa in self.casas:
            casa.peca = None
        for peca in self.pecas:
            peca.esconde()
        for marcador in self.marcadores:
            marcador.visible = False
        if TABULEIRO and self.peca_robo == 2:
            self.jogada()
        # alterna a vez de iniciar entre o humano e o robô
        self.peca_robo = 1 if self.peca_robo == 2 else 2
        #print([casa.tipo_peca() for casa in Casa.CASAS.values()])
        #print([casa.tipo_peca() for casa in self.casas])

    def joga(self, x, y, z):
        return self.pecas.pop().move_e_mostra(x, y, z)

    def verifica_alguem_ganha(self, casa_anterior, pc=1):
        def casas_ganhadoras(tira):
            tipo_tira = [Casa.CASAS[casa].tipo_peca() for casa in tira if isinstance(casa, tuple)]
            return tipo_tira == [pc, pc, 0] or tipo_tira == [0, pc, pc] or tipo_tira == [pc, 0, pc]
        tiras = [tira for tira in TIRASD[casa_anterior] if casas_ganhadoras(tira)]  # crie aqui um teste para saber se alguem venceu
        #print("testa_ganhou", tiras,  casas_ganhadoras(tiras))
        return tiras

    def jogada(self, casa_anterior=(0, 0, 0)):
        def casa_do_indice(ind):
            return Casa.CASAS[Tabuleiro.CASAS[ind]]
        casa_da_jogada = choice(self.casas)  # choice(TABULEIRO)  # TABULEIRO[0]
        alguem_ganha = self.verifica_alguem_ganha(self.jogada_robo,  1 if self.peca_robo == 2 else 2)
        if not alguem_ganha:
            alguem_ganha = self.verifica_alguem_ganha(casa_anterior, self.peca_robo)
        if alguem_ganha:
            casas = alguem_ganha[0]
            casa_vazia = [Casa.CASAS[casa] for casa in casas if Casa.CASAS[casa].tipo_peca() == 0]
            print('humano_ganha:', alguem_ganha, casas, "jogue aqui:", casa_vazia)

            casa_da_jogada = casa_vazia[0]
        # AI: consulta a hitória de vitórias para repetir um lance vitorioso
        if self.vitorias_nesta_jogada and choice(range(10)) >-1:
            # seleciona entre os palpites vitoriosos um que caia numa casa vazia
            palpite = [casa_do_indice(tentativa[1])
                for tentativa in self.vitorias_nesta_jogada
                if casa_do_indice(tentativa[1]) in self.casas]
            # se exite um palpite possível seleciona o primeiro da lista ordenada
            if palpite:
                casa_da_jogada = palpite[0]
        self.remove(casa_da_jogada)
        casa_da_jogada.clicou()
        self.jogada_robo = casa_da_jogada.pos
        return self.jogada_robo

    def clica(self, event):
        self._clica(event)

    def ganhou(self, vencedores):
        for vencedor in vencedores:
            for posicao in vencedor:
                print("box", posicao)
                marca = self.marcadores.pop()
                marca.pos = posicao
                marca.visible = True
        self._clica = self.inicia
        jogadas = self.jogadas.split()
        l = len(jogadas)-1
        #AI : cria uma lista de chaves que representam as jogadas que levaram à vitória
        ganhadoras = [(" ".join(jogadas[:l-i]), int(jogadas[l-i]))
            for i in range(0, len(jogadas), 2)
            if not '_' in jogadas[l-i]]
        print( ganhadoras, jogadas, "-%s-"%self.jogadas, jogadas[:-0])
        #AI : atualiza a história adicionando uma vitória a cada tupla de jogada da lista
        for chave, jogada in ganhadoras:
            # recupera o registro de vitórias representado por esta chave
            registros = Tabuleiro.HISTORY[chave]
            # acha a tupla cuja jogada é a jogada usada nesta vitória
            registro = [par for par in registros if jogada == par[1]]
            # remove esta tupla se existia, para que fique duplicada
            if registro:
                registros.remove(registro[0])
            # cria ou recupera a tupla vitoriosa
            ganhos, casa = registro[0] if registro else [0, int(jogada)]
            # cria um novo registro de vitórias ordenado do mais vitorioso para o menso
            novos = sorted(registros + [(ganhos+1, casa)])
            # evita um bug que existe na versão 2.1.3 do brython
            novos = novos if len(novos) ==1 else novos[::-1]
            # Atualiza a história com esta nova lista de jogadas vitoriosas
            Tabuleiro.HISTORY[chave] = novos
        print(Tabuleiro.HISTORY)

    def clicou(self, event):
        cc = self.cena.mouse.pick().pos  # pega a posição do objeto clicado pelo mouse
        clicada = casa_clicada = (cc.x, cc.y, cc.z)  # cria uma tripla ordenada no espaço
        if casa_clicada in Casa.CASAS.keys():  # procura a tripla na coleção de casas
            casa_clicada = Casa.CASAS[casa_clicada]
            if casa_clicada in self.casas:
                self.remove(casa_clicada)
                if casa_clicada.clicou():
                    return # chama o clicou da casa escolhida
        #registra_jogada_na_historia(clicada)
        self.jogada(clicada)

TABULEIRO = None
def main():
    global TABULEIRO

    _gs = glow('main')
    cena = canvas()
    cena.width = 400
    cena.height = 400
    print(unquote(doc["history"].text))

    #TABULEIRO = [Casa(coluna, linha, camada)
    #             for coluna in TAM for linha in TAM for camada in TAM]
    TABULEIRO = Tabuleiro(cena)
    cena.bind("mousedown", TABULEIRO.clica)
    TABULEIRO.jogada()
    return TABULEIRO

if __name__ == "__main__":
    main()
