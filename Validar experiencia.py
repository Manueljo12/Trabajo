nombre_conductor:str = str(input("Ingrese el Nombre completo del Conductor: "))
fecha_licencia:str = str(input("Ingrese su fecha de nacimiento: "))
numero_de_licencia:str = str(input("Ingrese numero de licencia: "))
asegurable:str = str(input("Ingrese año actual: "))

def asegurable(nombre_conductor:str,fecha_licencia:str,numero_de_licencia:str,asegurable:str ):
    
    print("")
    
    if conductor_asegurable >=  2:
        
        print("El nombre del conductor es: ",nombre_conductor)
        print("La fecha de licencia: ",fecha_licencia)
        print("El numero de licencia: ",numero_de_licencia)
        
    else:
        print("El conductor no es asegurable")
        

Asegurable(nombre_conductor,fecha_licencia,numero_de_licencia)
        