#!/usr/bin/env python
# -*- coding: utf-8 -*-
import erro
import gera_graficos as graf
import trataArquivo as t
import sys
import os
#for filename in os.listdir(directory):

def trataArquivo(file_name):
    s = open("output.ou", "w")
    with open(file_name) as f:
        flag = 0
        for linha in f:
            if (flag):
                linha = linha.strip()

                if linha:
                    valores = linha.split(',')

                    a = valores[1]
                    b = a.split("\"")
                    c = ''.join(b)
                    d = c.split(" ")
                    c = d[0]+d[1]


                    s.write(c)
                    s.write(',')
                    s.write(valores[5])
                    s.write('\n')
            else:
                flag = 1

    f.close()
    s.close()




















def execucao():
