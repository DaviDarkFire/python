#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pips
import volca_alternativo as volca
import zigzag
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def gera_graficos(od_volca, od_pips, od_zigzag, dataset_name):
    dias_volca = []
    valores_volca = []
    dias_pips = []
    valores_pips = []
    dias_zigzag = []
    valores_zigzag = []
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

    dias = []
    valores = []
    j = 0
    size = len(W_data)
    for i in range(0,size):
        a = mdates.datestr2num(str(W_data[i]))
        dias.append(j)
        dias[j] = mdates.num2date(a)
        valores.append(j)
        valores[j] = W_valor[i]
        j = j+1


    j = 0
    for i in od_volca:
        a = mdates.datestr2num(str(i))
        dias_volca.append(j)
        dias_volca[j] = mdates.num2date(a)
        #print dias[j]
        valores_volca.append(j)
        valores_volca[j] = od_volca[i]
        j = j+1


    j = 0
    for i in od_pips:
        a = mdates.datestr2num(str(i))
        dias_pips.append(j)
        dias_pips[j] = mdates.num2date(a)
        #print dias[j]
        valores_pips.append(j)
        valores_pips[j] = od_pips[i]
        j = j+1

    j = 0
    for i in od_zigzag:
        a = mdates.datestr2num(str(i))
        dias_zigzag.append(j)
        dias_zigzag[j] = mdates.num2date(a)
        #print dias[j]
        valores_zigzag.append(j)
        valores_zigzag[j] = od_zigzag[i]
        j = j+1


    hfmt = mdates.DateFormatter('%d/%m/%Y')

    fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(hfmt)
    # ax.legend(loc='best', fancybox=True, framealpha=0.5)
    # ax.set_title('fancy, transparent legends')

    plt.plot_date(x=dias, y=valores, fmt="k-", label='original')
    plt.plot(dias_volca, valores_volca,'b-',label='volca')
    plt.plot(dias_pips, valores_pips,'g-',label='pips')
    plt.plot(dias_zigzag, valores_zigzag,'r-',label='zigzag')
    #plt.plot(dias, valores,'b-',label='Sem simplificação')
    plt.legend(loc='upper right')

    plt.title("Data vs Valor")
    plt.xlabel("Data")
    plt.ylabel("Valor")

    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('saida/'+dataset_name+'/50pt_vs_original_comp',dpi=600)
