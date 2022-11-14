import pandas as pd
import matplotlib.pyplot as plt

def grafico():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Jesus\\programacion\\aguaprogramacion.csv")
    df = datos[["Ús","any_","m3_registrats","núm_clients","ObjectId","CODI_ENS","NOM_ENS"]]
    df = datos.rename(columns={
        "Ús": "USOS",
        "any_": "AÑO",
        "m3_registrats": "M3",
        "núm_clients": "NUMERO_DE_CLIENTES",
        "ObjectId": "OBJETIVOS",
        "CODI_ENS": "CODIGO",
        "NOM_ENS": "NOMBRE_EMPRESA"
    })

    valor_por_ciudad = df.groupby("NUMERO_DE_CLIENTES")["M3"].mean()
    valor_por_ciudad.head(10).plot.barh()
    plt.show()

grafico()



