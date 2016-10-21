#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
