from colorama import Fore, Back, Style
import os, time 
n = input("cual es tu nombre :  ")
os.system("clear")
a = input("cual es tu primer apellido :  ")
os.system("clear")
e = input("cual es tu segundo apellido:  ")
os.system("clear")
time.sleep(1)
print(Fore.RED,n,Fore.RESET, end=" ")
print(Fore.GREEN,a,Fore.RESET, end=" ")
print(Fore.BLUE,e,Fore.RESET, end=" ")
