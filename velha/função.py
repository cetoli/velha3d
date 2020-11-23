# -*- coding : utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo para ensino de programação Python.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.11
        Usando uma função.

.. versionchanged::    20.11
        Melhorando a documentação da função.

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


def velha():
    """Executa o joga da velha.
    
    Referências:
    
    casa
     Lista contendo as casas do jogo.
     
    jogador
     Marcador do jogador com a vez corrente.
    
    jogada
     Índice da casa a ser preenchida.
    
    display_das_casas
     Apresentação do conteúdo de cada casa: o índice se vazia ou marcador se cheia.
    """
    casa = [None]*9
    """A operação de multiplicar com a lista contendo um **None**
    gera uma lista contendo nove posições contendo None.
    """

    jogador = "x"
    """O jogador com a peça x começa"""

    while True:
        display_das_casas = [a_casa or posicao for posicao, a_casa in enumerate(casa)]

        if all(casa):
            print(TABULEIRO.format(FINAL, *display_das_casas))
            """Mostra a situação final do tabuleiro."""
            break
        jogada = str(input(TABULEIRO.format(ESCOLHA, *display_das_casas)))
        """Mostra a situação atual do tabuleiro e pede a próxima jogada."""
        casa_escolhida = casa[int(jogada)]
        """Obtem a peça que está colocada na casa escolhida"""
        if casa_escolhida:
            """Se a casa escolhida já está ocupada volta a fazer a pergunta."""
            continue
        casa[int(jogada)] = jogador
        """ Coloca a peça na posição pedida pela jogada."""
        jogador = "o" if jogador == "x" else "x"
        """Troca a vez para o outro jogador."""


if __name__ == '__main__':
    velha()