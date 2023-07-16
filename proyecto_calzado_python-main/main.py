#Librerias

import numpy as np
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import graficos

# Funciones:
engine=sqlalchemy.create_engine("sqlite:///ventas_calzados.db")
base=declarative_base()

class Ventas(base):
    __tablename__='ventas'
    id = Column(Integer,primary_key=True)
    fecha = Column(String)
    producto_id = Column(Integer)
    pais = Column(String)
    genero = Column(String)
    talle = Column(String)
    precio = Column(String)
    
    def __repr__(self):
        return f"Ventas: {self.producto_id}"

def read_db():
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(Ventas)

    paises_lista = []
    generos_lista = []
    taller_lista=[]
    precios_lista=[]

    for producto in query:
        paises_lista.append(producto.pais)
        generos_lista.append(producto.genero)
        taller_lista.append(producto.talle)
        precios_lista.append(producto.precio)

    paises = np.array(paises_lista)
    generos = np.array(generos_lista)
    talle = np.array(taller_lista)
    precios = np.array([float(value.replace('$','').strip()) for value in precios_lista])

    return paises, generos, talle, precios

def obtener_paises_unicos(paises):
    return np.unique(paises)

def obtener_ventas_por_pais (paises_objetivo, paises, precios):
    result = {}
    for pais_objetivo in paises_objetivo:
        result[pais_objetivo] = 0
        for pais, precio in zip(paises, precios):
            # valor = 0
            if pais == pais_objetivo:
                # valor += precio
                result[pais_objetivo] += float(precio)
        
        
        # for pais in paises:
        #     for precio in precios:
        #         # valor = 0
        #         if pais_objetivo == pais:
        #             # valor += precio

        #         # print (pais_objetivo)
        #             result[pais_objetivo] += precio
    return result


def obtener_calzado_mas_vendido_por_pais(paises_objetivo, paises, talles):
        result = {}
        
        for pais in paises_objetivo:
            indices = np.where(paises == pais)[0]
            country_talles = talles[indices]
            
            unique_talles, counts = np.unique(country_talles, return_counts=True) 
            
            most_sold_talle = unique_talles[np.argmax(counts)]
            
            result[pais] = most_sold_talle
        
        return result
    
def obtener_ventas_por_genero_pais(paises_objetivo, genero_objetivo, paises, generos):
    result = {}
    mask = generos == genero_objetivo
    pais_filtrado_por_genero = paises[mask]
    unique_country, counts = np.unique(pais_filtrado_por_genero, return_counts=True)
    for pais in paises_objetivo:
        indice = np.where(unique_country == pais)[0]
        count_genre = counts[indice]
        result[pais] = count_genre[0]

    return result

    # for pais in paises_objetivo:
        
        # indices = np.where(paises == pais)[0]
        
#Bloque principal

if __name__ == "__main__":
    database = read_db()
    paises = database[0]
    genero = database[1]
    talle = database[2]
    precios = database[3]
    print('Paises: ',obtener_paises_unicos(paises))


    paises_objetivo = ["Canada", "Germany", "United Kingdom"]
    ingresos_por_pais = obtener_ventas_por_pais(paises_objetivo, paises, precios)
    print('Ingresos por pais: ', ingresos_por_pais)
    print(graficos.plot_bar(ingresos_por_pais, "Ingresos por pais"))
    
    calzado_por_pais = obtener_calzado_mas_vendido_por_pais(paises_objetivo, paises, talle)
    print('Calzado por pais: ', calzado_por_pais)
    print(graficos.plot_scatter(calzado_por_pais, "Calzado por pais"))


    genero_objetivo = 'Unix'
    calzado_por_genero = obtener_ventas_por_genero_pais(paises_objetivo, genero_objetivo, paises, genero)
    print('Calzado por genero: ', calzado_por_genero)
    print(graficos.plot_bar(calzado_por_genero, "Calzado por genero"))