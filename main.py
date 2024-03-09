import sys
import re
from unicodedata import normalize
def transformarTexto(texto): #Elimina elementos diacriticos, tildes, dieresis entre otros ademas de borrar los espacios
    nuevoTexto = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",  
        normalize( "NFD", texto), 0, re.I
    )
    nuevoTexto = re.sub(r'[.,"\'-?:!;]', '', nuevoTexto)
    nuevoTexto = normalize( 'NFC', nuevoTexto)
    nuevoTexto = nuevoTexto.replace(" ","")
    return nuevoTexto

def esPalindromo(texto):
    textoTransformado = transformarTexto(texto)
    minuscula = textoTransformado.lower()
    inverso = minuscula[::-1] 
    if (minuscula == inverso):
        print("True")
    else:
        print("False")
    

def chequeoParentesis(texto): #No contempla el uso correcto de parentesis, solo si la cantidad de abiertos es igual a la de cerrados
    parentesisAbiertos = 0
    parentesisCerrados= 0
    for char in texto:
        asciichar = ord(char)
        if (asciichar == 40):
            parentesisAbiertos += 1
        elif(asciichar == 41):
            parentesisCerrados += 1
        if(parentesisCerrados > parentesisAbiertos):
            print("Un parentesis cerrado aparecio antes que un abierto")
            break 
    if(parentesisAbiertos == parentesisCerrados):
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