import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


hoy = datetime.date.today()

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="admin",
                               db="covid_madrid"))

conn = engine.connect()


#Cargamos la tabla completa
#generator_df = pd.read_sql_table('casos_municipio',
#                                 con=conn                         
#                                 )


query ="SELECT * FROM casos_municipio where casos_confirmados_activos_ultimos_14dias is not null"
generator_df = pd.read_sql(sql=query,  # mysql query
                           con=conn #,
                           #chunksize=chunksize  # size you want to fetch each time
                           )  

    
#Eliminamos los datos que tienen NaN y los sustituimos por cero
generator_df.fillna(0)



fig, ax = plt.subplots(1,1)


grafico = sns.barplot(ax=ax,
                      x="municipio_distrito", 
                      y="casos_confirmados_activos_ultimos_14dias",                   
                      data=generator_df, 
                      label="Casos Confirmados Activos Últimos 14 días")


plt.legend()
plt.suptitle("Casos Confirmados Activos Últimos 14 días en Madrid a " + hoy.strftime("%m/%d/%Y"), fontsize=18)
plt.xlabel('Municipio-Distrito', fontsize=16)
plt.ylabel('Casos Confirmados Activos Últimos 14 días', fontsize=16)

plt.xticks(rotation=90, horizontalalignment='right',fontsize=7)

plt.show()


#query ="SELECT * FROM casos_municipios "

#generator_df = pd.read_sql(sql=query,  # mysql query
#                           con=conn,
#                           chunksize=chunksize)  # size you want to fetch each time

#for dataframe in generator_df:
#    for row in dataframe:
#        pass  # whatever you want to do
       