class Gift:
    def __init__(self,sex,type,price):
        self.set_sex(sex)
        self.set_type(type)
        self.set_price(price)

    def set_sex(self, sex):
        match sex:
            case 'male' | 'female' | 'child' | 'anyone':
                self.__sex = sex
            case _:
                print("Задайте корректный пол")
                exit()

    def get_sex(self):  
        return self.__sex  
    
    def set_type(self, type):
        match type:
            case 'technique' | 'perfumery' | 'toys' | 'postcards':
                self.__type = type
            case _:
                print("Задайте корректный тип подарка")
                exit()

    def get_type(self):  
        return self.__type    

    def set_price(self, price):
        if price > 0 and price < 3000000:
            self.__price = price
        elif price <= 0:
            print('Задайте корректную цену')
            exit()
        else:
            print('Мы таким дорогим не торгуем')
            exit()

    def get_price(self):
        return self.__price

    

    def display_info(self):
        print(f'sex: {self.__sex}')
        print(f'type: {self.__type}')
        print(f'price: {self.__price}')


gift1 = Gift('male','technique', 10000.00)
gift1.display_info()
gift2 = Gift('etwrce','tdfrre', 0.00)
if gift2 != None:  gift2.display_info()