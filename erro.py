#!/usr/bin/env python
# -*- coding: utf-8 -*-
import volca_alternativo

def calc_reta(x1,y1,x2,y2): #função que calcula reta que liga os dois pontos mais próximos da simplificação
	m = (float(y2-y1))/(float(x2-x1))
	a = -m*float(x1)+float(y1)
	return m, a

def calc_erro(od):
    od_data = []
    od_valor = []
    for chave, valor in od.items():
        od_data.append(chave)
        od_valor.append(valor)

    print len(od_data)
    for i in range(0,len(od_data)):
    	print i, od_data[i]
                        

calc_erro(volca_alternativo.main())


