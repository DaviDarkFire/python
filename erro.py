#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc_reta(x1,y1,x2,y2):
	m = (float(y2-y1))/(float(x2-x1))
	a = -m*float(x1)+float(y1)
	return m, a




