
class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + " - " + self.meaning

flash = []

print("Welcome to Flashcard Application")

while True:
    word = input("enter the name you want to add to the flashcard: ")
    meaning = input("enter the meaning of the word: ")
    flash.append(Flashcard(word, meaning))
    
    try:
        option = int(input("enter 0 if you want to add another flashcard, otherwise enter 1: "))
        if option == 1:
            break
    except ValueError:
        print("Invalid input. Exiting.")
        break

print("\nYour flashcards:")
for i in flash:
    print(">", i)
