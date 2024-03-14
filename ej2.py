diccionario = {}

while True:
    alimento = input("Ingresa el nombre del alimento: ")
    cantidad = float(input("Ingresa la cantidad consumida(en gramos): "))
    registro = input("¿Quieres registrar otro alimento, si o no?: ")
    diccionario[alimento] = cantidad

    if registro == "no":
        print("Resumen del consumo diario: \n")
        for alimento, cantidad in diccionario.items():
            print(alimento, cantidad)
        break