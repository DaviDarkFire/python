#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

# Main
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


hfmt = mdates.DateFormatter('%d/%m/%Y')

fig, ax = plt.subplots()

ax.xaxis.set_major_formatter(hfmt)

plt.plot_date(x=dias, y=valores, fmt="b-")

plt.title("Data vs Valor")
plt.xlabel("Data")
plt.ylabel("Valor")

plt.xticks(rotation=60)
plt.tight_layout()
plt.grid(True)
plt.show()

f.close() #fecha o arquivo
