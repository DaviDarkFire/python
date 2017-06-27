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
import math

def slide(W_data,W_valor,w_data,w_valor,w_mod,data,valor,flag): #função que move a janela pela time serie
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

def main(w_mod, W_data, W_valor):
    start_time = time.time()
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
    for i, data in enumerate(W_data[:tamanho]): #laço que vai levando a janela w e votando nos pontos de máximo e mínimo
        valor = W_valor[i]
        slide(W_data,W_valor,w_data,w_valor,w_mod,data,valor,flag)
        flag = 0

        i_M = iprice_max(w_valor,w_data)+i
        i_m = iprice_min(w_valor,w_data)+i

        v_max[i_M] = v_max[i_M]+1
        v_min[i_m] = v_min[i_m]+1

    temp_max = []
    temp_min = []

    for i, val in enumerate(v_max):
        if(val >= w_mod):
            temp_max.append(i)
        if(v_min[i] >= w_mod):
            temp_min.append(i)

    od = {}
    passo1 = int(math.ceil((len(temp_max)/w_mod)*2))
    passo2 = int(math.ceil((len(temp_max)/w_mod)*2))
    for i in range(0,len(temp_max), passo1):
        od[W_data[temp_max[i]]] = W_valor[temp_max[i]]

    for i in range(0,len(temp_min), passo2):
        od[W_data[temp_min[i]]] = W_valor[temp_min[i]]

    od = collections.OrderedDict(sorted(od.items()))
    temp = time.time() - start_time
    print "TEMPO VOLCA:",temp
    return od, W_data, W_valor, temp
