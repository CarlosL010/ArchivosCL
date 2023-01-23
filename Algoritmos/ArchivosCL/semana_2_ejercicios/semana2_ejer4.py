eleccion=input("Desea una pizza vegetariana o normal: 1-vegetariana, 2-normal " )

if eleccion=="1":
    print("los ingredienes de la pizza vegetariana son: 1-Pimiento y 2-Tofu")
    elec_veg=input("Elija uno de los ingredientes: ")
    if elec_veg=="1":
        print("Pizza vegetariana: mozarella, tomate y pimiento")
        
    elif elec_veg=="2":
        print("Pizza vegetariana: mozarella, tomate y tofu")
        
elif eleccion=="2":
    print("Los ingredientes de la pizza normal son: 1-pepperoni, 2-salmon y 3-jamon")
    elec_normal=input("Elija uno de los ingredientes: ")
    if elec_normal=="1":
        print("Pizza normal:  mozarella, tomate y pepperoni ")
        
    elif elec_normal=="2":
        print("Pizza normal:  mozarella, tomate y salmon ")
        
    elif elec_normal=="3":
        print("Pizza normal:  mozarella, tomate y jamon ")
        
        