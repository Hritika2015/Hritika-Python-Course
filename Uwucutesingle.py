class India():
    def capital(self):
        print(" P :P :P :P :P :P :P :P :P :P YAYY!!")
    def language(self):
        print(" OOOOOOOoooooOOOOOOO")
    def type(self):
        print(" SLAY. ")    #2
class USA():
    def capital(self):
        print(" :P :P :P :P :P :P :P :P :P :P YAYY!!")
    def language(self):
        print(" OOOOOOOoooooOOOOOOO")
    def type(self):
        print(" SLAY. ")    
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
