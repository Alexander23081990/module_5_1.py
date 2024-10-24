class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = int(floors)


    def go_to(self, new_floor):
        int(new_floor)
        i = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'В доме {self.name} Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(f' {self.name}, этаж {i}')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)