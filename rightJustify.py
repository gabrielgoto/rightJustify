# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:25:40 2021

@author: PasqualeDeAngelis
"""

# rightJustify.py
# Exerise 3.1 in Think Python

def right_justify(s):
    indent = 70 - len(s)
    print(indent * ' ' + s)
    
right_justify('monty')

