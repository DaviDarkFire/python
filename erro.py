#!/usr/bin/env python
# -*- coding: utf-8 -*-
import volca_alternativo as volca
import pips

def calc_reta(x1,y1,x2,y2): #função que calcula reta que liga os dois pontos mais próximos da simplificação
	m = (float(y2-y1))/(float(x2-x1))
	a = -m*float(x1)+float(y1)
	return m, a

def calc_erro(od, W_data, W_valor): #sabendo agora a equação da reta podemos gerar pontos sobre e assim calcular o erro através da diferença
    od_data = []
    od_valor = []
    erro = 0
    for chave, valor in od.items(): #passa o valor do dicionário ṕara listas para que a manipulação dos dados fique mais fácil
        od_data.append(chave)
        od_valor.append(valor)

    for i in range(0,len(od_data)): #percorre a lista das datas após a simplificação
    	if(i < len(od_data)-1): #a verificação serve para não termos erros de indice quando fizermos conta mais a frente com i+1

            j = W_data.index(od_data[i])
            k = W_data.index(od_data[i+1])
            m, a = calc_reta(od_data[i], od_valor[i], od_data[i+1], od_valor[i+1]) #calcula os coeficientes angulares e lineares da reta m e a respectivamente

            for l, val in enumerate(W_data[j:k+1]): #calcula o ponto sobre a reta e subtrai do ponto original
            	y = val*m+a
            	erro = abs(W_valor[l+j]-y)+erro
    return erro
def main(w_mod):
    #retorno dos valores
    temp_pips = 0
    temp_volca = 0
    od, W_data, W_valor, temp_pips = pips.main(w_mod)
    erro_pips = calc_erro(od, W_data, W_valor)
    print "ERRO PIPS:", erro_pips
    od, W_data, W_valor, temp_volca = volca.main(w_mod)
    erro_volca = calc_erro(od, W_data, W_valor)
    print "ERRO VOLCA:", erro_volca
    return temp_pips, temp_volca, erro_pips, erro_volca
	#falta retornar os valores de erro e tempo e fazer essa parada igual gente pq tem mta gambiarra

def erro_vs_pontos():
    saida = open("erro_vs_pontos.csv", "w")
    saida.write('"Quantidade de Pontos"')
    saida.write(',')
    saida.write('Tempo Pips')
    saida.write(',')
    saida.write('Erro Pips')
    saida.write(',')
    saida.write('Tempo Volca')
    saida.write(',')
    saida.write('Erro Volca')
    saida.write('\n')
    for i in range(5, 105, 5):
        temp_pips, temp_volca, erro_pips, erro_volca = main(i)
        saida.write(str(i))
        saida.write(',')
        saida.write(str(temp_pips))
        saida.write(',')
        saida.write(str(erro_pips))
        saida.write(',')
        saida.write(str(temp_volca))
        saida.write(',')
        saida.write(str(erro_volca))
        saida.write('\n')
    saida.close()
erro_vs_pontos()
