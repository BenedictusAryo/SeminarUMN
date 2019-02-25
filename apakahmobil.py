# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:59:43 2019

@author: Benedict Aryo
"""

def apakahmobil():
    """
    Fungsi untuk membedakan mobil atau bukan
    """
    print('\n',"Program untuk menentukan mobil atau bukan",'\n')
    print("Apakah memiliki roda ?  (Jawab True/False)")
    f1 = eval(input())
    print("apakah jumlah rodanya 4 ? (Jawab True/False)")
    f2 = eval(input())
    if f1 and f2 == True:
        print("Itu adalah Mobil")
    else:
        print("Itu bukan Mobil")


apakahmobil()