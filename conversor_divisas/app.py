from flask import Flask, render_template, request
import requests

app = Flask(__name__)

url = "https://api.apilayer.com/exchangerates_data/convert"
api_key = "Your API key"

# Ruta principal de la aplicación
@app.route('/', methods=['GET', 'POST'])
def convert_currency():
    if request.method == 'POST':
        to_currency = request.form['to_currency']
        from_currency = request.form['from_currency']
        amount = request.form['amount']

        # Verifica si el valor de la cantidad está vacío o no es un número
        if not amount or not amount.isdigit():
            error_message = "Ingrese una cantidad válida"
            return render_template('index.html', error_message=error_message)

        # Realiza la conversión de divisas
        conversion_result = perform_conversion(to_currency, from_currency, float(amount))

        # Si la conversión fue exitosa, muestra el resultado en la plantilla
        if conversion_result:
            return render_template('index.html', result=conversion_result)

    # Muestra la plantilla con el formulario
    return render_template('index.html')


# Función para realizar la conversión de divisas
def perform_conversion(to_currency, from_currency, amount):
    # Parámetros de la solicitud a la API
    payload = {
        "to": to_currency,
        "from": from_currency,
        "amount": amount
    }

    # Encabezados de la solicitud a la API
    headers = {
        "apikey": api_key
    }

    # Realiza la solicitud GET a la API de conversión de divisas
    response = requests.get(url, headers=headers, params=payload)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtiene el resultado de la conversión en formato JSON
        result = response.json()
        return result

    # Si la solicitud no fue exitosa, retorna None
    return None


# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    # Inicia la aplicación Flask en modo de depuración
    app.run(debug=True)
