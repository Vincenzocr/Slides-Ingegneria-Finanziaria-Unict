# Questo in Python 3 è un commento che non influisce nell'esecuzione del codice

# Importare un modulo esterno
import math

# Stampare un output a video
print("Hello world!")
print(math.pi)

# Stampare una concatenazione di stringhe e variabili
myAge = 33
myName = "Vincenzo"
print("ciao mi chiamo " + myName + " e ho compiuto", myAge, "anni")

# richiedere la digitazione di un input da terminale
print("Qual' è il tuo nome?")
# yourName = input()

# Ciclo for
for i in range(1, myAge):
    if i < 18:
        print("Ho festeggiato il mio ", i, "° compleanno")
    else:
        if i < 25:
            print("Sono ormai grande per festeggiare")
        else:
            print("è la", i - 24, "° volta che posso votare al senato della Repubblica")

# Ciclo While

while myAge > 18:
    myAge -= 1
    print("A", myAge, "anni ero già maggiorenne")

# Richiedere il tipo dato di una variabile
print(type(myAge))
print(type(myName))

# Strutture dati native in Python

# Liste
myList = list()
myAlternativeList = []

# Dizionari
myDictionary = dict()
myAlternativeDictionary = {"nome": myName, "età": myAge}

# Aggiungere uno o più elementi in coda
myList.append(myName)
print(myList)
print(myAlternativeDictionary)


for i in range(1, 20):
    myAlternativeList.append(i)

# Indexing
print(myAlternativeList[5])
print(myAlternativeDictionary["nome"])

# Slicing
print(myAlternativeList[10:])

try:
    print(myAlternativeList[100])
except IndexError:
    print("Attenzione! Indice non presente nella lista!")


# Definire una funzione
def somma(primoAddendo, secondoAddendo):
    return primoAddendo + secondoAddendo

print(somma(10, 0.5))


# Classi
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

mySelf = Persona(myName, myAge)
print(mySelf.age)


# Definizione di classe più generale
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Ereditarietà: costruzione di sottoclasse (classe figlia) più paricolare
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

quadrato = Square(5)
print(quadrato.area())





