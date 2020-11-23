.. Velha3D documentation master file, created by
   sphinx-quickstart on Mon Nov 23 10:30:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Usando Listas
================

Neste programa vamos melhorar um pouco, usando uma função para encapsular o código e usar o objeto lista.

.. note::
  A lista é um objeto já existente no Python. Vamos usar as capacidades deste objeto para melhorar
  a estrutura do nosso programa.
    

Criando uma função
-------------------

Vamos criar uma função velha para encapsular o código.

.. code:: python

    ESCOLHA = "Escolha uma casa do tabuleiro"
    FINAL = "Situação final do tabuleiro"
    TABULEIRO = """
        {}
        {} | {} | {}
        -----------
        {} | {} | {}
        -----------
        {} | {} | {}
        """   

    def velha():
        """AI is creating summary for velha
        """
        casa = [None]*9
        """A operação de multiplicar com a lista contendo um **None**
        gera uma lista contendo nove posições contendo None.
        """

        jogador = "x"
        """O jogador com a peça x começa"""

        while True:
            display_das_casas = [a_casa or posicao for posicao, a_casa in enumerate(casa)]    

.. note::
  Estamos usando aqui uma compreensão de listas (*list comprehension*) para gerar a lista
  de display de casas. Também estamos usando a função **enumerate ()** para que cada item da lista
  gere uma tupla contendo a posição corrente na lista e o conteúdo do item. Nesta compreensão
  aplicamos o curto circuito (*a_casa or posicao*) a cada item da lista para que faça o display
  mostrar o índice da casa quando a casa estiver vazia.

All, Break e Continue
---------------------

A função **all ()** testa cada uma das posições de uma lista para saber se todas são verdadeiras.
nós usamos um loop infinito com *while True* e vamos parar este loop somente quando todas as
posições do tabuleiro forem preenchidas. Ao usarmos a função all ela vai acusar quando não
houver nenhuma casa com None e então podemos usar o break para terminar o loop.

Caso o jogador tente ocupar uma casa já preenchida o valor de **casa_escolhida** vai retornar
verdadeiro. Usamos então o **continue** para que se retorne ao início do loop para pedir que
o jogador escolha outra casa.

.. code:: python

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

 
Tela Gerada
------------

.. image:: ../_static/console_simples.png
   :height: 200
   :width: 200
   :scale: 50
   :alt: Tela inicial do Jogo da Velha
   :align: center

