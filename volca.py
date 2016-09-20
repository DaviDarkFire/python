#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def slide(W,w,w_mod,flag):			#o parâmetro flag indica se eu vou ter que preencher o w completamente, ou se vou precisar apenas adicionar um dia e excluir o primeiro
	if flag:						#se a flag == 1 significa que eu tenho que preencher toda janela w
		keys_W = W.keys()			#faz uma lista com as chaves do W
		for i in keys_W[:w_mod+1]:	#preenche  a janela w com os valores de W
			w[i] = W[i]		
	else:
		keys_w = w.keys()			#se a flag for 0, somente elimina-se a primeira posição e adciona-se uma nova chave no final da janela
		del w[keys_w[0]]
		w[keys_w[-1]+1] = W[keys_w[-1]+1]

	return w    					#retorna a janela atualizada



def iprice_max(w):					#função que retorna o endereço/dia do maior ponto	
	keys_w = w.keys()	
	maior = w[keys_w[0]]				
	for i in w:		
		if w[i] > maior:
			indice_maior = i
			maior = w[i]
	return indice_maior		


def iprice_min(w):				#função que retorna o endereço/dia do menor ponto		
	keys_w = w.keys()	
	menor = w[keys_w[0]]
	for i in w:
		if w[i] < menor:
			indice_menor = i
			menor = w[i]
	return indice_menor

f = open("input.in", "r") #abre o arquivo de entradas
w_mod = int(f.readline()) #le o |w|
p = int(f.readline())     #le o p
W = {}                    #cria o dicionario W
w = {}					  #cria o dicionário w	
v_max = {}                #cria o dicionario v_max
v_min = {}                #cria o dicionario v_min
v_class = {}              #cria o dicionario v_class
limit = w_mod-w_mod*p     #inicializa a variável limit

for i in W:						#inicializa os dicionários v_max, v_min, v_class
	v_max[i] = 0
	v_min[i] = 0
	v_class[i] = "do_nothing"

for linha in f:					#inicializa W com os valores de entrada
    pass

slide(W,w,w_mod,1)
for i in W:											#laço que vai levando a janela w e votando nos pontos de máximo e mínimo, alterar
	v_max[iprice_max(w)] = v_max[iprice_max(w)]+1
	v_min[iprice_min(w)] = v_min[iprice_min(w)]+1
	slide(W,w,w_mod,0)


for i in v_max:					                    #preenche o dicionário v_class com as informações de compra e venda
    if v_max[i] > limit:
        v_class[i] = "sell"
    if v_min[i] > limit:
        v_class[i] = "buy"


f.close()                                          #fecha o arquivo de entrada
