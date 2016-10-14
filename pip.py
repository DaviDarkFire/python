#!/usr/bin/env python
# -*- coding: utf-8 -*-

def distancia_vertical(x1,x2,x3,y1,y2,y3): #essa distância verticar retorna a distância do ponto analisado com relação
    # à linha que liga os pips adjacentes deste ponto, assim o quão maior for a distância vertical, maior vai ser
    #a importância daquele ponto
    dv = (y1+(y2-y1)*((x3-x1)/(x2-x1)))-y3
    if (dv < 0):
        dv = dv*(-1)
    return dv

def calc_pip():
    
