# -*- coding: utf-8 -*-
from glow import *
from __random import choice
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
        return algo3d

    def tipo_peca(self):
        #print("tipo_peca", self.peca.tipo if self.peca is not None else 0)
        return self.peca.tipo if self.peca else 0

    def clicou(self):
        coluna, linha, camada = self.pos  # aposição da peça vai ser a posição da casa
        #peca = Peca(pecas.pop(), coluna, linha, camada, cores.pop())  # cria uma peça aqui
        peca = TABULEIRO.joga(coluna, linha, camada)  # cria uma peça aqui
        #Casa.CASAS.pop(self.pos)  # remove esta da lista de casas para não ser clicada
        self.recebe(peca)  # avisa a casa que ela esta é a peça que está nela
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
    def __init__(self, cena):
        SP = SZ+1
        self.cena = cena
        self._casas = [Casa(coluna, linha, camada)
                 for coluna in TAM for linha in TAM for camada in TAM]
        self._pecas = [Peca(peca, 0, 0, 0, cores.pop()) for peca in pecas]
        self._marcadores = [box(pos=(0, 0, 0), color=color.yellow,
            size=(SP, SP, SP), opacity=0.3) for x in range(9)]
        print([casa.tipo_peca() for casa in Casa.CASAS.values()])
        self.inicia()

    def remove(self, casa):
        self.casas.remove(casa)

    def inicia(self, ev=0):
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
        if TABULEIRO:
            self.jogada()
        print([casa.tipo_peca() for casa in Casa.CASAS.values()])
        print([casa.tipo_peca() for casa in self.casas])

    def joga(self, x, y, z):
        return self.pecas.pop().move_e_mostra(x, y, z)

    def verifica_humano_ganha(self, casa_anterior):
        print(casa_anterior)
        def casas_ganhadoras(tira):
            tipo_tira = [Casa.CASAS[casa].tipo_peca() for casa in tira if isinstance(casa, tuple)]
            return tipo_tira == [1, 1, 0] or tipo_tira == [0, 1, 1] or tipo_tira == [1, 0, 1]
        tiras = [tira for tira in TIRASD[casa_anterior] if casas_ganhadoras(tira)]  # crie aqui um teste para saber se alguem venceu
        #print("testa_ganhou", tiras,  casas_ganhadoras(tiras))
        return tiras

    def verifica_robo_ganha(self):
        pass

    def jogada(self, casa_anterior=(0, 0, 0)):
        casa_da_jogada = choice(self.casas)  # choice(TABULEIRO)  # TABULEIRO[0]
        humano_ganha = self.verifica_humano_ganha(casa_anterior)
        if humano_ganha:
            casas = humano_ganha[0]
            print('humano_ganha:', humano_ganha, casas, "jogue aqui:", casas[2])
            # descobre qual casa está vazia
            casa_vazia = [Casa.CASAS[casa] for casa in casas if Casa.CASAS[casa].tipo_peca() == 0]
            print('humano_ganha:', humano_ganha, casas, "jogue aqui:", casa_vazia)

            casa_da_jogada = casa_vazia[0]

        #verifica_robo_ganha()
        self.remove(casa_da_jogada)
        casa_da_jogada.clicou()

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

    def clicou(self, event):
        cc = self.cena.mouse.pick().pos  # pega a posição do objeto clicado pelo mouse
        clicada = casa_clicada = (cc.x, cc.y, cc.z)  # cria uma tripla ordenada no espaço
        if casa_clicada in Casa.CASAS.keys():  # procura a tripla na coleção de casas
            casa_clicada = Casa.CASAS[casa_clicada]
            if casa_clicada in self.casas:
                self.remove(casa_clicada)
                casa_clicada.clicou()  # chama o clicou da casa escolhida
        self.jogada(clicada)

TABULEIRO = None
def main():
    global TABULEIRO
    print(TIRASD)

    _gs = glow('main')
    cena = canvas()
    cena.width = 400
    cena.height = 400

    #TABULEIRO = [Casa(coluna, linha, camada)
    #             for coluna in TAM for linha in TAM for camada in TAM]
    TABULEIRO = Tabuleiro(cena)
    cena.bind("mousedown", TABULEIRO.clica)
    TABULEIRO.jogada()
    return TABULEIRO

if __name__ == "__main__":
    main()
