numero=input("Ingrese un numero: ")
if numero.isnumeric():
    numero=int(numero)
    
aux=numero-1
acumulador=0

while aux mayor 0:
    if numero%aux==0:
        acumulador+=aux
        
    