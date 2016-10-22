#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def distancia_vertical(x1,x2,x3,y1,y2,y3): #essa distância vertical retorna a distância do ponto analisado com relação
    # à reta que liga os pips adjacentes deste ponto, assim o quão maior for a distância vertical, maior vai ser
    #a importância daquele ponto
    dv = (y1+(y2-y1)*((x3-x1)/(x2-x1)))-y3 #conta que determina a distância vertical
    if (dv < 0): #faz o módulo do número
        dv = dv*(-1)
    return dv

def calc_pip(W,x1,y1,x2,y2): #tem que passar count dividido por 2
    keys_W = W.keys()
    i = keys_W.index(x1)
    j = keys_W.index(x2)
    dv = dv_aux = x_aux = y_aux = 0
    for k in keys_W[i:j+1]:
        dv_aux = distancia_vertical(x1,x2,k,y1,y2,W[k])
        if(dv_aux > dv):
            y_aux = W[k]
            dv = dv_aux
            x_aux = k
    return x_aux,y_aux

def pip(W, count): # tentativa com o código do github
    w = {}

    for chave in W.keys():
        w[chave] = W[chave]
        if (len(w) <= count):
            continue

        miniv = sys.maxsize
        minij = 0

        keys_w = w.keys()
        for j in w[1:-1]:
            
            d = distancia_vertical(ret[j - 1], ret[j], ret[j + 1]) #alterar
            if d < miniv:
                miniv = d
                minij = j

        del w[minij]

    return w

def trataValores(valores):
    aux = valores[0].split(" ")
    val = aux[0]+aux[1]

    return float(val), float(valores[1])

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
keys_W = W.keys()

for i in w:
    print i,w[i]

f.close()
