# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# 5.Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:  # я снова не понял замысел. для чего новые классы, если они не отличаются от базового? :( придумал сам
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, name: str, color: str):
        self.name, self.color = name, color
        self.is_police = False
        self.speed = 0

    def go(self, speed: float):
        self.speed = speed
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')
        self.speed = 0

    def turn(self, direction: str):
        valid = ('налево', 'направо')
        if direction not in valid:
            raise ValueError(f'turn: direction must be one of {valid}.')
        if self.speed == 0:
            raise Exception(f'turn: {Car} requires speed to turn, use go(self, speed: float) first')
        else:
            print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} движется со скоростю {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.color} {self.name} превысила скорость на {self.speed - 60} км/ч')


class SportCar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)
        self.color = self.color + ' с полосочкой'


class WorkCar(Car):
    def __init__(self, name: str):
        super().__init__(name, color='жёлтая')

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.color} {self.name} превысила скорость на {self.speed - 40} км/ч')


class PoliceCar(Car):
    def __init__(self, name: str):
        super().__init__(name, color='белая')
        self.is_police = True
        self.name = 'полицейская ' + self.name


x = TownCar('Мазда', 'чёрная')
x.go(70)
x.show_speed()
x.turn('налево')
x.stop()
x.go(20)
x.show_speed()
x.turn('направо')
print(x.speed, x.color, x.name, x.is_police)

x = SportCar('Феррари', 'красная')
x.go(70)
x.show_speed()
x.turn('налево')
x.stop()
x.go(20)
x.show_speed()
x.turn('направо')
print(x.speed, x.color, x.name, x.is_police)

x = WorkCar('Нива')
x.go(70)
x.show_speed()
x.turn('налево')
x.stop()
x.go(20)
x.show_speed()
x.turn('направо')
print(x.speed, x.color, x.name, x.is_police)

x = PoliceCar('БМВ')
x.go(70)
x.show_speed()
x.turn('налево')
x.stop()
x.go(20)
x.show_speed()
x.turn('направо')
print(x.speed, x.color, x.name, x.is_police)
