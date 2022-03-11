import pandas as pd
import matplotlib.pyplot as plt
import random


####################
# Crear un Dataframe
####################

# A pandas DataFrame can be created using various inputs like −
#   Lists
#   dict
#   Series
#   Numpy ndarrays
#   Another DataFrame
# https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

datos = [
    {
        "columna1": 1,
        "columna2":93
    },
    {
        "columna1":2,
        "columna2":105 
    }
    ]

#Creamos un Dataframe de datos numéricos
df2 = pd.DataFrame(data=datos)

#Creamos un Dataframe de alumnos
students_df = pd.DataFrame({
    'Name': ["Jonathan", "Will", "Michael", "Liva", "Sia", "Alice"],
    'Age': [10, 11, 9, 10, 10, 11],
    'Group': ["A", "B", "A", "A", "B", "B"],
    'GPA': [3.2, 3.5, 4.0, 2.9, 4.0, 3.6]

})


################
# Carga de Datos
################

df = pd.read_csv(, index_col="")

#Muestra las primeras y las últimas lineas del Dataframe
df.head()
df.tail()

#Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
df.describe()

###################
# Limpieza de Datos
###################

#Elimina las filas que tienen datos incompleto
df_sinna = df.dropna()

#Se sustituyen los nulos con 0
df_naacero = df.fillna(0)

#Podemos especificar un valor para cada columna mediante un diccionario a la hora de sustituir los nulos
df_sinnavalores = df.fillna({"columna1": 0, "columna2" : 1})

###################
# Filtrado de Datos
###################

#Recuperar el valor de una columna
df["columna1"]

#Para recuperar una serie de columnas del Dataframe lo tenemos que hacer mediante una lista con las columnas a recuperar
df[["columna1","columna2","columna3"]]

#Accedemos a la primera fila, mediante la función iloc señalando el índice 0
df.iloc[0]

#Para acceder a un rango de índices
df.iloc[0:4]

#Para acceder sólo a índices concretos utilizamos una lista
df.iloc[0,1,2]

#Para filtrar por identificadores de cada fila sustituimos iloc por loc
df.loc[18245,18248]

#Mediante loc podemos filtrar a la vez filas y columnas
df.loc[[18245,18248], ["columna1", "columna2"]]

#Filtrado por condiciones. La columna1 es mayor que 400
df[df["columna1"] > 400]

#Filtrado para varias condiciones se usa el & (AND) y el | (OR) encerrando cada condición entre paréntesis
df[(df["columna1"] > 400) & (df["columna2"] > 20)]

#Para filtrar por condiciones de texto (que no sean numéricas)
df[df["columna3"].str.contains("España")]

#########################
# Transformación de Datos
#########################

#Definimos una función de transformación para transformar los datos
def calcular (columna1):
    valor = columna1 * random.randint(3, 5)
    return valor    

#Obtenemos los valores de la nueva columna aplicándole a la columna de la que obtenemos los datos la función de transformación
df["nueva_columna"] = df["columna1"].apply(calcular)


#Obtener un nuevo valor a partir del valor de variar columnas
#Para ello creamos una función de transformación que recibe la fila completa
def calcular2(fila):
    resultado = fila["columna1"] * fila["columna2"]
    return resultado

#La nueva columna la creamos aplicando la función de transformación a cada fila del dataframe (Esto se indica mediante axis=1) 
df["nueva_columna"] = df.apply(calcular2, axis=1)

#####################
# Agrupación de Datos
#####################

#Agrupamos por la columna4 indicando que queremos transformar el resto de columnas calculando su promedio
df.groupby("columna4").mean()

#Podemos especificar el cálculo de cada columna mediante un diccionario
grouped = df.groupby("columna4").agg({
    "columna1": 'sum',
    "columna2": 'mean',
    "columna3": 'max'
})

#################################
# Filtrado de Agrupación de Datos
#################################

#Podemos filtrar por valores de columnas indicando las columna y el valor por los que queremos filtrar
grouped[grouped["columna1"] > 5000]


############################
# Gráficos a partir de Datos
############################

#Se puede mostrar directamente un gráfico indicando la columna del dataframe y el tipo de gráfico en plot() y luego utilizando show()
grouped["columna1"].plot(kind="bar")
plt.show() 

#Para mostrar el valor de varias columnas indicamos las columnas a representar en el eje x y en el eje y
df.plot(kind="scatter", x="columna1", y="columna2")
plt.show() 


###################
# Guardado de Datos
###################
grouped.to_csv("fichero_salida.csv")
