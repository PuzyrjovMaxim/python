class CatDog(object):
    Total_Objects = 0
    def __init__(self, cat, dog):
        CatDog.Total_Objects += 1
        self.c = cat
        self.d = dog
    @classmethod
    def total_objects(cls):
        print('Total Objects: ', cls.Total_Objects)
    # def __del__(self):
    #     print('Удаление экземпляра класса')
    def getcat(self):
        return self.c
    def getdog(self):
        return self.d
    def getparts(self):
        s = []
        s.append(self.c), s.append(self.d)
        return s
    def climb_tree(self):
        if(self.c>=self.d):
            print('Котопёс умеет лазить по деревьям!')
            return True
        else:
            print('Котопёс упал с дерева(')
            return False
    def bark(self):
        if(self.d>=self.c): print('Woof!')
        else: print('Meow!')
    def eat(self, food, value):
        if(food=='fish'):
            if(self.c + value >100): self.c = 100
            else: self.c += value
            if(self.d - value < 0): self.d = 0
            else: self.d -= value
        elif(food=='meat'):
            if(self.d + value >100): self.d = 100
            else: self.d += value
            if(self.c - value < 0): self.c = 0
            else: self.c -= value
        else: print('Котопёс такое не ест.')
    def __str__(self):
        return 'Котопёс со статами: ' + str(self.c) + ', ' + str(self.d)

class Cosmic_CatDog(CatDog):
    def __str__(self):
        return 'Космический Котопёс со статами: ' + str(self.c) + ', ' + str(self.d)

cd = CatDog(30, 20)
print(cd.getparts())
cd.climb_tree()
cd.bark()
cd.eat('meat', 15)
print(cd.getparts())
cd.climb_tree()
cd.bark()
ccd = Cosmic_CatDog(20,30)
ccd.climb_tree()
print(ccd.getparts())
print(cd)
print(ccd)
CatDog.total_objects()