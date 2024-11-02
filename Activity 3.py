import random

class FruitQuiz:
    def __init__(self):

    #Create a dictionary of fruits as keys and colour as value.
        self.fruits = {'Apple' : 'red',
                       'Orange' : 'orange',
                        'Banana' : 'yellow',
                         'Watermelon' : 'green'}
        
    #Function for the quiz, where a fruit will be chosen randomly.
    def quiz(self):
        while (True):
            fruit, colour = random.choice(list(self.fruits.items()))

            print("What is the colour of {}".format(fruit))
            user_answer = input()
            
            if (user_answer.lower() == colour):
                print("Correct answer")
            else:
                print("Wrong Answer")
            
            option = int(input("Enter 0, if you wish to continue playing. Otherwise enter 1------"))
            if (option):
                break

print("Welcome to the fruit quiz!")
fq = FruitQuiz()
fq.quiz()
