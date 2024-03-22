from exportacion import * 

class Trabajor:
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

    def calcular_Liquidacion(self):
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
        total = self.calcular_Liquidacion()
        e = exportacion(nombre,apellido,salarioAumento,salarioTrans,prima,cesantias,interes,vacaciones,total)

        e.exportar()