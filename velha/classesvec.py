# -*- coding : utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo para ensino de programação Python.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.11.b0
        Usando uma classe para Casa e uma para Velha.

"""
class Casa():
    """Representa uma casa do jogo da velha.
    
    Referências:
    
    casa
     Célula contendo o marcador do jogador.
    """     

    def __init__(self):
        self.casa = None
        """Uma casa vazia contendo None.
        """
        
    def joga(self, jogador):
        """Preecha a casa com o maracdor de um jogador.
        
        :param jogador: Marcador do jogador para preencher a casa.
        
        """
        self.casa = jogador
        
    def mostra(self):
        """Retorna o marcador do jogador.
        
        :return: Marcador do jogador usado para preencher a casa.
        
        """
        return self.casa


class Velha():
    """Representa o jogo da velha.
    
    Referências:
    
    casa
     Lista contendo as casas do jogo.
     
    jogador
     Marcador do jogador com a vez corrente.
    """
    ESCOLHA = "Escolha uma casa do tabuleiro"
    """Frase para pedir uma jogada."""
    FINAL = "Situação final do tabuleiro"
    """Frase indicando o fim o do jogo."""
    TABULEIRO = """
        {}
        {} | {} | {}
        -----------
        {} | {} | {}
        -----------
        {} | {} | {}
        """   
    """Display mostrando a situação atual do tabuleiro."""

    def __init__(self):
        self.casa = [Casa() for _ in range(9)]
        """Usamos uma compressão de lista para criar nove instâncias da classe **Casa**.
        """

        self.jogador = "x"
        """O jogador com a peça x começa"""
        
    def joga(self):
        """Executa o joga da velha.
        
        Referências:
        
        jogada
         Índice da casa a ser preenchida.
        
        display_das_casas
         Apresentação do conteúdo de cada casa: o índice se vazia ou marcador se cheia.
        """

        while True:
            display_das_casas = [a_casa.mostra() or posicao for posicao, a_casa in enumerate(self.casa)]

            if all([marcador.mostra() for marcador in self.casa]):
                print(Velha.TABULEIRO.format(Velha.FINAL, *display_das_casas))
                """Mostra a situação final do tabuleiro."""
                break
            jogada = str(input(Velha.TABULEIRO.format(Velha.ESCOLHA, *display_das_casas)))
            """Mostra a situação atual do tabuleiro e pede a próxima jogada."""
            casa_escolhida = self.casa[int(jogada)].mostra()
            """Obtem a peça que está colocada na casa escolhida"""
            if casa_escolhida:
                """Se a casa escolhida já está ocupada volta a fazer a pergunta."""
                continue
            self.casa[int(jogada)].joga(self.jogador)
            """ Coloca a peça na posição pedida pela jogada."""
            self.jogador = "o" if self.jogador == "x" else "x"
            """Troca a vez para o outro jogador."""


if __name__ == '__main__':
    Velha().joga()