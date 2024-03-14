def OrdenarLista(numeros):
    """Función que recibe una lista de números enteros y los 
    escribe en un fichero llamado "ListaOrdenada.txt".
    Parámetros:
    - numeros: contiene una lista de números enteros
    Salida:
    La función no devuelve nada
    """
    with open("ListaOrdenada.txt", "w") as file:
        numeros.sort() 
        numeros.reverse()
        file.write(str(numeros))

OrdenarLista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def NumeroPar(fichero_lista):
    """Función que abre un fichero que contiene una lista ordenada de números, lo lea y escriba 
    en otro fichero llamado "ListaDePares.txt", solo los números pares del fichero de entrada
    Parámetros:
    - fichero_lista: contiene un fichero con una lista ordenada de números
    Salida:
    La función no devuelve ningún valor
    """
    with open("ListaOrdenada.txt", "r") as file:
        with open("ListaDePares.txt", "w") as file_1:
            numeros_pares = file.readline()
            for x in numeros_pares:
                cont = 0
                x = len(numeros_pares) % 1 + 2
                cont = x 
            if file_1 != x:
                file_1.write(str(cont))

NumeroPar("ListaOrdenada.txt")

    

    



