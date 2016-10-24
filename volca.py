#!/usr/bin/env python
# -*- coding: utf-8 -*-

def slide(W,w,w_mod,j):			#o parâmetro flag indica se eu vou ter que preencher o w completamente, ou se vou precisar apenas adicionar um dia e excluir o primeiro
	keys_W = W.keys()			#faz uma lista com as chaves do W
	for i in keys_W[j:w_mod+j+1]:	#preenche  a janela w com os valores de W
		w[i] = W[i]
	return w    					#retorna a janela atualizada



def iprice_max(w):					#função que retorna o endereço/dia do maior ponto
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


with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
    for linha in f:
        linha = linha.strip()
        if linha:
            valores = linha.split(',')
            x,y = trataValores(valores)
            W[x] = y

w_mod = 10                #le o |w|
p =                       #le o p
w = {}					  #cria o dicionário w
v_max = {}                #cria o dicionario v_max
v_min = {}                #cria o dicionario v_min
v_class = {}              #cria o dicionario v_class
limit = w_mod-w_mod*p     #inicializa a variável limit

for i in W:						#inicializa os dicionários v_max, v_min, v_class
	v_max[i] = 0
	v_min[i] = 0
	v_class[i] = "do_nothing"


keys_W = W.keys()
i = 0
while i < len(keys_W)-w_mod:	                #laço que vai levando a janela w e votando nos pontos de máximo e mínimo, alterar
	slide(W,w,w_mod,i)
	v_max[iprice_max(w)] = v_max[iprice_max(w)]+1
	v_min[iprice_min(w)] = v_min[iprice_min(w)]+1
	i = i + 1


for i in v_max:					                    #preenche o dicionário v_class com as informações de compra e venda
    if v_max[i] > limit:
        v_class[i] = "sell"
    if v_min[i] > limit:
        v_class[i] = "buy"

for i in v_class:
	print v_class[i]


f.close()                                          #fecha o arquivo de entrada
