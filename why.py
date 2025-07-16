from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    def task(self):
        print(" WE ARE IN A AREA WHERE PPL SUFFER a.k.a class")
class test_class(Absclass):
    def task(self):
        print("We are inside the scary area a.k.a science class")
test_obj = test_class()
test_obj.task()
test_obj.print(100)