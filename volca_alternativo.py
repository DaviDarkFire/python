#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time


def slide(W_data,W_valor,w_data,w_valor,w_mod,data,valor,flag):
	if(flag == 1):
		for i in range(w_mod):
			w_valor.append(W_valor[i])
			w_data.append(W_data[i])
	else:
		w_valor.popleft()
		w_data.popleft()
		w_valor.append(valor)
		w_data.append(data)

def iprice_max(w_valor,w_data):		#função que retorna o endereço/dia do maior ponto
    maior = w_valor[0]
    indice_maior = 0
    for i, val in enumerate(w_valor):
        if w_valor[i] > maior:
            indice_maior = i
            maior = val
    return indice_maior


def iprice_min(w_valor,w_data):				#função que retorna o endereço/dia do menor ponto
	menor = w_valor[0]
	indice_menor = 0
	for i, val in enumerate(w_valor):
		if w_valor[i] < menor:
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

w_mod = 50                 #le o |w|
p = 1                     #le o p
w_data = []
w_valor = []
w_data = collections.deque(w_data)
w_valor = collections.deque(w_valor)
v_max = []                #cria o dicionario v_max
v_min = []                #cria o dicionario v_min
limit = w_mod-w_mod*p     #inicializa a variável limit

for i in W_data:						#inicializa os dicionários v_max, v_min, v_class
	v_max.append(0)
	v_min.append(0)


flag = 1
tamanho = len(W_data)-w_mod+1
for i, data in enumerate(W_data[:tamanho]): #laço que vai levando a janela w e votando nos pontos de máximo e mínimo, alterar
	valor = W_valor[i]
	slide(W_data,W_valor,w_data,w_valor,w_mod,data,valor,flag)
	flag = 0

	i_M = iprice_max(w_valor,w_data)+i
	i_m = iprice_min(w_valor,w_data)+i

	v_max[i_M] = v_max[i_M]+1
	v_min[i_m] = v_min[i_m]+1

order_max = np.empty([len(W_data),3])
order_min = np.empty([len(W_data),3])

for i in range(len(W_data)):
	order_max[i][0] = W_data[i]
	order_min[i][0] = W_data[i]

	order_max[i][1] = W_valor[i]
	order_min[i][1] = W_valor[i]

	order_max[i][2] = v_max[i]
	order_min[i][2] = v_min[i]

order_max = np.sort(order, axis=-1, kind='quicksort', order=None)
order_min = np.sort(order, axis=-1, kind='quicksort', order=None)

tamanho_order = len(order_max)
tamanho_ir = len(order_max)-(w_mod/2)

od = {}

for i in xrange(tamanho_order,tamanho_ir,-1):







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
