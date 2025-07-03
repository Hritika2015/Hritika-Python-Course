class Iostring ():

    def __init__(self):
        self.str1 = ""
        #2
    def get_String(self):
        self.str1 = input("ENTER STRING : ")
        #3
    def print_String(self):
        print("Result is :", self.str1.upper())

str1 = Iostring()

str1.get_String()
str1.print_String()