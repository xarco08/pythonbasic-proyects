import os, time 
os.system("clear")
print("elige una opcion", "1:sumar", "2:restar", "3:dividir", "4:multiplicar", "5:ejecutar un comando", sep = "\n")
selec = float(input("que eliges? : "))
time.sleep(1)
os.system("clear")
if selec == 1:
    sumando1=float(input("numero 1 : "))
    sumando2=float(input("numero 2 : "))
    print("el resultado es: ",sumando1+sumando2)
    time.sleep(2)
    resp=input("quieres hacer algo mas? (respuesta si o no):  \n")
    if resp == "si":
        print("reiniciando...")
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 ./menuvictor.py")
    else:
        print("cerrando...")
        time.sleep(1)
        os.system("clear")
elif selec == 2:
    restanum1=float(input("numero 1 : "))
    restanum2=float(input("numero que resta al 1 : "))
    print("el resultado es: ",restanum1-restanum2)
    time.sleep(2)
    resp=input("quieres hacer algo mas? (respuesta si o no):  \n")
    if resp == "si":
        print("reiniciando...")
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 ./menuvictor.py")
    else:
        print("cerrando...")
        time.sleep(1)
        os.system("clear")
elif selec == 3:
    numerodiv=float(input("numero a dividir : "))
    divisor=float(input("numero divisor : "))
    if divisor != 0:
        print("el resultado es: ",round(numerodiv/divisor,2))
    else:
        print("no se puede dividir entre 0")
        time.sleep(2)
    resp=input("quieres hacer algo mas? (respuesta si o no):  \n")
    if resp == "si":
        print("reiniciando...")
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 ./menuvictor.py")
    else:
        print("cerrando...")
        time.sleep(1)
        os.system("clear")
elif selec == 4:
    factor1=float(input("numero 1 : "))
    factor2=float(input("numero 2 : "))
    print("el resultado es: ",factor2*factor1)
    time.sleep(2)
    resp=input("quieres hacer algo mas? (respuesta si o no):  \n")
    if resp == "si":
        print("reiniciando...")
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 ./menuvictor.py")
    else:
        print("cerrando...")
        time.sleep(1)
        os.system("clear")
elif selec == 5:
    comando=input("que comando quieres ejecutar : ")
    os.system(comando)
    time.sleep(2)
    resp=input("quieres hacer algo mas? (respuesta si o no):  \n")
    if resp == "si":
        print("reiniciando...")
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 ./menuvictor.py")
    else:
        print("cerrando...")
        time.sleep(1)
        os.system("clear")
else:
    print("funcion no definida, reiniciando programa")
    time.sleep(2)
    os.system("python3 ./menuvictor.py")




