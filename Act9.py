from algoritmo import distancia_euclidiana
class Particula:
    def __init__(self, x_1, y_1, x_2, y_2):
        self.__id=4
        self.__origen_x = x_1
        self.__origen_y = y_1
        self.__destino_x = x_2
        self.__destino_y = y_2
        self.__velocidad= 55
        self.__red= 350
        self.__green= 400
        self.__blue= 450
        self.__distancia= distancia_euclidiana(x_1,y_1, x_2, y_2)
    def __str__(self):
        return(
            'id: ' + str(self.__id) + '\n' +
            'Origen en x: ' + str(self.__origen_x) + '\n' +
            'Origen en y: ' + str(self.__origen_y) + '\n' +
            'Destino en x: ' + str(self.__destino_x) + '\n' +
            'Destino en y: ' + str(self.__destino_y) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n'
        )