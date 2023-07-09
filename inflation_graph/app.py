from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    # Leer los datos de inflación desde el archivo CSV
    data = pd.read_csv('inflacion.csv')

    # Obtener los años
    years = data['Año']

    # Obtener los datos de inflación para Argentina, UE, EE.UU. y el mundo
    argentina = data['Argentina']
    ue = data['UE']
    eeuu = data['EE.UU']
    mundo = data['Mundo']

    # Crear el gráfico
    plt.plot(years, argentina, label='Argentina')
    plt.plot(years, ue, label='UE')
    plt.plot(years, eeuu, label='EE.UU')
    plt.plot(years, mundo, label='Mundo')

    plt.xlabel('Año')
    plt.ylabel('Inflación')
    plt.title('Inflación en Argentina, UE, EE.UU. y el Mundo')
    plt.legend()

    # Guardar el gráfico en un archivo
    plt.savefig('static/inflacion.png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
