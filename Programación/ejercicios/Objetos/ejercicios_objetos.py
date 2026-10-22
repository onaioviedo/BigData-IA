'''1. Crear una clase y sus objetos'''
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo



coche1 = Coche("Mercedes", "Seyn")
coche2 = Coche("Audi", "A4")

print(coche1.marca, coche1.modelo)
print(coche2.marca, coche2.modelo)

coche1.modelo = "Clase C"

print(coche1.marca, coche1.modelo)
print(coche2.marca, coche2.modelo)

'''2. Modificar el estado de un objeto'''

class CochePruebas:
    def __init__(self):
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10

    def detener(self):
        self.velocidad = 0

coche1 = CochePruebas()
coche2 = CochePruebas()

coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()

coche2.acelerar()
coche2.acelerar()
coche2.acelerar()
coche2.acelerar()
coche2.acelerar()
coche2.detener()

print(coche1.velocidad)
print(coche2.velocidad)

'''3. Heredar atributos y métodos'''

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def Describir(self):
        return print(self.marca, self.modelo)
    
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
        
    def super().describir():
