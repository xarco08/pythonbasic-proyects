import time, os
os.system("clear")
fin= float(input("hasta que numero quieres cronometrar? : "))
inicio=0
while inicio<fin:
    time.sleep(1)
    inicio += 1
    print(inicio)


