#!/usr/bin/env python
# -*- coding: utf-8 -*-

#código pra criar um arquivo com somente os valores que serão necessários para os programas

s = open("output.ou", "w")

with open('input.in') as f:
    for linha in f:

        linha = linha.strip()

        if linha:
            valores = linha.split(',')

            a = valores[1]
            b = a.split("\"")
            c = ''.join(b)

            s.write(c)
            s.write(',')
            s.write(valores[5])
            s.write('\n')

f.close()
s.close()
