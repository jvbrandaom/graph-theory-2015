#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Nobusada, João Vitor Brandão e Pedro Padoveze'
""" A Task 4 é a resolução do Sudoku por coloração de Grafos.
"""

import networkx as nx

class Tabuleiro:
    """ A grid é uma lista de listas. Permite o acesso grid[x][y]
    """
    def __init__(self, lista):
        #Inicializa o grid inteiro com None
        self.grid = []
        for i in range(0,9):
            self.grid.append([])
            for j in range(0,9):
                self.grid[i].append(None)
        # Preenche o grid com o parâmetro lista
        for i in range(0, 81):
            if lista[i] != 0:
                self.grid[i/9][i%9] = lista[i]

    def verifica_local(self, valor, linha, coluna):
        """ Verifica se o número "valor" já se encontra no sub-quadrado 3x3 local e retorna uma lista com os valores
            possíveis
        """

        possiveis = [1,2,3,4,5,6,7,8,9]
        for i in range((coluna/3) * 3, ((coluna/3) * 3 + 3)):
            for j in range((linha/3) * 3, ((linha/3) * 3 + 3)):
                #print "i,j: ("+str(i)+","+str(j)+"); "+"grid[i][j] : "+str(self.grid[i][j])
                if self.grid[i][j] in possiveis:
                    possiveis.remove(self.grid[i][j])

        if valor not in possiveis:
            return []
        else:
            return possiveis

    def verifica_linha(self, valor, linha):
        """ Verifica se o número "valor" já existe na linha e retorna uma lista com os valores possíveis
        """

        possiveis = [1,2,3,4,5,6,7,8,9]
        for i in range(0,9):
            if self.grid[linha][i] in possiveis:
                possiveis.remove(self.grid[linha][i])

        if valor not in possiveis:
            return []
        else:
            return possiveis


    def verifica_coluna(self, valor, coluna):
        """ Verifica se o número "valor" já existe na coluna e retorna uma lista com os valores possíveis
        """
        possiveis = [1,2,3,4,5,6,7,8,9]
        for i in range(0,9):
            if self.grid[i][coluna] in possiveis:
                possiveis.remove(self.grid[i][coluna])

        if valor not in possiveis:
            return []
        else:
            return possiveis


    def verifica_tudo(self, valor, coord_x, coord_y):
        """ Realiza todas as verificações e retorna uma lista com a intersecção dos resultados de linha, coluna e
            ao redor
        """
        possiveis = [1,2,3,4,5,6,7,8,9]
        lista_linha = []
        lista_redor = []
        lista_coluna = []

        if self.verifica_linha(valor, coord_y) != []:
            lista_linha = self.verifica_linha(valor, coord_y)
            #print lista_linha
        if self.verifica_coluna(valor, coord_x) != []:
            lista_coluna = self.verifica_coluna(valor, coord_x)
            #print lista_coluna
        if self.verifica_local(valor, coord_x, coord_y) != []:
            lista_redor = self.verifica_local(valor, coord_x, coord_y)
            #print lista_redor

        lista_possiveis = [possivel for possivel in possiveis if possivel in lista_coluna and possivel in
                           lista_linha and possivel in lista_redor]
        if lista_possiveis == []:
            return False
        else:
            return lista_possiveis


if '__name__' == '__main__':
    # Abaixo temos um exemplo de um Sudoku não resolvido.
    sudoku = [9, 5, 0, 0, 0, 1, 0, 0, 8,
             0, 2, 1, 8, 9, 0, 6, 0, 0,
             3, 0, 0, 0, 4, 2, 1, 5, 9,
             2, 4, 0, 0, 7, 8, 0, 0, 1,
             1, 0, 9, 3, 2, 0, 0, 6, 5,
             8, 0, 0, 1, 0, 0, 0, 7, 2,
             4, 9, 0, 0, 1, 0, 5, 8, 0,
             6, 8, 2, 9, 0, 0, 0, 0, 4,
             0, 0, 0, 4, 8, 3, 0, 9, 6]
    t = Tabuleiro(sudoku)
    t.verifica_tudo(5, 4, 0)