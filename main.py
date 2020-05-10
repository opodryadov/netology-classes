class Animals:
    hunger = 'голодный'
    def feed(self):
        self.hunger = 'сытый'
        print(self.hunger)
    def __gt__(self, other):
        return self.weight > other.weight

class Birds(Animals):
    def __init__(self, sound='кукарекает', eggs=10, weight=100, name='Серый'):
        self.sound = sound
        self.eggs = eggs
        self.weight = weight
        self.name = name
    def collect(self, value):
        print(f'Было {self.eggs} яиц')
        self.eggs -= value
        print(f'Собрали {value } яиц')
        print(f'Стало {self.eggs} яиц')

class Smallcattle(Animals):
    sound = 'бекает'
    wool = 'много шерсти'  # шерсть
    def __init__(self, weight=100, name='Барашек'):
        self.weight = weight
        self.name = name
    def shave(self):
        self.wool = 'подстриженный'
        print(self.wool)

class Cattle(Animals):
    sound = 'мычит'
    milk = 5  #молоко(л)
    name = 'Манька'
    weight = 500 #вес(кг)
    def milkcow(self, liters):
        self.milk -= liters
        print(self.milk)

goose1 = Birds(sound='крякает', eggs=2, weight=3, name='Серый')
goose2 = Birds(sound='крякает', eggs=1, weight=2, name='Белый')
cow1 = Cattle()
sheep1 = Smallcattle(weight=100, name='Барашек')
sheep2 = Smallcattle(weight=160, name='Кудрявый')
chicken1 = Birds(sound='кукарекает', eggs=12, weight=1, name='Ко-Ко')
chicken2 = Birds(sound='кукарекает', eggs=14, weight=1, name='Кукареку')
goat1 = Smallcattle(weight=60, name='Рога')
goat2 = Smallcattle(weight=40, name='Копыта')
duck1 = Birds(sound='крякает', eggs=0, weight=1, name='Кряква')

duck1.feed() #покормить Крякву
print(goose1.weight + goose2.weight + cow1.weight + sheep1.weight + sheep2.weight + chicken1.weight +
      + chicken2.weight + goat1.weight + goat2.weight + duck1.weight)
print(max(goose1.weight, goose2.weight, cow1.weight, sheep1.weight, sheep2.weight, chicken1.weight,
      chicken2.weight, goat1.weight, goat2.weight, duck1.weight))
cow1.milkcow(5) #подоить корову
sheep1.shave() #подстричь Барашка
chicken2.collect(12) #собрать яйца у Кукареку
