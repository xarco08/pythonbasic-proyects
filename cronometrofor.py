import os, time
print("cronometro")
p=int(input("dame el primer numero:  "))
a=int(input("dame el ultimo numero:  "))
b=int(input("de cuanto en cuanto quieres que avance:  "))
for i in range (p,a,b):
	print(i)
	time.sleep(1)
	 
