import csv
import mysql.connector
from mysql.connector import Error
import pandas as pd
import pymysql
from sqlalchemy import create_engine





#Importamos el CSV en un Dataframe
data = pd.read_csv ("covid19_tia_muni_y_distritos_s.csv", encoding="latin-1", sep=";")   
df = pd.DataFrame(data, columns= ['municipio_distrito','fecha_informe','casos_confirmados_activos_ultimos_14dias','tasa_incidencia_acumulada_activos_ultimos_14dias','casos_confirmados_ultimos_14dias','tasa_incidencia_acumulada_ultimos_14dias','casos_confirmados_totales','tasa_incidencia_acumulada_total','codigo_geometria'])

#Convertimos la fecha del informe a formato fecha en el Dataframe
#df['fecha_informe'] = pd.to_datetime(df['fecha_informe'])

print(df)


#Hay que crear la Base de Datos en MySql previamente. Se puede realizar desde la línea de comandos con esta instrucción
#Create database Nombre_BBDD;


# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="admin",
                               db="covid_madrid"))



print(engine)

#Conexión con la Base de Datos
#try:
#    connection = mysql.connector.connect(host='localhost',
#                                         database='covid_madrid',
#                                         user='root',
#                                         password='admin')
#    if connection.is_connected():
#        db_Info = connection.get_server_info()
#        print("Conectado a MySQL Server version", db_Info)
#        cursor = connection.cursor()
#        cursor.execute("select database();")
#        record = cursor.fetchone()
#        print("Estás conectado a la base de datos: ", record)

#except Error as e:
#    print("Error al conectar a MySQL", e)
#finally:
#    if (connection.is_connected()):
        #cursor.close()
        #connection.close()
        #print("La conexión a MySQL está cerrada")


#Creamos una tabla en MySQL
#try:
#    #connection = mysql.connector.connect(host='localhost',
#    #                                     database='Electronics',
#    #                                     user='pynative',
#    #                                     password='pynative@#29')


#    #Id int(5) NOT NULL,
#    #PRIMARY KEY (Id))

#    mySql_Create_Table_Query = """CREATE TABLE Casos_Municipio (                              
#                             municipio_distrito varchar(250) NOT NULL,
#                             fecha_informe Date NOT NULL,
#                             casos_confirmados_activos_ultimos_14dias float,
#                             tasa_incidencia_acumulada_activos_ultimos_14dias float,
#                             casos_confirmados_ultimos_14dias float,
#                             tasa_incidencia_acumulada_ultimos_14dias float,
#                             casos_confirmados_totales float,
#                             tasa_incidencia_acumulada_total float,
#                             codigo_geometria int(8))"""
                             
                                 
#    result = cursor.execute(mySql_Create_Table_Query)
#    print("Tabla creada correctamente")

#except mysql.connector.Error as error:
#    print("Failed to create table in MySQL: {}".format(error))
#finally:
#    if (connection.is_connected()):
#        cursor.close()
#        connection.close()
#        print("MySQL connection is closed")



# Insert DataFrame to Table
#insert_stmt = (
#  "INSERT INTO Casos_Municipio (id, municipio_distrito, fecha_informe, casos_confirmados_activos_ultimos_14dias, tasa_incidencia_acumulada_activos_ultimos_14dias, casos_confirmados_ultimos_14dias, tasa_incidencia_acumulada_ultimos_14dias, casos_confirmados_totales, tasa_incidencia_acumulada_total, codigo_geometria) "
#  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
#  )

#contador=1

#for row in df.itertuples():
#    data = (contador,
#            row.municipio_distrito, 
#            row.fecha_informe,
#            row.casos_confirmados_activos_ultimos_14dias,
#            row.tasa_incidencia_acumulada_activos_ultimos_14dias,
#            row.casos_confirmados_ultimos_14dias,
#            row.tasa_incidencia_acumulada_ultimos_14dias,
#            row.casos_confirmados_totales,
#            row.tasa_incidencia_acumulada_total,
#            row.codigo_geometria
#            )
#    print(data)

#    result = cursor.execute(insert_stmt,data)
#    contador = contador + 1


df.to_sql('Casos_Municipio', 
          con=engine, 
          if_exists='replace', 
          #index=False, 
          chunksize = 10)


    #result = cursor.execute("""
    #            INSERT INTO Casos_Municipio (municipio_distrito, fecha_informe, casos_confirmados_activos_ultimos_14dias, tasa_incidencia_acumulada_activos_ultimos_14dias, casos_confirmados_ultimos_14dias, tasa_incidencia_acumulada_ultimos_14dias, casos_confirmados_totales, tasa_incidencia_acumulada_total, codigo_geometria FROM Casos_Municipio)
    #            VALUES (?,?,?,?,?,?,?,?,?)
    #            """,
    #            row.municipio_distrito, 
    #            row.fecha_informe,
    #            row.casos_confirmados_activos_ultimos_14dias,
    #            row.tasa_incidencia_acumulada_activos_ultimos_14dias,
    #            row.casos_confirmados_ultimos_14dias,
    #            row.tasa_incidencia_acumulada_ultimos_14dias,
    #            row.casos_confirmados_totales,
    #            row.tasa_incidencia_acumulada_total,
    #            row.codigo_geometria
    #            )
    #print("Registro del municipio " + row.municipio_distrito + " creado correctamente")




#Hacer consulta 
#cursor = connection.cursor()
#cursor.execute("SELECT municipio_distrito, fecha_informe, casos_confirmados_activos_ultimos_14dias, tasa_incidencia_acumulada_activos_ultimos_14dias, casos_confirmados_ultimos_14dias, tasa_incidencia_acumulada_ultimos_14dias, casos_confirmados_totales, tasa_incidencia_acumulada_total, codigo_geometria FROM Casos_Municipio" )
#for id in cursor.fetchall() :
#    print (municipio_distrito, fecha_informe, casos_confirmados_activos_ultimos_14dias, tasa_incidencia_acumulada_activos_ultimos_14dias, casos_confirmados_ultimos_14dias, tasa_incidencia_acumulada_ultimos_14dias, casos_confirmados_totales, tasa_incidencia_acumulada_total, codigo_geometria)


#if (connection.is_connected()):
#        connection.commit()
#        print("La Base de Datos MySQL se ha actualizado correctamente")
#        cursor.close()
#        connection.close()
#        print("La desconexión de la Base de Datos MySQL se ha realizado correctamente")

