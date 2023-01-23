
primer_numero=(input("Ingrese un numero: "))

segundo_numero=(input("Ingrese un numero: "))

if primer_numero.isnumeric():
    primer_numero=int(primer_numero)
    if segundo_numero.isnumeric():
        segundo_numero=int(segundo_numero)
        if segundo_numero==0:
            print("Error, el divisor es 0")
        else:
            print("EL resultado es igual:", primer_numero/segundo_numero)

    

