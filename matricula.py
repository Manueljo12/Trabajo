nombre_alumno:str = str(input("Ingrese el Nombre completo del Alumno: "))
fecha_de_nacimiento:str = str(input("Ingrese su fecha de nacimiento: "))
sexo:str = str(input("Ingrese su orientacion sexual: "))
ciudad_de_residencia:str = str(input("Ingrese su ciudad de residencia: "))
programa_de_interes:str = str(input("Ingrese el programa que desea cursar: ")).lower()
valormatricula:int = int(input("Ingrese el valor de la matricula: "))

def inscripcion(nombre_alumno:str,fecha_de_nacimiento:str,sexo:str,ciudad_de_residencia:str,programa_de_interes:str,valormatricula:int):
    
    print("")
    
    if programa_de_interes == "programacion":
        
        print("El nombre del alumno es: ",nombre_alumno)
        print("La fecha de nacimiento del alumno es: ",fecha_de_nacimiento)
        print("El sexo del alumno es: ",sexo)
        print("La ciudad de residencia del alumno es: ",ciudad_de_residencia)
        print(30 * "-")
        print("Matricula: \n","Programa: Programacion \n","Duracion: 6 meses \n", "Salon: 105 \n","Bloque: 6 \n")
        print("Matriculado en el programa de: ",valormatricula)
        
    else:
        print("El programa academico no existe")
        

inscripcion(nombre_alumno,fecha_de_nacimiento,sexo,ciudad_de_residencia,programa_de_interes,valormatricula)
        
    