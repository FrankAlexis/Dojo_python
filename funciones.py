#Clase para realizar las operaciones basicas de una calculadora
class dojo:
    #Constructor de la Clase
    #El parametro self hace referencia a los atributos que llegan desde el Constructor
    #lo mismo que this en Java
    def __init__(self, x, y ,s):
        self.menor = x
        self.mayor = y
        self.salto = s
        self.rango = range (menor, mayor, salto)

    def sum (self):
        suma = 0
        for i in self.rango:
            suma = suma + i
        print ("La suma es:", suma)
        return suma
    

print("Ingrese menor:");
menor = int(input());

print("Ingrese mayor:");
mayor = int(input());

print("Ingrese salto:");
salto = int(input());

calcular = dojo(menor, mayor, salto)
calcular.sum()
