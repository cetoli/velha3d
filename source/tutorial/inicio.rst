.. Kwarwp documentation master file, created by
   sphinx-quickstart on Mon Jul 27 10:30:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Programa Inicial
================

Neste programa vamos fazer uma versão bem simplificada do jogo da velha.

.. note::
  a ideia é usar os recursos mais simples da linguagem.
    

Atribuição Múltipla
-------------------

Vamos criar comandos diretamente no corpo do módulo.

.. code:: python

  casa_0, casa_1, casa_2 = None, None, None
  """Primeira linha do tabuleiro"""
  casa_3, casa_4, casa_5 = None, None, None
  """Segunda linha do tabuleiro"""

  casa_6, casa_7, casa_8 = None, None, None
  """Terceira linha do tabuleiro"""

.. note::
  O nomes **casa_0**, **casa_1** e **casa_2** foram atribuídos com os valores 
  **None, None, None** usando um atribuição múltipla. Tudo foi feito em um única linha de código.
  A atribuição múltipla pega o primero nome do lado esquerdo do **=** e atribui o valor do primeiro item
  do lado direito do **=** e assim por diante.
    

Formatação de String
--------------------

Vamos usar uma string formatada dinamicamente para apresentar o estado atual do tabuleiro.

.. code:: python

  jogador = "x"
  """O jogador com a peça x começa"""

  for turno in range(9):

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

.. note::
  O nome **tabuleiro** foi atribuído com uma string que se espalha por múltiplas linhas.
  Para isso englobamos o texto com três aspas: **"""<o texto>"""**.
  Este texto contêm vários pares de chaves: **{}**. Estas chaves são usadas pela operação de formatação
  dinâmica **.format()** Toda vez que a operação encontra um par de chaves no texto ela substitui as chaves
  pelo próximo valor da lista de argumentos do **format()**.
  

.. note::
  Um outro truque de Python que foi usado é o curto circuito. Em uma expressão lógica,
  o Python para de avaliar assim que descobre o resultado da expressão. Cada um do argumentos
  da operação format é uma expressão lógica da forma **a or b**. Basta que **a** seja verdadeiro
  que se saiba o resultado da operação, pois verdadeiro ou qualquer coisa retorna verdadeiro.
  As casas foram todas inicializadas com **None**, que no Python é equivalente a falso.
  O truque usado escreve no tabuleiro o número da casa caso o valor corrente seja **None**.
  Se a casa já estiver preenchida, o curto circuito entra em ação e a expressão retorna o
  valor da casa, ou seja, **o** ou **x**.

    

Input e Teste com if, elif
--------------------------

O nome jogada vai receber o número que identifica a casa que se pretende jogar.
A sequência de if e elif testa o número recebido para ver qual casa foi escolhida.
A casa escolhida é atribuída com o símbolo do jogador corrente (**o** ou **x**).
A próxima jogada será do outro jogador, isto é se o jogador atual é o **x** será
a vez do jogador **o**, senão a vez tinha sido do **o** então é a vez do **x**.

.. code:: python

      jogada = str(input(tabuleiro))
      if jogada == "0": casa_0 = jogador
      elif jogada == "1": casa_1 = jogador
      elif jogada == "2": casa_2 = jogador
      elif jogada == "3": casa_3 = jogador
      elif jogada == "4": casa_4 = jogador
      elif jogada == "5": casa_5 = jogador
      elif jogada == "6": casa_6 = jogador
      elif jogada == "7": casa_7 = jogador
      elif jogada == "8": casa_8 = jogador
      jogador = "o" if jogador == "x" else "x"
  

Tela Gerada
------------

.. image:: ../_static/console_simples.png
   :height: 200
   :width: 200
   :scale: 50
   :alt: Tela inicial do Jogo da Velha
   :align: center

