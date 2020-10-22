from Act9 import Particula
class Particulas:
    def __init__(self):
        self.__particulas= []
    def agregar_final(self, particula):
        self.__particulas.append(particula)
    def agregar_inicio(self, particula):
        self.__particulas.insert(0, particula)
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01= Particula(6,64,6,6)
p02= Particula(6,31,23, 50)
particulas = Particulas()
particulas.agregar_final(p01)
particulas.agregar_inicio(p02)
particulas.mostrar()