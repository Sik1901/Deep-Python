class Animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color

    def me_presento(self):
        print(
            f'Hola, soy {self.especie}, de color {self.edad} y tengo {self.color}')

    def cumplir_anios(self):
        self.edad = self.edad + 1


animal1 = Animal('snausher', 2, 'Marron')
animal2 = Animal('Chihuahua', 3, 'Blanco')

print(animal1.especie)
print(animal2.especie)

print(animal1.me_presento())
print(animal2.me_presento())
