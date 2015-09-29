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

##def juego():
##    intentosFallidos = 0
##    print(palabra)
##    letra = input("Digite una letra: ")
##    while sigueJuego(intentosPermitidos,palabra,letrasFallidas,letrasAcertadas):
##        if letra in palabra:
##            dibujarPalabra(palabra,letrasAcertadas)
##        else:
##            intentosFallidos += 1
##            dibujarAhorcado(intentosFallidos)
##            juego()

abecedario = "abcdefghijklmnñopqrstuvwxyz"

def leerLetra(abecedario):
    a = input("Digite una letra: ")
    if a == "" or a not in abecedario:
        print("Ingresó un caracter que no pertenece al abecedario, por favor intente de nuevo")
        leerLetra(abecedario)
    else:
        if a in abecedario:
            print("si")

##while sigueJuego(intentosPermitidos,palabra,letrasFallidas,letrasAcertadas):
##    letra = leerLetra(abecedario)
##    if esta(letra,palabra):
##        letrasAcertadas = agregar(letrasAcertadas,letra)
##    else:
##        letrasFallidas = letrasFallidas + letra
##        dibujarAhorcado(len(letrasFallidas),intentosPermitidos)
##        dibujarLetrasFallidas(letrasFallidas)
##    dibujarPalabra(palabra,letrasAcertadas)
##if gano(palabra,letrasAcertadas):
##    resultado = "Gana"
##else:
##    resultado = "Pierde"
