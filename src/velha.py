from glow import *
_gs = glow('main')
cena = canvas()
cena.width = 400
cena.height = 400
TAM = (-1, 0, 1)
TABULEIRO = []
PECAS = []
print("oi")
pecas = [box, sphere] *14
cores = [color.red, color.blue] *14
class Casa:
    def __init__(self, x, y, z):
        self.e_casa = box(pos=(x*3, y*3, z*3), size=(2, 2, 2), opacity=0.2)
        self.peca = None

    def recebe(self, algo3d):
        self.peca = algo3d
        return algo3d

class Peca:
    def __init__(self, tipo_peca, x,y,z, cor):
        self.e_peca = tipo_peca(pos=(x*3, y*3, z*3), color=cor,  size=(1, 1, 1), opacity=0.6)


TABULEIRO = [Casa(coluna, linha, camada)
             for coluna in TAM for linha in TAM for camada in TAM]
cor = color.blue
#peca, cor = pecas.pop()
PECAS = [Peca(pecas.pop(), coluna, linha, camada, cores.pop())
             for coluna in TAM for linha in TAM for camada in TAM]
PECASCOLOCADAS = [casa.recebe(peca) for casa, peca in zip(TABULEIRO,PECAS)]







