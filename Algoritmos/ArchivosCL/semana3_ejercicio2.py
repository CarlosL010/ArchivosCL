tabla=input("ingrese un numero del 1 al 10:  ")

if tabla.isnumeric():
    tabla=int(tabla)

for numero_tabla in range(1,11,1):
    
    ready=tabla*numero_tabla
    
    print(ready)
    
    
    