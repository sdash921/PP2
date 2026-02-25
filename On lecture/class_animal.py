class Animal(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)

    def get_age(self):
        return self.age

    def set_age(self, newage):
        self.age = newage

def make_animals(L1, L2):
    """ Creates a list of Animal objects """
    animal_list = []
    for i in range(len(L1)):
        new_animal = Animal(L1[i], L2[i])
        animal_list.append(new_animal)
    return animal_list

L1 = [2, 5, 1]
L2 = ["blobfish", "crazyant", "parafox"]

animals = make_animals(L1, L2)

print(animals)  # Prints the list of objects in hexedecimals
for i in animals:
    print(i)    # Prints the individual __str__ representation