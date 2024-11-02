class flashcard:
    def __init__(self, word, meaning):
        self.word = word 
        self.meaning = meaning
    def __str__(self):

        #We will return a string.
        return self.word+' ( '+self.meaning+' )'

flash = []
print("Welcome to the flashcard application.")

#The following loop will be reoeated until the user stops to add the flashcards.

while(True):
    word = input("Enter the word you want to add to the flashcard: ")
    meaning = input("Enter the meaning of the word you entered: ")

    flash.append(flashcard(word,meaning))
    option = int(input("Enter 0, if you want to add another flashcard. Otherwise enter 1.-----"))

    if (option):
        break

#Printing all the flashcards.
print("\n Your flashcards!")
for i in flash:
    print(">", i)
