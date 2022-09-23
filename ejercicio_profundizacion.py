import json
import requests
import numpy as np
import matplotlib.pyplot as plt

def fetch():
    response = requests.get(url)
    datos = response.json()    
    json_response = datos["results"]
    filtro = [{"price": x["price"] , "condition": x["condition"]} for x in json_response if x["currency_id"] == "ARS"]
    return filtro

def transform(dataset, min, max):
    pass



if __name__ == "__main__":
    # min = ....
    # max = ....
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    dataset = fetch()
    min = int(input("Ingrese el valor minimo: "))
    max = int(input("Ingrese el valor maximo: "))
    data = transform(dataset, min, max)
    #report(data)

