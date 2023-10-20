class Alphabet:
    def __init__(self, lang = "en", letters = []):
        self.__lang = lang
        self.__letters = letters

    def print(self):
        print(self.__letters)
    
    def letters_num(self):
        return len(self.__letters)
    

a = ['a', 'b', 'c', 'q', 'u']
a.append('r')

alf1 = Alphabet(letters=a)
alf1.print()
print(alf1.letters_num())