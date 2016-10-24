#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys
import collections

def distancia_vertical(x1,y1,x2,y2,x3,y3): #essa distância vertical retorna a distância do ponto analisado com relação
    # à reta que liga os pips adjacentes deste ponto, assim o quão maior for a distância vertical, maior vai ser
    #a importância daquele ponto
    dv = (y1+(y2-y1)*((x3-x1)/(x2-x1)))-y3 #conta que determina a distância vertical
    if (dv < 0): #faz o módulo do número
        dv = dv*(-1)
    return dv

def calc_pip(W,x1,y1,x2,y2): #função não usada
    keys_W = W.keys()
    i = keys_W.index(x1)
    j = keys_W.index(x2)
    dv = dv_aux = x_aux = y_aux = 0
    for k in keys_W[i:j+1]:
        dv_aux = distancia_vertical(x1,y1,x2,y2,k,W[k])
        if(dv_aux > dv):
            y_aux = W[k]
            dv = dv_aux
            x_aux = k
    return x_aux,y_aux

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


def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

# Main
W = {}
with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
    for linha in f:
        linha = linha.strip()
        if linha:
            valores = linha.split(',')
            x,y = trataValores(valores)
            W[x] = y


w = {}					  #cria o dicionário w

w = pip(W,10) #pede 10 pips a partir dos valores passados em W

od = collections.OrderedDict(sorted(w.items())) #ordena pelo índice os pips

for i in od: #mostra os pips na tela
    print i,",",od[i]

f.close() #fecha o arquivo
