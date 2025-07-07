"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt
def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    df = pd.read_csv('files/input/news.csv', index_col=0)
    df.index.name = 'Year'

    #orden original
    fuentes = ['Television', 'Newspaper', 'Radio', 'Internet']
    df = df[fuentes]

    estilos = {
        'Television': {'color': 'black',     'ancho': 2},
        'Newspaper':  {'color': 'gray',      'ancho': 2},
        'Radio':      {'color': 'lightgray','ancho': 2},
        'Internet':   {'color': 'dodgerblue','ancho': 3},
    }


    fig, ax = plt.subplots(figsize=(8, 6))

    # trazar cada serie y etiquetar inicio y fin
    for medio in fuentes:
        datos = df[medio]
        estilo = estilos[medio]
        ax.plot(
            datos.index, datos.values,
            label=medio,
            color=estilo['color'],
            linewidth=estilo['ancho']
        )
        # punto inicial
        ax.scatter(datos.index[0], datos.iloc[0], color=estilo['color'])
        ax.text(
            datos.index[0] - 0.2, datos.iloc[0],
            f"{medio} {datos.iloc[0]}%",
            ha='right', va='center'
        )
        # punto final
        ax.scatter(datos.index[-1], datos.iloc[-1], color=estilo['color'])
        ax.text(
            datos.index[-1] + 0.2, datos.iloc[-1],
            f"{datos.iloc[-1]}%",
            ha='left', va='center'
        )

    #estilo generales
    ax.set_title('How people get their news', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_xticks(df.index)
    ax.set_yticks([])
    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
    ax.legend()

    

    os.makedirs('files/plots', exist_ok=True)
    fig.savefig('files/plots/news.png', bbox_inches='tight')
    plt.close(fig)