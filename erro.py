#!/usr/bin/env python
# -*- coding: utf-8 -*-
import volca_alternativo as volca
import pips

def calc_reta(x1,y1,x2,y2): #função que calcula reta que liga os dois pontos mais próximos da simplificação
	m = (float(y2-y1))/(float(x2-x1))
	a = -m*float(x1)+float(y1)
	return m, a

def calc_erro(od, W_data, W_valor):
    od_data = []
    od_valor = []
    erro = 0
    for chave, valor in od.items():
        od_data.append(chave)
        od_valor.append(valor)
    
    for i in range(0,len(od_data)):
    	if(i < len(od_data)-1):

            j = W_data.index(od_data[i])
            k = W_data.index(od_data[i+1])
            m, a = calc_reta(od_data[i], od_valor[i], od_data[i+1], od_valor[i+1])

            for l, val in enumerate(W_data[j:k+1]):
            	y = val*m+a
            	erro = abs(W_valor[l]-y)+erro
    return erro

od, W_data, W_valor = pips.main()
print "ERRO PIPS:", calc_erro(od, W_data, W_valor)
od, W_data, W_valor = volca.main()
print "ERRO VOLCA:", calc_erro(od, W_data, W_valor)


