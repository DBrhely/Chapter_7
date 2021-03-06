#Challenge 4
#12/15/14
#Danielle Brhely

#Design
#create the trivia game that have knowledge of python
###########################################

import sys
import pickle ,shelve

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    pythonTrivia_file = open_file("pythonTrivia.txt", "r")
    title = next_line(pythonTrivia_file)
    welcome(title)
    score = 0
    highScore = []

    # get first block
    category, question, answers, correct, explanation = next_block(pythonTrivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation = next_block(pythonTrivia_file)
        pointValue = int(score)
        highScore = pointValue
    pythonTrivia_file.close()

    print("That was the last question!")
    print("You're final score is", pointValue)
    print("Your high score is ", highScore)
 
main()  
input("\n\nPress the enter key to exit.")

#Shelve
t = shelve.open("highScore.txt")
t['highScore'] = scores
t.close()
