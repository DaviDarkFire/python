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

def find_pips(W,w,x1,y1,x2,y2,count):
    x,y = calc_pip(W,x1,y1,x2,y2)
    w[x] = y

    print x
    print y
    print "\n"

    if (count == 0):
        return

    count = count-1
    find_pips(W,w,x1,y1,x,y,count)
    find_pips(W,w,x,y,x2,y2,count)

    return w

# Main
f = open("input.in", "r") #abre o arquivo de entradas
count = int(f.readline()) #le a quantidade de pips que se deseja
W = {1:1,2:20,3:-10,4:40,5:-90,6:60,7:70,8:80,9:-50,10:100}                    #cria o dicionario W
w = {}					  #cria o dicionário w
keys_W = W.keys()

w[keys_W[0]] = W[keys_W[0]]
w[keys_W[-1]] = W[keys_W[-1]]

find_pips(W,w,keys_W[0],W[keys_W[0]],keys_W[-1],W[keys_W[-1]],count/2)


f.close()
