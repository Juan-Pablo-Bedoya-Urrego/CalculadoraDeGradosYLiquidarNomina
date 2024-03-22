from tkinter import messagebox

class exportacion:

    def __init__(self,nombre,apellido,salarioAumento,salarioTrans,prima,cesantias,interes,vacaciones,total):
        self.nombre = nombre
        self.apellido = apellido
        self.salarioAumento = salarioAumento
        self.salarioTrans = salarioTrans
        self.prima = prima
        self.cesantias = cesantias
        self.interes = interes
        self.vacaciones = vacaciones
        self.total = total
        

    def exportar(self):
        nombre = self.nombre
        apellido = self.apellido
        salarioAumento = self.salarioAumento
        salarioTrans = self.salarioTrans
        prima = self.prima
        cesantias = self.cesantias
        interes = self.interes
        vacaciones = self.vacaciones
        total = self.total

        nombreExportar = f"Nombre = {nombre}\n"
        apellidoExportar = f"Apellido = {apellido}\n"
        primaExportar = f"Prima Empleado= {prima}\n"
        cesantiasExportar = f"Cesantias causa empleado = {cesantias}\n"
        interesExportar = f"Intereses causa de las cesantias = {interes}\n"
        vacacionesExportar = f"Vacaciones a la fecha = {vacaciones}\n"
        salarioAumentoExportar = f"Salario con aumento = {salarioAumento}\n"
        salarioTransporteExportar = f"Salario con sub transporte = {salarioTrans}\n"
        totalExportar = f"Total liquidacion = {total}"

        try:
            archivo = open("Resultados.txt","w")
            archivo.write(nombreExportar)
            archivo.write(apellidoExportar)
            archivo.write(primaExportar)
            archivo.write(cesantiasExportar)
            archivo.write(interesExportar)
            archivo.write(vacacionesExportar)
            archivo.write(salarioAumentoExportar)
            archivo.write(salarioTransporteExportar)
            archivo.write(totalExportar)
            messagebox.showinfo('Exportacion','Se exporto correctamente')
        except Exception as e:
            print(e)

        finally:
            archivo.close()