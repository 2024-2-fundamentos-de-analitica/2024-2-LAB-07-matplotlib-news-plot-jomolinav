"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os 
path = "files/input/news.csv"
archivo = pd.read_csv(path, index_col=0)

for col in archivo.columns:
    plt.plot(archivo[col], label=col)

plt.title("Como ven noticias(❁´◡`❁)")    
plt.legend(loc="upper right")


plt.savefig("files/plots/news.png")
plt.close()





def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
