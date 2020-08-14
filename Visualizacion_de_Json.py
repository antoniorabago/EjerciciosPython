# Load the Pandas libraries with alias 'pd' 
import json
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
import numpy as np
import datetime
import urllib


font = {'size'   : 10}

plt.rc('font', **font)

sns.set_palette(sns.color_palette("Dark2",10))


hoy = datetime.date.today() - datetime.timedelta(days=1)
hoymenos14 = hoy - datetime.timedelta(days=14)

print(hoy)

#Leemos el fichero Json en local - pd.read_json (r'Path where you saved the JSON file\File Name.json')
datos_json = pd.read_json ('casos.json')
#print(datos_json)
datos = pd.json_normalize(datos_json['records'])


#Leemos el fichero Json directamente desde una URL sin descargarlo en local
#url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
#json_url = urllib.request.urlopen(url)
#datos_json = json.loads(json_url.read())


#Filtramos el Dataframe para el país indicado 
datospais_df = datos[datos['countryterritoryCode'] == 'ESP']

#Convertimos la fecha de formato cadena a formato fecha para poder filtrar un intervalo de fechas
datospais_df['dateRep'] = pd.to_datetime(datospais_df['dateRep'], format='%d/%m/%Y')
#datospais_df['dateRep'] = pd.to_datetime(datospais_df['dateRep'], dayfirst = True)
print (datospais_df['dateRep'])

#Convertimos el número de casos de formato cadena a formato número para poder calcular las medias móviles
datospais_df['cases'] = pd.to_numeric(datospais_df['cases'])

#Ordenamos los datos por fecha ascendentemente
DatosOrdenadosPorFecha_df = datospais_df.sort_values(by = 'dateRep',ascending = True)


#Calculamos la media móvil de los últimos 14 días
DatosOrdenadosPorFecha_df['moving14'] = DatosOrdenadosPorFecha_df['cases'].transform(lambda x: x.rolling(14, 1).mean()) 
#Calculamos la media móvil de los últimos 7 días
DatosOrdenadosPorFecha_df['moving7'] = DatosOrdenadosPorFecha_df['cases'].transform(lambda x: x.rolling(7, 1).mean())

#Indicamos el intervalo de fechas que queremos utilizar
start_date = "2020-03-01"
end_date = "2020-08-13"
mask = (DatosOrdenadosPorFecha_df['dateRep'] >= start_date) & (DatosOrdenadosPorFecha_df['dateRep'] <= end_date)
fechasfiltradas_df = DatosOrdenadosPorFecha_df.loc[mask]


#Creamos el dataframe con los datos que se van a utilizar en el informe
grafico_df = fechasfiltradas_df[['dateRep','cases','moving14','moving7']]

#Formateamos la fecha de nuevo a formato cadena para que se muestre correctamente en el gráfico
grafico_df['dateRep']=grafico_df['dateRep'].astype(str)


#Dibujamos el gráfico
fig, ax = plt.subplots(1,1) 


grafico = sns.barplot(ax=ax,
                      x="dateRep", 
                      y="cases",                   
                      data=grafico_df, 
                      label="Nuevos Casos Diarios")


###Esto es para los índices de un gráfico catplot
#grafico.set_titles("Nuevos Casos en España", fontsize=30)
#grafico.set_xlabels("Fecha",fontsize=20)
#grafico.set_ylabels("España",fontsize=20)
#grafico.set_yticklabels(fontsize=10)
#grafico.set_xticklabels(fontsize=5)


#Gráfico de líneas media móvil de los últimos 14 días
graficomv14 = sns.lineplot(
    ax=ax,
    x="dateRep",
    y="moving14",
    data=grafico_df, 
    label="Media Movil 14"
    )

#Gráfico de líneas media móvil de los últimos 7 días
graficomv7 = sns.lineplot(
    ax=ax,
    x="dateRep",
    y="moving7",
    data=grafico_df, 
    label="Media Movil 7"    
)#.set_title('Nuevos Casos de Coronavirus')


plt.legend()
plt.suptitle("Nuevos Casos de Coronavirus en España a " + hoy.strftime("%d/%m/%Y"), fontsize=18)
plt.xlabel('Fecha', fontsize=16)
plt.ylabel('Nuevos Casos', fontsize=16)


plt.xticks(rotation=90, horizontalalignment='right',fontsize=5)


plt.show()