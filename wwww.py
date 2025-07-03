class Employee:

    def __init__(self):
        print(' Employee created')

        #2
    def __del__(self):
        print("Destructor called")

def Create_obj():
        print("MAKING OBJ WAIT RAT")
        obj = Employee()
        print( ' FINALLY GURL')
        return obj 
print( ' Calling Create_obj() function....')
print(" Gald that i didnt crash out on that 3 words?")
obj = Create_obj()
print(' Program End...')