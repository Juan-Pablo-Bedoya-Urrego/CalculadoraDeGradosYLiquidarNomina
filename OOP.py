class convertir():
    def __init__(self, numero):
        self.numero=numero

    def celsius_fahrenheit(self):
        self.resultadoFahrenheit= self.numero*9/5 + 32
        return round(self.resultadoFahrenheit,1)

    def fahrenheit_celsius(self):
        self.resultadoCelsius = (self.numero - 32) * 5/9
        return round(self.resultadoCelsius,1)

    def exportarArchivo(self):
        numero= self.numero
        resultadoFahrenheit= self.celsius_fahrenheit()
        resultadoCelsius= self.fahrenheit_celsius()

        numeroIngresado = f'Grados ingresados: {numero}\n'
        fahrenheit = f'El equivalente a Fahrenheit: {resultadoFahrenheit} \n'
        celsius = f'El equivalente a Celsius: {resultadoCelsius}'

        try:
            archivo = open("convertidor_grados.txt", "w")
            archivo.write(numeroIngresado)
            archivo.write(fahrenheit)
            archivo.write(celsius)
        except Exception as e:
            print(e)

        finally:
            archivo.close()