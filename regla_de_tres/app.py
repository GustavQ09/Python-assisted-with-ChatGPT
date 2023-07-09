from flask import Flask, render_template, request

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # Verifica si la solicitud es POST
        try:
            numero1 = float(request.form['numero1'])  # Obtiene el valor del campo 'numero1' del formulario enviado
            numero2 = float(request.form['numero2'])  # Obtiene el valor del campo 'numero2' del formulario enviado
            numero3 = float(request.form['numero3'])  # Obtiene el valor del campo 'numero3' del formulario enviado

            resultado = (numero3 * numero2) / numero1  # Realiza el cálculo de la regla de tres

            return render_template('index.html', resultado=resultado)  # Renderiza la plantilla 'index.html' y pasa el resultado como variable
        except ValueError:  # Si ocurre un ValueError (por ejemplo, si se ingresan caracteres no numéricos)
            error = '¡Error! Ingresa solo números'  # Crea un mensaje de error
            return render_template('index.html', error=error)  # Renderiza la plantilla 'index.html' y pasa el error como variable
    else:  # Si la solicitud es GET
        return render_template('index.html')  # Renderiza la plantilla 'index.html'

if __name__ == '__main__':
    app.run()  # Inicia el servidor web Flask
