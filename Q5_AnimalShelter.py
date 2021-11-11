# Implement cat and dog queue for animal shelter

class AnimalShelter:
    def __init__(self) -> None:
        self.cats=[]
        self.dogs=[]

    def enqueue(self,animal,type):
        if type=='cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats)==0:
            return None
        return self.cats.pop(0)

    def dequeueDog(self):
        if len(self.dogs)==0:
            return None
        return self.dogs.pop(0)

    def dequeueAny(self):
        if len(self.cats)==0:
            return self.dequeueDog()
        return self.dequeueCat()


cq=AnimalShelter()
cq.enqueue('cat1','cat')
cq.enqueue('cat2','cat')
cq.enqueue('Dog1','dog')
cq.enqueue('cat3','cat')
cq.enqueue('Dog2','dog')
print(cq.dequeueAny())
print(cq.dequeueCat())
print(cq.dequeueDog())