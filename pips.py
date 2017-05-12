#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys
import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time

def distancia_vertical(x1,y1,x2,y2,x3,y3): #essa distância vertical retorna a distância do ponto analisado com relação
    # à reta que liga os pips adjacentes deste ponto, assim o quão maior for a distância vertical, maior vai ser
    #a importância daquele ponto
    dv = (y1+(y2-y1)*((x3-x1)/(x2-x1)))-y3 #conta que determina a distância vertical
    if (dv < 0): #faz o módulo do número
        dv = dv*(-1)
    return dv

def pip(W, count): #função que calcula a quantidade de pips dada por count
    w = {}
    for chave in W.keys():
        w[chave] = W[chave]
        if (len(w) <= count):
            continue
            
        miniv = sys.maxsize
        minij = 0
        keys_w = w.keys()
        ultimo = keys_w[-1]
        for j, val in enumerate(keys_w):
            if(j != 0 and val != ultimo):
                x1 = keys_w[j-1] #to acessando uma posição na lista, essa posição da lista contém uma chave de um dicionário
                y1 = w[keys_w[j-1]] #to usando a chave desse dicionário pra acessar o elemento que eu quero do dicionário
                x2 = keys_w[j+1] #que locuuuuuuuuuura jão
                y2 = w[keys_w[j+1]]
                x3 = val
                y3 = w[val]
                d = distancia_vertical(x1,y1,x2,y2,x3,y3) #alterar
                if (d < miniv):
                    miniv = d
                    minij = j
            else:
                continue
        del w[keys_w[minij]]
    return w

def main(w_mod, W, W_data, W_valor):
    start_time = time.time()
    w = {}					  #cria o dicionário w
    w = pip(W,w_mod) #pede 50 pips a partir dos valores passados em W
    od = collections.OrderedDict(sorted(w.items())) #ordena pelo índice os pips
    temp = time.time() - start_time
    print "TEMPO PIPS:",temp
    return od, W_data, W_valor, temp
