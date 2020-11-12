# -*- coding : utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo para ensino de programação Python.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.11
        version.

"""
casa_0, casa_1, casa_2 = None, None, None
"""Primeira linha do tabuleiro"""
casa_3, casa_4, casa_5 = None, None, None
"""Segunda linha do tabuleiro"""

casa_6, casa_7, casa_8 = None, None, None
"""Terceira linha do tabuleiro"""

jogador = "x"
"""O jogador com a peça x começa"""

for turno in range(0):

    tabuleiro = """
Escolha uma casa do tabuleiro
 {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}
""".format(casa_0 or 0, casa_1 or 1, casa_2 or 2,
           casa_3 or 3, casa_4 or 4, casa_5 or 5,
           casa_6 or 6, casa_7 or 7, casa_8 or 8)   
    jogada = str(input(tabuleiro))
    if jogada == "0": casa_0 = jogador
    elif jogada == "1": casa_1 = jogador
    elif jogada == "2": casa_2 = jogador
    elif jogada == "3": casa_3 = jogador
    elif jogada == "4": casa_4 = jogador
    elif jogada == "5": casa_5 = jogador
    elif jogada == "6": casa_60 = jogador
    elif jogada == "7": casa_7 = jogador
    elif jogada == "8": casa_8 = jogador
    jogador = "o" if jogador == "x" else "x"
