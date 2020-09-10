# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
# метода. Например: 20м*5000м*25кг*5см = 12500 т


class Road:

    def __init__(self, length: float, width: float, thickness: float = 5):
        self._length = length
        self._width = width
        self._thickness = thickness

    def mass(self):
        mass = self._length * self._width * self._thickness * 25
        print(mass)


x = Road(width=20, length=5000)
x.mass()