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


def main(percent):
    start_time = time.time()

    W_data = []
    W_valor = []
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                x,y = trataValores(valores)
                W_data.append(x)

                W_valor.append(y)

    #w_data = collections.deque(w_data)
    #w_valor = collections.deque(w_valor)
    w_data = []
    w_valor = []

    w_data.append(W_data[0]) #considera o maior valor como sendo o primeiro
    w_valor.append(W_valor[0]) #considera o maior valor como sendo o primeiro
    high = W_valor[0]
    high_data = W_data[0]
    newHigh = (W_valor[0]*(percent/100))+W_valor[0]
    for i, val in enumerate(W_valor):
        if (val >= newHigh):
            high = val
            high_data = W_data[i]
            newHigh = (high*(percent/100))+high

        if (val <= high-(high*(percent/100))):
            w_data.append(high_data)
            w_valor.append(high)
            high = val
            high_data = W_data[i]
            newHigh = (high*(percent/100))+high

        if(i == len(W_valor)-1):
            w_data.append(high_data)
            w_valor.append(high)

    #for i, val in enumerate(w_valor): ta printando os valores
    #    print w_data[i], ",", val

    od = {}
    for i, val in enumerate(w_valor):
        od[w_data[i]] = val

    od = collections.OrderedDict(sorted(od.items()))
    temp = time.time() - start_time
    print "TEMPO ZIGZAG:",temp
    #gera_grafico(od)

    f.close() #fecha o arquivo
    #print len(od)
    return od, W_data, W_valor, temp

#main(4.5)
