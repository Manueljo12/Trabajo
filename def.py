
def resultadoresta(yearone:int,yeartwo:int):
    resultadoresta:int = (yeartwo-yearone)
    return resultadoresta


yearone:int = int(input("ingrese ano actual "))
yeartwo:int = int(input("Ingrese el ano de nacimiento "))


print (resultadoresta(yeartwo,yearone))