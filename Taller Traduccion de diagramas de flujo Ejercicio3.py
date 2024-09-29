def busqueda_binaria(arr, x):

    izq = 0
    der = len(arr) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if arr[medio] == x:
            return medio  # índice encontrado
        elif x < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1

    return -1  


arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
valor_a_buscar = int(input("Ingrese el valor a buscar: "))

resultado = busqueda_binaria(arreglo, valor_a_buscar)

if resultado != -1: 
    print(f'Elemento encontrado en el índice es: {resultado}')
else:  
    print('Elemento no encontrado')
