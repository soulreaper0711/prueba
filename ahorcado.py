## probando github con el manco dos veces al cuadrao

import random

intentosPermitidos = 7
letrasAcertadas = ""
letrasFallidas = ""

def escogerPalabraAlAzar():
    palabras = "escrotony,mancalberto,perrantony,mancartola"
    lista = palabras.split(",")
    pos = random.randint(0,len(lista)-1)
    return lista[pos]

palabra = escogerPalabraAlAzar()

def dibujarAhorcado(intentosFallidos):
    nombreArchivo = "ahorcado"+str(intentosFallidos)+".txt"
    archivo = open(nombreArchivo, "r")
    print(archivo.read())

def dibujarPalabra(palabra,letrasAcertadas):
    palabraConLetras = ""
    for letra in palabra:
        if letra in letrasAcertadas:
            palabraConLetras = palabraConLetras + letra + " "
        else:
            palabraConLetras = palabraConLetras + "_" + " "
    print(palabraConLetras)

def juego():
    intentosFallidos = 0
    print(palabra)
    letra = input("Digite una letra: ")
    for i in palabra:
        if letra in palabra:
            dibujarPalabra(palabra,letrasAcertadas)
        else:
            intentosFallidos += 1
            dibujarAhorcado(intentosFallidos)
            juego()
