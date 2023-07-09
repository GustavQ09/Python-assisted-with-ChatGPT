import tkinter as tk
from tkinter import font

def calcular_regla_de_tres():
    try:
        numero1 = float(entry1.get())
        numero2 = float(entry2.get())
        numero3 = float(entry3.get())

        resultado = (numero3 * numero2) / numero1

        label_resultado.config(text=f"El resultado es: {resultado}")
    except ValueError:
        label_resultado.config(text="¡Error! Ingresa solo números")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de regla de tres")
ventana.configure(bg="white")

# Configurar la fuente
font_size = font.Font(size=14)

# Crear los widgets del formulario
label1 = tk.Label(ventana, text="Número 1:", font=font_size, bg="white")
label2 = tk.Label(ventana, text="Número 2:", font=font_size, bg="white")
label3 = tk.Label(ventana, text="Número 3:", font=font_size, bg="white")
entry1 = tk.Entry(ventana, font=font_size)
entry2 = tk.Entry(ventana, font=font_size)
entry3 = tk.Entry(ventana, font=font_size)
boton_calcular = tk.Button(ventana, text="Calcular", font=font_size, command=calcular_regla_de_tres)
label_resultado = tk.Label(ventana, text="", font=font_size, bg="white")

# Ubicar los widgets en una cuadrícula
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)
boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ajustar el tamaño de las celdas de la cuadrícula
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(3, weight=1)

# Iniciar el bucle de eventos
ventana.mainloop()
