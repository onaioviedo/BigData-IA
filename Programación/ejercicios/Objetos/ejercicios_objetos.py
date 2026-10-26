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
    
    def describir(self):
        return f"{self.marca} {self.modelo}"
    
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
        

cocheElectrico = CocheElectrico("Tesla", "Model S", 600)
print(cocheElectrico.describir())

'''4. Sobrescribir un método heredado'''
class Motor():
    def __init__(self, modelo):
        self.modelo = modelo

    def Arrancar(self):
        return print("Motor en marcha")

class MotorElectrico(Motor):
    def Arrancar(self):
        return print("Motor eléctrico en marcha")

class MotorGasolina(Motor):
    def Arrancar(self):
        return print("Motor de gasolina en marcha")

class MotorDiesel(Motor):
    def Arrancar(self):
        return print("Motor diésel en marcha")

cocheElectrico = MotorElectrico("Tesla")
cocheElectrico.Arrancar()

cocheGasolina = MotorGasolina("Ford")
cocheGasolina.Arrancar()

'''5. Utilizar el polimorfismo'''

def poner_en_marcha(motor):
    motor.Arrancar()    

motores = [MotorGasolina("Ford"), MotorElectrico("Tesla"), MotorDiesel("Volvo")]

for motor in motores:
    poner_en_marcha(motor)


'''6. Ampliar un método heredado con super()'''
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
    def describir(self):
        return super().describir() + f". Autonomía: {self.autonomia_km} km."

cocheElectrico = CocheElectrico("Tesla", "Model S", 600)
print(cocheElectrico.describir())
print(cocheElectrico.marca, cocheElectrico.modelo, cocheElectrico.autonomia_km)

'''7. Mostrar datos con f-strings'''
marca = "Seat"
modelo = "Ibiza"
año = 2020

print(f"El coche es un {marca} {modelo} del año {año}.")

# Prueba: cambia los valores y vuelve a ejecutar el mismo print
marca = "Renault"
modelo = "Clio"
año = 2018

print(f"El coche es un {marca} {modelo} del año {año}.")

'''8. Gestionar una entrada incorrecta con try y except'''
entrada = input("Kilómetros recorridos: ")

try:
    kilometros = int(entrada)
    print("Kilómetros indicados:", kilometros)
except ValueError:
    print("Debes escribir un número entero.")

print("Programa finalizado.")