"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os 







def pregunta_01():
    path = "files/input/news.csv"
    archivo = pd.read_csv(path, index_col=0)

    for col in archivo.columns:
        plt.plot(archivo[col], label=col)

    plt.title("Como ven noticias")    


    newpath = "files/plots"
    if not os.path.exists(newpath):
        os.makedirs(newpath, exist_ok=True)

    plt.savefig("files/plots/news.png")
pregunta_01()