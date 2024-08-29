import re
frase:str = str(input("ingrese un texto "))
separadores:list = r"[,; /#]"
resultado:list=re.split(separadores,frase)
print(resultado)