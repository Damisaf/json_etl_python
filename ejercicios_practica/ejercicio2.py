# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    
    # forma 1 
    cantidad = [0 for x in list(range(10))]
    for usuario in data:
        if usuario["completed"]:
            id = usuario["userId"]-1
            cantidad[id] += 1
    lista_id = [x+1 for x in list(range(10))]

    fig = plt.figure()
    fig.suptitle('Titulos completados (1)', fontsize=16,)
    ax = fig.add_subplot()
    ax.bar(lista_id, cantidad)
    ax.set_ylabel("cursos")
    ax.set_xlabel("Id alumno")
    ax.set_facecolor('whitesmoke')
    ax.set_ylim([0, 20])
    ax.grid()
    plt.show()
    

    # forma 2
    lista = [x.get("userId") for x in data if x.get("completed")]
    lista_suma = [lista.count(x) for x in lista]  
    cantidad = [lista_suma[i] for i in range(len(lista)) if (lista[i-1] != lista[i])]
    lista_id = list(set(lista))    

    fig = plt.figure()
    fig.suptitle('Titulos completados (2)', fontsize=16,)
    ax = fig.add_subplot()
    ax.bar(lista_id, cantidad)
    ax.set_ylabel("cursos")
    ax.set_xlabel("Id alumno")
    ax.set_facecolor('whitesmoke')
    ax.set_ylim([0, 20])
    ax.grid()
    plt.show()
    
    print("terminamos")