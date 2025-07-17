import random
class FruitQuiz:
      def __init__(self):
            self.fruits={'apple':'red',
                                    'orange':'orange'
                                    'watermelon':' green and red'
                                    'banana':'yellow'}
      def quiz(self):
                  while(True):
                        fruit, color = 
random.choice(list(self.fruits.items))
                        print("WHAT IS THE COLOR OF {}")
                        user_answer = input()
                        if (user_answer.lower() == color):
             print("Correct answer")
         else:
  