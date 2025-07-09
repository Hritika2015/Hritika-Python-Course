class Brid:
    def __init__(self):
        print("She was a fairy")

    def whoisThis(self):
        print("Brid")

    def swim(self):
        print("GYATT FASTER DUDE")

class Penguin(Brid):
    def __init__(self):
        super().__init__()
        print("You're as useless as flippy dippy diddy")

    def whoisThis(self):
        print("GYAAAAATTTTTTTTTTTTTTTTT")

    def run(self):
        print("Ew Go faster")

# Create instance and call methods
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
                    
