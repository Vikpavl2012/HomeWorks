class Human:
    default_name = "Name"
    default_age = 1

    @staticmethod
    def default_info():
        print(f'default name:{Human.default_name}')
        print(f'default age:{Human.default_age}')
        
    
    def __init__(self,name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__house = None
        self.__money = 0

    def display_info(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'House:{self.__house}')
        print(f'Money:{self.__money}')


    def __make_deal(self, house_to_buy, house_price):
        self.__money -= house_price
        self.__house = house_to_buy


    def earn_money(self, income):
        self.__money += income

            
    def buy_house(self, home, discount):
        if self.__money >= home.final_price(discount):
            self.__make_deal(home, home.final_price(discount))
        else:
            print('На вашем счету недостаточно средств.')

class House:
    def __init__(self, area = 0, price = 0):
        self._area = area 
        self._price = price

    def final_price(self, discount):
        fp = self._price - self._price/100*discount
        return fp
    
            

class SmallHouse(House):
    def __init__(self): 
        super().__init__(area = 40, price = 1000000)
        

    def display_info(self):
        print(f'Area:{self._area}, {self._price}')
        

hum1 = Human('Popka Myravya', 22)
hum1.display_info()

object = SmallHouse()
object.display_info()

hum1.buy_house(object, 10)

hum1.earn_money(900001)

hum1.buy_house(object, 10)
hum1.display_info()

