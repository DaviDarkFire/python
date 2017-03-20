#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
import heapq
import operator

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


    w_data = []
    w_valor = []
    #w_data = collections.deque(w_data)
    #w_valor = collections.deque(w_valor)



    od = collections.OrderedDict(sorted(od.items()))
    temp = time.time() - start_time
    print "TEMPO ZIGZAG:",temp

    f.close() #fecha o arquivo

    return od, W_data, W_valor, temp
