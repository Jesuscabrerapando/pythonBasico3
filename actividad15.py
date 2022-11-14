#1. Crea un proyecto en Pycharm llamado actividad15
#2. Crea una archivo python que muestre 10 números aleatorios entre 1 y 100 y los muestre ordenados
from numpy import random


def numero():
    for i in range(10):
        print(random.randint(1,100))

numero()
#3. Crea otro archivo python que pida una frase y responda cuántas veces está la letra que hayas elegido
def pregunta():
    frase = "¡Hola soy Jesus!"
    print(frase)
    ocurrencias = frase.count("s")
    print(ocurrencias)
pregunta()

#4. Busca un archivo csv en internet y muestra un gráfico circular que muestre los datos
def internet():
    datos = pd.read_csv(C:\\Users\\Tecnicos\\Desktop\\Jesus\\programacion\\farmacias.csv)

internet()
#5. Este proyecto, sus archivos, lo subes a un repositorio Github




