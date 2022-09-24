import json
import requests
import matplotlib.pyplot as plt

def fetch():
    response = requests.get(url)
    datos = response.json()    
    json_response = datos["results"]    
    filtro = [{"price": x["price"] , "condition": x["condition"]} for x in json_response if x["currency_id"] == "ARS"]
    return filtro

def transform(dataset, min, max):    
    lista_debajo = [x for x in dataset if x["price"] < min]
    lista_arriba = [x for x in dataset if x["price"] > max]
    lista_medio  = [x for x in dataset if (x["price"] >= min and x["price"] <= max)]
    min_count     = len(lista_debajo)
    min_max_count = len(lista_medio)
    max_count     = len(lista_arriba)
    return [min_count, min_max_count, max_count]


def report(data):   
    fig = plt.figure()
    fig.suptitle('Alquileres en '+ ciudad, fontsize=16)
    ax = fig.add_subplot()
    lab = ["< a "+str(min), "Entre "+str(min)+" y "+str(max), "> a "+ str(max)]
    ax.pie(data, labels=lab, startangle=90)                   
    plt.show()
    

if __name__ == "__main__":
    #url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'    
    ciudad = input ("Ingrese ciudad         : ")
    min = int(input("Ingrese el valor minimo: "))
    max = int(input("Ingrese el valor maximo: "))
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20'+ciudad+'%20&limit=50'    
    dataset = fetch()    
    data = transform(dataset, min, max)
    report(data)

