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

def dibujarLetra(palabra,letrasAcertadas):
    palabraConLetras = ""
    for letra in palabra:
        if letra in letrasAcertadas:
            palabraConLetras = palabraConLetras + letra + " "
        else:
            palabraConLetras = palabraConLetras + "_" + " "
    print(palabraConLetras)

abecedario = "abcdefghijklmnñopqrstuvwxyz"

def leerLetra(abecedario):
    a = input("Digite una letra: ")
    if a == "" or a not in abecedario:
        print("Ingresó un caracter que no pertenece al abecedario, por favor intente de nuevo")
        leerLetra(abecedario)
    else:
        if a.lower() in abecedario:
            a = a.lower()
            return a

def iguales(letrasAcertadas,palabra):
    for letra in palabra:
        if letra in letrasAcertadas:
            iguales = True
        else:
            return False
    return iguales

def sigueJuego(intentosPermitidos,palabra,letrasFallidas,letrasAcertadas):
    if len(letrasFallidas) > intentosPermitidos or iguales(letrasAcertadas,palabra):
        return False
    else:
        return True

def esta(letra,palabra):
    if letra in palabra:
        return True
    else:
        return False

def gano(palabra,letrasAcertadas):
    if iguales(letrasAcertadas,palabra):
        return True
    else:
        return False

def dibujarLetrasFallidas(letra):
    print("----------------\n"+letra+"\n----------------")

def juego():
    palabra = escogerPalabraAlAzar()
    letrasAcertadas = ""
    letrasFallidas = ""
    while sigueJuego(intentosPermitidos,palabra,letrasFallidas,letrasAcertadas):
        letra = leerLetra(abecedario)
        if esta(letra,palabra):
            letrasAcertadas = letrasAcertadas + letra + " "
        else:
            letrasFallidas = letrasFallidas + letra
            dibujarAhorcado(len(letrasFallidas))
            dibujarLetrasFallidas(letrasFallidas)
        dibujarLetra(palabra,letrasAcertadas)
    if gano(palabra,letrasAcertadas):
        print("Gana")
    else:
        if len(letrasFallidas) == intentosPermitidos:
            print("Pierde")

juego()
