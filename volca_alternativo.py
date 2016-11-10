#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
import sys
from operator import itemgetter


def load():
		t = csv.reader(open(sys.argv[1]), delimiter = ',')
		v = []
		for row in t:
			v.append(row)
			v[][]			

		v.pop(0)
		dataset = None
		dataset = np.matrix(v)
		print dataset		
		return dataset


def slide(W,keys_W,w,keys_w,w_mod,j,flag):
	if(flag == 1):
		l = 0
		for i in keys_W:
			if(l == w_mod):
				break
			w[i] = W[i]			
			l = l+1
	else:
		del w[w.keys()[0]]
		w[j] = W[j]
		#w = collections.OrderedDict(sorted(w.items()))
		#print w
		#print "\n"



def iprice_max(w):		#função que retorna o endereço/dia do maior ponto
    keys_w = w.keys()
    maior = w[keys_w[0]]
    indice_maior = keys_w[0]
    for i in w:
        if w[i] > maior:
            indice_maior = i
            maior = w[i]
    return indice_maior


def iprice_min(w):				#função que retorna o endereço/dia do menor ponto
	keys_w = w.keys()
	menor = w[keys_w[0]]
	indice_menor = keys_w[0]
	for i in w:
		if w[i] < menor:
			indice_menor = i
			menor = w[i]
	return indice_menor

def trataValores(valores):
    return int(valores[0]), float(valores[1])

#Main
start_time = time.time()
W = {}
with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
    for linha in f:
        linha = linha.strip()
        if linha:
            valores = linha.split(',')
            x,y = trataValores(valores)
            W[x] = y

w_mod = 2                 #le o |w|
p = 1                     #le o p
w = {}					  #cria o dicionário w
v_max = {}                #cria o dicionario v_max
v_min = {}                #cria o dicionario v_min
v_class = {}              #cria o dicionario v_class
limit = w_mod-w_mod*p     #inicializa a variável limit

load()

# for i in W:						#inicializa os dicionários v_max, v_min, v_class
# 	v_max[i] = 0
# 	v_min[i] = 0
# 	v_class[i] = "do_nothing"
# 	print i, W[i]


# keys_W = W.keys()
# keys_W.sort()
# flag = 1
# i = 0
# for i in W:
# 	keys_w = w.keys()	                #laço que vai levando a janela w e votando nos pontos de máximo e mínimo, alterar	
# 	slide(W,keys_W,w,keys_w,w_mod,i,flag)
# 	flag = 0
# 	v_max[iprice_max(w)] = v_max[iprice_max(w)]+1
# 	v_min[iprice_min(w)] = v_min[iprice_min(w)]+1
# 	i = i + 1


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
