# TAREA CORTA Juego Ahorcado
# FORMA DE ENTREGA: Individual
# Fecha de Entrega: Martes 29 de setiembre, TEC-Digital
# Reglas:
#1. No es sensible a min/MAY
#2. Un solo nivel
#3. Adivina una letra a la vez
#4. Dibujar letras fallidas solo muestra las letras.
#5. Lista de palabras estan alambradas en escogerPalabraAlAzar
##
##Entradas: palabra, abecedario,numIntentosPermitidos
##Limitación: todos los símbolos en la palabra pertenecen al abecedario
##            numIntentosPermitidos > 0
##Salida: resultado {Gana/Pierde}
##
##
##1. Adicionales: letrasAcertadas, letrasFallidas
##
##Pasos:
##
##Inicio
##    letrasAcertadas="";
##    letrasFallidas="";
##    dibujarPalabra(palabra, letrasAcertadas);
##
##    Mientras sigueJuego(numIntentosPermitidos, palabra, letrasFallidas, letrasAcertadas) haga
##    Inicio
##        letra = leerLetra(abecedario);
##        Si esta(letra, palabra) entonces
##        Inicio
##            letrasAcertadas = agregar(letrasAcertadas,letra);
##        Fin
##        sino
##        Inicio
##            letrasFallidas = letrasFallidas + letra;
##            dibujaAhorcado(largo(letrasFallidas), numIntentosPermitidos);
##            dibujarLetrasFallidas(letrasFallidas);
##        Fin
##        dibujarPalabra(palabra, letrasAcertadas);
##   Fin
##   Si gano(palabra, letrasAcertadas) entonces
##   Inicio
##       resultado = "Gana";
##   Fin
##   sino
##   Inicio
##       resultado = "Pierde";
##   Fin
##Fin
##
##
##jugar("tecnologico", "abcdefghijklmnñopqrstuvwwxyz",10)

palabra= "ahorcado"

### metodo 1
##for letra in palabra:
##    print(letra)
##
### metodo 2
##pos= 0
##while pos < len(palabra):
##    print (palabra[pos])
##    pos = pos + 1
##
### metodo 3
##while palabra != "":
##    print(palabra[0])
##    palabra = palabra[1:]
##
### metodo 4
##def recorrer(miString, funcion):
##    if miString != "":
##        funcion(miString[0])
##        recorrer(miString[1:], funcion)
        
# dibujarPalabra(palabra, letrasAcertadas)
def dibujarPalabra(palabra, letrasAcertadas):
    palabraConLetras = ""
    for letra in palabra:
        if letra in letrasAcertadas:
            palabraConLetras = palabraConLetras + letra+" "
        else:
            palabraConLetras = palabraConLetras + "_"+" "
    print(palabraConLetras)
    
def dibujarAhorcado(IntentosFallidos):
    nombreArchivo = "ahorcado"+str(IntentosFallidos)+".txt"
    archivo = open(nombreArchivo, "r")
    print(archivo.read())

import random
def escogerPalabraAlAzar():
    palabras = "power,east,side,newyork,hurley,dell,rvca,silver"
    lista = palabras.split(",")
    pos = random.randint(0,len(lista)-1)
    return lista[pos]


#juego(escogerPalabraAlAzar(), abecedario, 6)









    

































