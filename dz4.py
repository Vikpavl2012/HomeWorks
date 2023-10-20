#Задача 3
class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205
   
    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def kg(self,kg):
        if isinstance(kg,(int, float)):
            self.__kg = kg
        else: print('Килограммы задаются только числами')


kg1 = KgToPounds(23)
print(kg1.to_pounds())
print(kg1.kg)
kg1.kg = 66
print(kg1.kg)
kg1.kg = 'двадцать три'