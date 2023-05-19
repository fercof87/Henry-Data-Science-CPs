# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.
from xml.dom.minidom import Entity
import pandas as pd
import numpy as np


def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galciia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después de la coma, redondeado.
    '''
    #Tu código aca: 
    cotizaciones = pd.read_csv("datasets\GGAL - Cotizaciones historicas.csv")
    return cotizaciones.maximo.sum().round(4)


def Ret_Pregunta02(precio_min, precio_max):
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galciia SA.
    Esta función toma como argumentos un precio mínimo y un precio máximo cualquiera sea y
    devuelve el promedio correspondiente a la columna "cierre" del conjunto resultante
    entre [precio_min, precio_max]
     filtrando por la columna "apertura", con 2 decimales después del punto.
    PISTA: usar una máscara sobre la columna "apertura" y después hacer los cálculos
     sobre la columna "cierre"
    '''
    #Tu código aca:
    cotizaciones = pd.read_csv("datasets\GGAL - Cotizaciones historicas.csv")
    return cotizaciones[np.logical_and(cotizaciones.apertura > precio_min, cotizaciones.apertura < precio_max)].cierre.mean().round(2)


def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros únicos de la columna Year sin tener en cuenta 
    aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    consumo = pd.read_csv("datasets\Fuentes_Consumo_Energia.csv")
    return consumo.Year.dropna().nunique()


def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    consumo = pd.read_csv("datasets\Fuentes_Consumo_Energia.csv")
    return consumo.shape[0]


def Ret_Pregunta05():
    '''
        Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galciia SA. Crear una nueva columna, llamada "variacion", que registre
    las variaciones de la columna "máximo". La función debe devolver el valor máximo de la 
    columna "variacion". 
    '''
    #Tu código aca:  
    cotizaciones = pd.read_csv("datasets\GGAL - Cotizaciones historicas.csv")

    cotizaciones["variacion"] = cotizaciones.maximo - cotizaciones.maximo[0]
    return cotizaciones.variacion.max().round(1)

def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy, cada uno de dimensión 2, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:

    return np.logical_and(m1.shape[1] == m2.shape[0], m2.shape[1] == m3.shape[0])


def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar cuál de la siguiente lista de países tuvo mayor generacíon de
    energía hìdrica (Hydro_Generation_TWh) en el año 2017:
        * Argentina
        * Germany
        * Chile
        * Colombia
        * Ecuador
        * Mexico
        * Peru
    Debe retornar el valor en un dato de tipo string.
    '''
    #Tu código aca:
    consumo = pd.read_csv("datasets\Fuentes_Consumo_Energia.csv")
    lista = ["Argentina", "Germany", "Chile", "Colombia", "Ecuador", "Mexico", "Peru"]

    return consumo.Entity[consumo[consumo.Entity.isin(lista)].Hydro_Generation_TWh.idxmax()]
    

def Ret_Pregunta08():
    '''
        Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galciia SA.
    Esta función debe calcular el promedio tomando los últimos 100 datos de las columnas "apertura"
    y "cierre", en ese orden, y retornar los dos valores en forma de tupla. Usar dos decimales después
    del punto y redondear de ser necesario.
    '''
    #Tu código aca:
    cotizaciones = pd.read_csv("datasets\GGAL - Cotizaciones historicas.csv")
    return (cotizaciones.tail(100).apertura.mean().round(2),cotizaciones.tail(100).cierre.mean().round(2))


def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe la mayor cantidad, en TWh, de energía nuclear generada, agrupando según entidad.
    Use dos decimales después del punto.
    '''
    #Tu código aca:
    consumo = pd.read_csv("datasets\Fuentes_Consumo_Energia.csv")
    return consumo.groupby("Entity")["Nuclear_Generation_TWh"].sum().max().round(2)

def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    
    cantidad = 0

    if(lista.getCabecera()):
        cantidad = 1
        nodo = lista.getCabecera()
        while(nodo.getSiguiente()):
            cantidad += 1
            nodo = nodo.getSiguiente()
    
    return cantidad
