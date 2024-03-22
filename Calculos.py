from tkinter import messagebox

class calcular:
    def __init__(self,nombre , apellido,  salario, porcentaje, dias):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.porcentaje = porcentaje
        self.dias = dias

    def aumento(self):
        salarioConTransporte = 0
        porcentajeAumento = (self.porcentaje / 100) * self.salario
        salarioConAumento = self.salario + porcentajeAumento
        if self.salario <= 2600000:
            salarioConTransporte = salarioConAumento + 104606

        return salarioConAumento, salarioConTransporte

    def prima(self):
        prima = (self.salario * self.dias) / 360
        return prima

    def cesantias(self):
        cesantia = (self.salario * self.dias) / 360
        return cesantia

    def intereses(self):
        cesantias = self.cesantias()
        interes = (cesantias * self.dias * 0.12) / 360
        return interes

    def vacaciones(self):
        vacaciones = (self.salario * self.dias) / 720
        return vacaciones

    def calcularLiquidacion(self):
        prima = self.prima()
        cesantias = self.cesantias()
        interes = self.intereses()
        vacaciones = self.vacaciones()
        total = prima + cesantias + interes + vacaciones
        return total
    
    def exportar(self):
        nombre = self.nombre
        apellido = self.apellido
        salarioAumento, salarioTrans = self.aumento()
        prima = self.prima()
        cesantias = self.cesantias()
        interes = self.intereses()
        vacaciones = self.vacaciones()
        total = self.calcularLiquidacion()

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