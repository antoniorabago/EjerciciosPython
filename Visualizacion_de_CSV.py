# Load the Pandas libraries with alias 'pd' 
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
import numpy as np
import datetime


font = {'size'   : 10}

plt.rc('font', **font)

sns.set_palette(sns.color_palette("Dark2",10))


hoy = datetime.date.today() - datetime.timedelta(days=1)
hoymenos14 = hoy - datetime.timedelta(days=14)

print(hoy)

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
datos = pd.read_csv("new_cases.csv") 

#Calculamos la media móvil de los últimos 14 días
datos['moving14'] = datos['Spain'].transform(lambda x: x.rolling(14, 1).mean())
#Calculamos la media móvil de los últimos 7 días
datos['moving7'] = datos['Spain'].transform(lambda x: x.rolling(7, 1).mean())

spain_df = datos[['date','Spain','moving14','moving7']]

print(spain_df)

fig, ax = plt.subplots(1,1)


grafico = sns.barplot(ax=ax,
                      x="date", 
                      y="Spain",                   
                      data=spain_df, 
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
    x="date",
    y="moving14",
    data=spain_df, 
    label="Media Movil 14"
    )

#Gráfico de líneas media móvil de los últimos 7 días
graficomv7 = sns.lineplot(
    ax=ax,
    x="date",
    y="moving7",
    data=spain_df, 
    label="Media Movil 7"    
)#.set_title('Nuevos Casos de Coronavirus')


plt.legend()
plt.suptitle("Nuevos Casos de Coronavirus en España a " + hoy.strftime("%d/%m/%Y"), fontsize=18)
plt.xlabel('Fecha', fontsize=16)
plt.ylabel('Nuevos Casos', fontsize=16)


plt.xticks(rotation=90, horizontalalignment='right',fontsize=5)


plt.show()



#print(spain_df.head(5))
#print(spain_df.tail(15))








