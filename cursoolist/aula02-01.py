kind = "blank"
 
def test_kind():
    print("Test Kind:", kind)
 
class Dog:
    kind = 'canine' #campo estático à classe
 
    def __init__(self, name):
        #definir todos os atributos no __init__
        self.name = name
 
    def what_kind(self):
        print("Name:", self.name)
        print("Geral:", kind)
        print("Self:", self.kind)
 
Dog.kind = 'Lassie' 
# Testes...
d = Dog('Fido')
e = Dog('Buddy')
 
test_kind()
print('-' * 40)

#d.kind = 'Shitzu' 
d.what_kind()

print('-' * 40)
e.what_kind()
print('-' * 40)
 
print(Dog)
print(Dog.what_kind)
print(e)
print(e.what_kind)


# para chamar um método de uma classe pai:
#BaseClassName.methodname(self, arguments)
#ou
#super().methodname(arguments)

#variaveis privadas = __nomedavariavel ou _nomedavariavel


class Reverse:
    """ Iterator for looping ober a sequence backwards"""
    def __init__(self):
    
    def _next_:

    def __iter__(self):
       ''' Returns the Iterator object '''
       return self;
