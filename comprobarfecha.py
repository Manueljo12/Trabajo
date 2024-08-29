fecha = list(map(int, input("agrega una fecha en formato d,m,a: ").split("/")))
dia = fecha[0]
mes = fecha[1]
año = fecha[2]
if dia>31:
    print("el dia no es posible")
elif mes>12:
    print("el mes no es posible")
elif dia<15 or mes > 8 or año>2024 :
else:
    print("su fecha es", fecha)