#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
import heapq
import operator


def trataValores(valores):
    return int(valores[0]), float(valores[1])

def gera_grafico(od):
    dias = []
    valores = []
    j = 0
    for i in od:
        a = mdates.datestr2num(str(i))
        dias.append(j)
        dias[j] = mdates.num2date(a)
        #print dias[j]
        valores.append(j)
        valores[j] = od[i]
        j = j+1

    hfmt = mdates.DateFormatter('%d/%m/%Y')

    fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(hfmt)

    plt.plot_date(x=dias, y=valores, fmt="o-")

    plt.title("Data vs Valor")
    plt.xlabel("Data")
    plt.ylabel("Valor")

    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def main(percent, W_data, W_valor):
    start_time = time.time()
    #w_data = collections.deque(w_data)
    #w_valor = collections.deque(w_valor)
    w_data = []
    w_valor = []

    w_data.append(W_data[0]) #considera o maior valor como sendo o primeiro
    w_valor.append(W_valor[0]) #considera o maior valor como sendo o primeiro
    topo = False
    fundo = False
    indiceFundo = 0
    indiceTopo = 0
    indiceInicio = 0
    
    for i, val in enumerate(W_valor):
    
        if(W_valor[i] > W_valor[indiceTopo]):
        
            indiceTopo = i
            if((not fundo) and ((W_valor[indiceTopo] - W_valor[indiceFundo]) / W_valor[indiceFundo]) * 100 >= percent):
                w_data.append(W_data[indiceFundo])
                w_valor.append(W_valor[indiceFundo])
                topo = False
                fundo = True
                
            if(fundo):
                indiceFundo = indiceTopo
        else:
            if(W_valor[i] < W_valor[indiceFundo]):
                    
                indiceFundo = i
                if((not topo) and ((W_valor[indiceTopo] - W_valor[indiceFundo]) / W_valor[indiceFundo]) * 100 >= percent):
                    w_data.append(W_data[indiceTopo])
                    w_valor.append(W_valor[indiceTopo])
                    topo = True
                    fundo = False
                
                if(topo):
                    indiceTopo = indiceFundo

    #for i, val in enumerate(w_valor): ta printando os valores
    #    print w_data[i], ",", val

    od = {}
    for i, val in enumerate(w_valor):
        od[w_data[i]] = val

    od = collections.OrderedDict(sorted(od.items()))
    temp = time.time() - start_time
    print "TEMPO ZIGZAG:",temp
    #gera_grafico(od)

    
    #print len(od)
    return od, W_data, W_valor, temp

#main(4.5)
