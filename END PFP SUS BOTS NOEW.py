from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
    # hard part STARTING NOW.
class Human(Animal):

    def move(self):
     print(" I can walk and run! :D")
     print("  Man, We can all do that shush -_-")

class Snake(Animal):

    def move(self):
     print(" I can crawl! :3 ")
     print(" Bro, do you have common sense? *O*")

class Dog(Animal):

    def move(self):
     print(" I can bark! ^.^ ")
     print(" OMG?! ISHOWSPEED'S LOST BORTHA?! ^O^ ")

class Lion(Animal):

    def move(self):
     print(" I can Roar! >;) ")
     print(" Let it Gooo Let it goo Fly Away from earthh~ ;O ")
    
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()