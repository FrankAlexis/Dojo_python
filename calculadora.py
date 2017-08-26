class calculadora:
    #Constructor de la Clase
    #El parametro self hace referencia a los atributos que llegan desde el Constructor lo mismo que this en Java
    def __init__(self, x, y):
        self.menor = x
        self.mayor = y

        def sum (self):
            suma = self.x + self.y
            return suma

        def rest (self):
            resta = self.x - self.y
            return resta

        def mult (self):
            multiplicacion = self.x * self.y
            return multiplicacion

        def div (self):
            if y != 0:
                division = self.x / self.y
            else:
                print ("No se puede hacer una división entre cero")
            return suma
