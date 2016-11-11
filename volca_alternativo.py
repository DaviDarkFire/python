#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
from operator import itemgetter


def slide(W_valor,W_data,w_valor,w_data,w_mod,data,valor,flag):
	if(flag == 1):
		for i in range(w_mod):
			w_valor[i] = W_valor[i]
			w_data[i] = W_data[i]
	else:
		w_valor.popleft()
		w_data.popleft()
		w_valor.append(valor)
		w_data.append(data)

def iprice_max(w):		#função que retorna o endereço/dia do maior ponto
    maior = w[0]
    indice_maior = 0
    for i, val in enumerate(w):
        if w[i] > maior:
            indice_maior = i
            maior = val
    return indice_maior


def iprice_min(w):				#função que retorna o endereço/dia do menor ponto
	menor = w[0]
	indice_menor = 0
	for i, val in enumerate(w):
		if w[i] < menor:
			indice_menor = i
			menor = val
	return indice_menor

def trataValores(valores):
    return int(valores[0]), float(valores[1])

#Main
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

w_mod = 2                 #le o |w|
p = 1                     #le o p
w_data = []
w_valor = []
w_data = collections.deque(w_data)
w_valor = collections.deque(w_valor)
v_max = []                #cria o dicionario v_max
v_min = []                #cria o dicionario v_min
limit = w_mod-w_mod*p     #inicializa a variável limit

for i in W:						#inicializa os dicionários v_max, v_min, v_class
	v_max.append(0)
	v_min.append(0)


flag = 1
i = 0
for i, data in enumerate(W_data): #laço que vai levando a janela w e votando nos pontos de máximo e mínimo, alterar
	valor = W_valor[i]
	slide(W_data,W_valor,w_data,w_valor,w_mod,data,valor,flag)
	flag = 0
	v_max[iprice_max(w)] = v_max[iprice_max(w)]+1
	v_min[iprice_min(w)] = v_min[iprice_min(w)]+1
	i = i + 1


# s = {}
# od = {}
# v_max = collections.OrderedDict(sorted(v_max.items(), key=itemgetter(1), reverse=True)) #ordena o dicionario v_max pelos valores
# v_min = collections.OrderedDict(sorted(v_min.items(), key=itemgetter(1), reverse=True)) #ordena o dicionario v_min pelos valores

# l = 0
# for i in v_min:
# 	if (l < w_mod/2):
# 		od[i] = v_min[i]
# 		l += 1
# 	else:
# 		break
# l = 0
# for i in v_max:
# 	if (l < w_mod/2):
# 		od[i] = v_max[i]
# 		l += 1
# 	else:
# 		break

# od = collections.OrderedDict(sorted(od.items())) #ordena os valores pelo índice

# for i in od:
# 	od[i] = W[i]


# dias = []
# valores = []
# j = 0
# for i in od:
#     a = mdates.datestr2num(str(i))
#     dias.append(j)
#     dias[j] = mdates.num2date(a)
#     #print dias[j]
#     valores.append(j)
#     valores[j] = od[i]
#     j = j+1


# hfmt = mdates.DateFormatter('%d/%m/%Y')

# fig, ax = plt.subplots()

# ax.xaxis.set_major_formatter(hfmt)

# plt.plot_date(x=dias, y=valores, fmt="o-")

# plt.title("Data vs Valor")
# plt.xlabel("Data")
# plt.ylabel("Valor")

# plt.xticks(rotation=60)
# plt.tight_layout()
# plt.grid(True)
# print time.time() - start_time
# plt.show()

# f.close()#fecha o arquivo de entrada
