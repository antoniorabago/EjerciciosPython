
import csv
import mysql.connector
from mysql.connector import Error
import pandas as pd
import pymysql
from sqlalchemy import create_engine


#Importamos el CSV en un Dataframe
data = pd.read_csv ("covid19_tia_muni_y_distritos_s.csv", encoding="latin-1", sep=";")   
df = pd.DataFrame(data, columns= ['municipio_distrito','fecha_informe','casos_confirmados_activos_ultimos_14dias','tasa_incidencia_acumulada_activos_ultimos_14dias','casos_confirmados_ultimos_14dias','tasa_incidencia_acumulada_ultimos_14dias','casos_confirmados_totales','tasa_incidencia_acumulada_total','codigo_geometria'])


# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="admin",
                               db="covid_madrid"))

df.to_sql('casos_municipio', 
          con=engine, 
          if_exists='replace', 
          index=False, 
          chunksize = 100)

