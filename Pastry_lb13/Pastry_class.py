class Pastry:

    def __init__(self):
        pass

    def init(self, name, weight, prise, shelf_life, ):
        self.name = name
        self.weight = weight
        self.prise = prise
        self.shelf_life = shelf_life

    def read(self):
        self.name = input(" Какое имя будет у вашего изделия? - ").capitalize()
        self.text_check()
        self.weight = int(input(" Какой будет вес? - "))
        self.prise = int(input(" Какая Будет цена? - "))
        self.shelf_life = int(input("Сколько будет срок годности? - "))

    def text_check(self):
            h = 20
            for i in range(h):
                if not self.name:
                    break
                if not (self.name.isalpha()):
                    print(" Введите имя еще раз\n")
                    self.name = input(" Какое имя будет у вашего изделия? - ").capitalize()
                    h +=3
                else:
                    break

    def display(self):
        print('\n Название нашего изделия - {0},\n Вес в граммах - {1},\n'.format(self.name, self.weight),
              'Цена нашего продукта - {0} рублей,\n Срок годности - {1} Дней'.format(self.prise, self.shelf_life),
              '\n')


class Math:
    def add(self, arg1, arg2):
        obj_Pastry3 = Pastry()
        sum_prise = arg1.prise + arg2.prise
        if arg1.shelf_life < arg2.shelf_life:
            shelf_life_min = arg1.shelf_life
        else:
            shelf_life_min = arg2.shelf_life

        obj_Pastry3.init(arg1.name, arg2.weight, sum_prise, shelf_life_min)
        return obj_Pastry3

obj_Pastry1 = Pastry()
obj_Pastry1.read()
obj_Pastry1.display()

obj_Pastry2 = Pastry()
obj_Pastry2.read()
obj_Pastry2.display()

obj_math = Math()
obj_math.add(obj_Pastry1, obj_Pastry2)

array_Pastry = []
array_Pastry.append(obj_Pastry1)
array_Pastry.append(obj_Pastry2)
comparison_values = int(input("\nВес с которым будете сравнивать - "))
number_Pastry = int(input(" Количество кондитерский изделий - "))
count = 0

for i in range(number_Pastry):
    array_Pastry.append(obj_math.add(array_Pastry[(len(array_Pastry) - 1)], array_Pastry[len(array_Pastry) - 2]))

for f in range(len(array_Pastry)):
    if array_Pastry[f].weight > comparison_values:
        count += 1

print("Количество изделий " + str(count) + " Которые превышает зананное нами число")
