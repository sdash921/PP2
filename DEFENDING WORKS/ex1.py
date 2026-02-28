class person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def calculate_age(self):
        if int(self.id[0:2]) < 26:
            return 25 - int(self.id[0:2])
        else:
            return 100 - int(self.id[0:2])
p = person("0811251231","Aman",34)
print(p.calculate_age())