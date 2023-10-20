'''
#Задача 1
class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')

drink1 = Soda()
drink2 = Soda('клубника')
drink3 = Soda()
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()
'''

#Задача 2
class Tomato:
    type = 'Tomato'
    states = ['отсутствует','цветение','зелёный','красный']


def __init__(self,index,state):
    self._index = index
    self._state = state

    

class TomatoBush:
    def __init__(self,):
        pass
bush = []
print(bush)
N = 7
for i in range(N):
    bush.append(i**1)
    print(bush[i])



class Gardener:
    def __init__(self,name,plant):
        self.name = name
        self._plant = plant


