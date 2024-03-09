import sys

def esPalindromo(texto):
    strippedT = texto.replace(" ","")
    lowerT = strippedT.lower()
    inverso = lowerT[::-1] 
    if (lowerT == inverso):
        print("True")
    else:
        print("False")
    

def chequeoParentesis(texto): #No contempla el uso correcto de parentesis, solo si la cantidad de abiertos es igual a la de cerrados
    parentesisAbierto = 0
    parentesisCerrado = 0
    for char in texto:
        asciichar = ord(char)
        if (asciichar == 40):
            parentesisAbierto += 1
        elif(asciichar == 41):
            parentesisCerrado += 1
        if(parentesisCerrado > parentesisAbierto):
            print("Un parentesis cerrado aparecio antes que un abierto")
            break 
    if(parentesisAbierto == parentesisCerrado):
        print("True")
    else:
        print("False")

def invertirTexto(texto):
    temp = texto.split()
    temp.reverse()
    print(*temp)

def main():
    print("Ingrese un texto, presione enter al terminar de escribir")
    texto = input()
    print("Elija cual es el trato que desea hacerle al texto: ")
    print("1)¿Es Palindromo?")
    print("2)Chequeo de parentesis")
    print("3)Invertir texto")
    while True: 
        eleccion = input()
        if(eleccion == "1"):
            esPalindromo(texto)
            break
        elif(eleccion == "2"):
            chequeoParentesis(texto)
            break
        elif(eleccion == "3"):
            invertirTexto(texto)
            break
        else:
            print("No ha ingresado correctamente el valor, porfavor ingrese uno de los 3 numeros de nuevo")

main()