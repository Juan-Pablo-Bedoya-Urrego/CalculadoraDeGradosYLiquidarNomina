import sys
from tkinter import ttk, messagebox, Menu
import tkinter as tk
from Calculos import *

ventanaInicio = tk.Tk()
ventanaLiquidacion = tk.Tk()
ventanaLiquidacion.withdraw()
ventanaLiquidacion.geometry("600x600")
ventanaLiquidacion.title("Liquidacion")
ventanaInicio.geometry("150x200")
ventanaInicio.title("Inicio de Seccion")

def integrantes():
    messagebox.showinfo('Integrantes','Juan Pablo Bedoya Urrego \n Mariana Jaramillo Jaramillo')

def salir():
    ventanaLiquidacion.quit()
    ventanaLiquidacion.destroy()
    sys.exit()

def archivo():
    entradaNombre.delete(0,tk.END)
    entradaApellido.delete(0,tk.END)
    entradaDias.delete(0,tk.END)
    entradaSalario.delete(0,tk.END)
    entradaAumento.delete(0,tk.END)
    nombreLbl.config(text="")
    apellidoLbl.config(text="")
    primaLbl.config(text="")
    CesantiasLbl.config(text="")
    interesLbl.config(text="")
    vacacionesLbl.config(text="")
    salarioAumentoLbl.config(text="")
    salarioTransporteLbl.config(text="")
    totalLbl.config(text="")

def BTNExportar():
    nombre = entradaNombre.get()
    apellido = entradaApellido.get()
    dias_laborados = int(entradaDias.get())
    salario = float(entradaSalario.get())
    aumento = float(entradaAumento.get())

    calcu = calcular(nombre, apellido, salario, aumento, dias_laborados)

    calcu.exportar()

    archivo()

def BTNcalcular():
    nombre = entradaNombre.get()
    apellido = entradaApellido.get()
    dias_laborados = int(entradaDias.get())
    salario = float(entradaSalario.get())
    aumento = float(entradaAumento.get())

    global nombreLbl,apellidoLbl,primaLbl,CesantiasLbl,interesLbl,vacacionesLbl,salarioAumentoLbl,salarioTransporteLbl,totalLbl

    calc = calcular(nombre, apellido, salario, aumento, dias_laborados)

    salau, salt = calc.aumento()

    nombreLbl = ttk.Label(ventanaLiquidacion, text=nombre)
    nombreLbl.grid(row=6, column=0, padx=3, pady=1)

    apellidoLbl = ttk.Label(ventanaLiquidacion, text=apellido)
    apellidoLbl.grid(row=6, column=3, padx=3, pady=1)

    prima = ttk.Label(ventanaLiquidacion, text="Prima Empleado: ")
    prima.grid(row=7, column=0, padx=3, pady=1)

    primaLbl = ttk.Label(ventanaLiquidacion, text=calc.prima())
    primaLbl.grid(row=7, column=3, padx=3, pady=1)

    Cesantias = ttk.Label(ventanaLiquidacion, text="Cesantias causadas empleado: ")
    Cesantias.grid(row=8, column=0, padx=3, pady=1)

    CesantiasLbl = ttk.Label(ventanaLiquidacion, text=calc.cesantias())
    CesantiasLbl.grid(row=8, column=3, padx=3, pady=1)

    interes = ttk.Label(ventanaLiquidacion, text="Interes causado de las fechas ")
    interes.grid(row=9, column=0, padx=3, pady=1)

    interesLbl = ttk.Label(ventanaLiquidacion, text=calc.intereses())
    interesLbl.grid(row=9, column=3, padx=3, pady=1)

    vacaciones = ttk.Label(ventanaLiquidacion, text="Vacaciones")
    vacaciones.grid(row=10, column=0, padx=3, pady=1)

    vacacionesLbl = ttk.Label(ventanaLiquidacion, text=calc.vacaciones())
    vacacionesLbl.grid(row=10, column=3, padx=3, pady=1)

    salarioAumento = ttk.Label(ventanaLiquidacion, text="Salario aumento")
    salarioAumento.grid(row=11, column=0, padx=3, pady=1)

    salarioAumentoLbl = ttk.Label(ventanaLiquidacion, text=salau)
    salarioAumentoLbl.grid(row=11, column=3, padx=3, pady=1)

    salarioTransporte = ttk.Label(ventanaLiquidacion, text="Salario con sub transporte")
    salarioTransporte.grid(row=12, column=0, padx=3, pady=1)

    salarioTransporteLbl = ttk.Label(ventanaLiquidacion, text=salt)
    salarioTransporteLbl.grid(row=12, column=3, padx=3, pady=1)

    total = ttk.Label(ventanaLiquidacion, text="Total liquidacion")
    total.grid(row=13, column=0, padx=3, pady=1)

    totalLbl = ttk.Label(ventanaLiquidacion, text=calc.calcularLiquidacion())
    totalLbl.grid(row=13, column=3, padx=3, pady=1)


def VentanaCalculo():
    ventanaLiquidacion.deiconify()

    global  entradaNombre, entradaApellido, entradaDias, entradaSalario, entradaAumento

    menuP = Menu(ventanaLiquidacion)
    submenu_archivo = Menu(menuP,tearoff=0)
    submenu_archivo.add_command(label='Archivo', command=archivo)

    menuP.add_cascade(menu=submenu_archivo,label='Archivo')
    submenu_archivo.add_command(label='salir',command=salir)

    submenu_ayuda = Menu(menuP,tearoff=0)
    submenu_ayuda.add_command(label="Acerca del Proyecto", command=integrantes)

    menuP.add_cascade(menu=submenu_ayuda, label='Acerca del proyecto')

    ventanaLiquidacion.config(menu=menuP)

    labelNombre = ttk.Label(ventanaLiquidacion, text="Ingrese el nombre:")
    labelNombre.grid(row=0, column=0, padx=3, pady=1)

    entradaNombre = ttk.Entry(ventanaLiquidacion, width=20, justify=tk.LEFT)
    entradaNombre.grid(row=0, column=1, padx=3, pady=1)

    labelApellido = ttk.Label(ventanaLiquidacion, text="Ingrese el apellido:")
    labelApellido.grid(row=1, column=0, padx=3, pady=1)

    entradaApellido = ttk.Entry(ventanaLiquidacion, width=20, justify=tk.LEFT)
    entradaApellido.grid(row=1, column=1, padx=3, pady=1)

    labelDias = ttk.Label(ventanaLiquidacion, text="Ingrese el dias laborados:")
    labelDias.grid(row=2, column=0, padx=3, pady=1)

    entradaDias = ttk.Entry(ventanaLiquidacion, width=20, justify=tk.LEFT)
    entradaDias.grid(row=2, column=1, padx=3, pady=1)

    labelSalario = ttk.Label(ventanaLiquidacion, text="Ingrese salario:")
    labelSalario.grid(row=3, column=0, padx=3, pady=1)

    entradaSalario = ttk.Entry(ventanaLiquidacion, width=20, justify=tk.LEFT)
    entradaSalario.grid(row=3, column=1, padx=3, pady=1)

    labelAumento = ttk.Label(ventanaLiquidacion, text="Ingrese el aumento en %:")
    labelAumento.grid(row=4, column=0, padx=3, pady=1)

    entradaAumento = ttk.Entry(ventanaLiquidacion, width=20, justify=tk.LEFT)
    entradaAumento.grid(row=4, column=1, padx=3, pady=1)

    botonCalcular = ttk.Button(ventanaLiquidacion, text="Calcular", command=BTNcalcular)
    botonCalcular.grid(row=5, column=0, padx=3, pady=1)

    botonExportar = ttk.Button(ventanaLiquidacion, text="Exportar", command=BTNExportar)
    botonExportar.grid(row=5, column=5, padx=3, pady=1)

    ventanaLiquidacion.mainloop()

def validarUsuario():
    banderaUsuario = True
    banderaContraseña = True
    Usuario = "Admin"
    Contreña = "Admin"
    UsuarioTeclado = EntradaUsuario.get()
    ContraseñaTeclado = EntradaContraseña.get()
    if not Usuario == UsuarioTeclado:
        messagebox.showerror('Error Usuario', 'El usuario es incorrecto')
        banderaUsuario = False
    else:
        banderaUsuario = True

    if not Contreña == ContraseñaTeclado:
        messagebox.showerror('Error Contrasela', 'La contraseña es incorrecta')
        banderaContraseña = False
    else:
        banderaContraseña = True

    if banderaUsuario and banderaContraseña:
        ventanaInicio.destroy()
        VentanaCalculo()

LabelUsuario = ttk.Label(ventanaInicio, text="Usuario:")
LabelUsuario.grid(row=0, column=0, padx=3, pady=1)

EntradaUsuario = ttk.Entry(ventanaInicio, width=20, justify=tk.LEFT)
EntradaUsuario.grid(row=1, column=0, padx=3, pady=1)

LabelContraseña = ttk.Label(ventanaInicio, text="Contraseña:")
LabelContraseña.grid(row=2, column=0, padx=3, pady=1)

EntradaContraseña = ttk.Entry(ventanaInicio, show="*", width=20, justify=tk.LEFT)
EntradaContraseña.grid(row=3, column=0, padx=3, pady=1)

botonInicio = ttk.Button(ventanaInicio, text="Entrar", command=validarUsuario)
botonInicio.grid(row=4, column=0, padx=10, pady=5)

ventanaInicio.mainloop()
