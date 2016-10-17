#!/usr/bin/env python
# -*- coding: utf-8 -*-

def distancia_vertical(x1,x2,x3,y1,y2,y3): #essa distância vertical retorna a distância do ponto analisado com relação
    # à reta que liga os pips adjacentes deste ponto, assim o quão maior for a distância vertical, maior vai ser
    #a importância daquele ponto
    dv = (y1+(y2-y1)*((x3-x1)/(x2-x1)))-y3 #conta que determina a distância vertical
    if (dv < 0): #faz o módulo do número
        dv = dv*(-1)
    return dv

def calc_pip(W,w,x1,y1,x2,y2,count): #tem que passar count dividido por 2
    keys_W = W.keys()
    i = keys_W.index(x1)
    j = keys_W.index(x2)

    if (count == 0): #condição de fim da recursão
        return count

    dv = 0
    dv_aux = 0
    x_aux = 0
    y_aux = 0
    for k in keys_W[i:j+1]:
        dv_aux = distancia_vertical(x1,x2,k,y1,y2,W[k])
        if(dv_aux > dv):
            x_aux = k
            y_aux = W[k]
            dv = dv_aux

    w[x_aux] = y_aux
    count = count-1
    calc_pip(W,w,x1,y1,x_aux,y_aux,count)
    calc_pip(W,w,x_aux,y_aux,x2,y2,count)
