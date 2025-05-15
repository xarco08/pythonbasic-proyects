from math import sqrt
import os
a = 0
while a==0 :
	print("programa para hacer ecuaciones de segundo grado", end="\n")
	a=float(input("dame el numero a : "))
	os.system("clear")
b=float(input("dame el numero b : "))
os.system("clear")
c=float(input("dame el numero c : "))
os.system("clear")
r=(b**2)-4*a*c
if r>=0:
	print("la solucion 1 es ", (b+r)/(a*2))
	print("la solucion 2 es ", (b-r)/(a*2))
else:
	print("las soluciones son imaginarias")
