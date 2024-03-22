import tkinter as tk
from tkinter import ttk, messagebox
from OOP import *

frame=tk.Tk()
frame.geometry("600x200")
frame.title("Convertidor de grados")
def btnFahrenheit():
    resultado= convertir(float(txtNumero.get()))
    global lblResultadoFahrenheit
    lblResultadoFahrenheit= ttk.Label(frame,text=resultado.celsius_fahrenheit())
    lblResultadoFahrenheit.grid(row=6, column=3, padx=6, pady=6)
def btnCelsius():
    resultado= convertir(float(txtNumero.get()))
    global  lblResultadoCelsius
    lblResultadoCelsius = ttk.Label(frame,text=resultado.fahrenheit_celsius())
    lblResultadoCelsius.grid(row=7, column=3, padx=6, pady=6)
def btnExportar():
    resultado = convertir(float(txtNumero.get()))
    resultado.exportarArchivo()
    txtNumero.delete(0, tk.END)
    lblResultadoFahrenheit.config(text="")
    lblResultadoCelsius.config(text="")
    messagebox.showinfo("Mensaje Informativo", " Se exporto los datos")

lblTitulo= ttk.Label(frame, text="Convertirdor de grados")
txtNumero= ttk.Entry(frame)
btnFahrenheit=ttk.Button(frame,text="Convertir Fahrenheit", command=btnFahrenheit)
btnCelsius=ttk.Button(frame,text="Convertir celsius", command=btnCelsius)
btnExportar= ttk.Button(frame,text="Exportar", command=btnExportar)
lblConversionFahrenheit= ttk.Label(frame,text="Conversion Fahrenheit")
lblConversionCelsius=ttk.Label(frame,text="Conversion Celsius")

lblTitulo.grid(row=0, column= 4, padx=6, pady=6)
txtNumero.grid(row=4, column=4, padx=6, pady=6)
btnFahrenheit.grid(row=5, column=2,padx=6, pady=6)
btnCelsius.grid(row=5, column=3,padx=6, pady=6)
btnExportar.grid(row=5, column=4,padx=6, pady=6)
lblConversionFahrenheit.grid(row=6, column=2,padx=6, pady=6)
lblConversionCelsius.grid(row=7, column=2,padx=6, pady=6)

frame.mainloop()

