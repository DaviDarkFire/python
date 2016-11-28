#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pips
import volca_alternativo as volca
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time

def gera_graficos(od_volca, od_pips):    
    dias_volca = []
    valores_volca = []
    dias_pips = []
    valores_pips = []
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
            

    hfmt = mdates.DateFormatter('%d/%m/%Y')

    fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(hfmt)
    # ax.legend(loc='best', fancybox=True, framealpha=0.5)
    # ax.set_title('fancy, transparent legends')

    plt.plot(dias_volca, valores_volca,'b-',label='volca')
    plt.plot(dias_pips, valores_pips,'g-',label='pips')
    plt.legend(loc='upper right')

    plt.title("Data vs Valor")
    plt.xlabel("Data")
    plt.ylabel("Valor")

    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)    
    plt.show()


od_volca, u, v = volca.main()
od_pips, u, v = pips.main()
gera_graficos(od_volca, od_pips)
