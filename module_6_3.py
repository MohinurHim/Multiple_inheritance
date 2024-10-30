# Задача "Мифическое наследование":
class Horse:
    def __init__(self):
        self.x_distance = 0 # пройденный путь
        self.sound = 'Frrr' # звук, который издаёт лошадь
        super().__init__()
    def run(self, dx): #изменение дистанции
        self.x_distance += dx
        
class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл (отсылка)
    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
# изменения дистанции
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
# возвращает текущее положение пегаса в виде кортежа
    def get_pos(self):
        return self.x_distance, self.y_distance
#  печатает значение унаследованного атрибута sound
    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()