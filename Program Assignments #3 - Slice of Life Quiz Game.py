####################################################################################################################################################
##
## CS 101
## Program #3 Slice of Life Quiz Game
##
## Name: CHIA-HUI,AMY,LIN 
## Email: clthf@mail.umkc.edu
##
## Creaetion Date: 02/20/2016
## Due Date:       02/28/2016
##
## PROBLEM : Ask user how many rounds and the level of difficulty to play. Provide index hint if user wishes.
##           Generate random questions and slice range for user to guess and then keep track of the correctness of user's responses.
##           Return the percentage of correct answers out of total rounds.
##           
##
## ALGORITHM : 
##      1. Build a function to evaluate empty string return in level hard.
##      2. Ask for number of rounds to play from the user.
##      3. if user_prompt is not within 1 and 20. Return to step 2. and ask again.
##      4. Ask for the level of difficulty to play from the user
##      5. Return to step 4. if the user doesn't enter a number between 1-3.
##      6. Generate random start, end and assign interval from the choise made in step 5.
##      7. Generate a random series of alphabets based on the length of the choice in step 5.
##      8. Swap the orders of start and end by calling the function built in step 1.
##      9. Change the 0 for either start and end slicing number to None to avoid getting an empty string.
##      10.Output index hints if user requests. Else, output quetsions and slicing parts and ask for user's answers.
##      11.Keep track of the correct responses.
##      12.Calculuate the correct percentage of the user reponses and print out the result.
##      13.Ask the user if he/she wants to play again or not. If yes, return to step 2. If not, end the program.
##
## ERROR HANDLING:
##      None.
##
## OTHER COMMENTS:
##      Nope! More loops and more error handling requires in this program.  Stuck on the slicing parts for a really long time.
##
####################################################################################################################################################

import string
import random
import math

# Fucntion for Checking an Empty String for Level Hard
def check_valid_string(level_of_difficulty,word_length,question):
    random_start = random.randint(0, int(word_length/2))
    random_end = random.randint(int(word_length/2)+1, word_length)
    interval = 1

    if level_of_difficulty == 3:
           # [START NEGATIVE SLICE]
        if random.randint(1, 4) == 1:
            random_start *= -1

        # [END NEGATIVE SLICE]
        if random.randint(1, 4) == 1:
            random_end *= -1

        # [REVERSE SLICE]
        if random.randint(1, 4) == 1:
            interval = -1

        # [INTERVAL 2 OR -2]
        if random.randint(1, 5) == 1:
            interval_choice = [2, -2]
            interval = random.choice(interval_choice)

    if question[random_start:random_end:interval] == "":
            random_start, random_end = random_end, random_start

    return random_start, random_end, interval

#---------------------------------------------------------- Main Code ----------------------------------------------------------#
# Input Number of Rounds to Play From User
run = True
while run:
    error = True
    while error:
        error = False
        user_prompt = input("\n Welcome to the Game of Slice! \n How many rounds do you want to play? [ Please Enter a number 1-20]")
        if user_prompt.isdigit():
            user_prompt = int(user_prompt)
            pass

        else:
            error = True
            print("\n Invalid input. You must enter a number. ")

    while not(1 <= user_prompt <= 20):
            print("\n Invalid Input. \n You must enter a number between 1 and 20.")
            user_prompt = int(input("\n How many rounds do you want to play? [ Please Enter a number 1-20]"))
    else:
# Input Level Of Difficulty From User
            level_of_difficulty = int(input("\n How easy of a string? [ Enter 1.Easy  2.Medium  3.Hard ]"))

            if not(1 <= level_of_difficulty <=3):
                error_level = True
                print("\n Invalid input. \n You must enter 1, 2 or 3.")


# Generate Random Start, End and Interval Numbers
    run_round = 1
    guess_correct = 0

    while run_round <= user_prompt:

        # EASY Level
        if level_of_difficulty == 1:
                word_length = 5
                random_start = random.randrange(0,int(word_length/2))
                random_end = random.randrange(math.ceil(word_length/2)+1,word_length+1)
                interval = 1


        #MEDIUM Level
        elif level_of_difficulty == 2:
                word_length = 7
                random_start = random.randrange(0,int(word_length/2))
                random_end = random.randrange(math.ceil(word_length/2)+1,word_length+1)
                interval = 1

        # Hard Level
        else:
            word_length = 10
            random_start = random.randrange(0,int(word_length/2))
            random_end = random.randrange(math.ceil(word_length/2)+1,word_length+1)
            interval = 1

            # [START NEGATIVE SLICE]
            if random.randint(1, 4) == 1:
                random_start *= -1

            # [END NEGATIVE SLICE]
            if random.randint(1, 4) == 1:
                random_end *= -1

            # [REVERSE SLICE]
            if random.randint(1, 4) == 1:
                interval = -1

            # [INTERVAL 2 OR -2]
            if random.randint(1, 5) ==1:
                interval_choice = [2, -2]
                interval = random.choice(interval_choice)


#Generate Random Series of Alphabets
        i = 0
        question = ""
        upper_lower_alphabet = string.ascii_uppercase + string.ascii_lowercase
        while i < word_length:
            question += random.choice(upper_lower_alphabet)
            i += 1

#Swap Orders for Empty STring
        (random_start, random_end, interval) = check_valid_string(level_of_difficulty, word_length, question)

#Change 0 to None for Start or End Value
        if random_start == 0:
            random_start == None
        if random_end ==0:
            random_end == None


#Print Out Index Hint if User Wants
        index_run = True
        while index_run:
            index_hint_prompt = input("\n Do you want to hint indexes [Y/YES/N/NO] ?  ").upper()

            if index_hint_prompt == ("Y" or "YES"):
                index_run = False
                positiveindex = " "
                negativeindex = ""

                for i in range(0,word_length):
                    positiveindex += str(i)

                for t in range(0,word_length):
                     negativeindex += str(t)

                print("\t",positiveindex)
                print("\t -0" + negativeindex[word_length:0:-1])

            elif index_hint_prompt != ("N" or "NO" or "Y" or "YES"):
                print("\n You enterted an invalid value. Please enter [ Y/YES/N/NO ].")
                index_run = True
            else:
                break

#Question for the Game/ Game Starts!
        question_combine = print("\t ",question,"[", random_start, ":", random_end, ":", interval, "]")
        user_answer_question = input(" What is your guess? -----> ")
        correct_answer = (question[random_start:random_end:interval])

#Answer Correct Count
        if correct_answer == user_answer_question:
                print("\t CORRECT! :) The word was ", correct_answer)
                print()
                guess_correct += 1

        else:
                print("\t WRONG :( ...  The word was", correct_answer)
                print()
                pass

        run_round += 1

#User Accuracy on Guessing
    guess_correct_percentage = (guess_correct/user_prompt)*100.0
    print("\n You got ", guess_correct, " out of ", user_prompt," which is {:.2f}%".format(guess_correct_percentage))

#Prompt User to Play again or Not
    run = False
    while True:
        second_user_prompt = input("\n Do you want to play again [ Y/Yes/N/No ]? ").upper()
        if second_user_prompt == ("Y" or "YES"):
            run = True
            break

        elif second_user_prompt == ("N" or "NO"):
            print("\n <<<------------- Thank you for playing the game!------------->>>")
            break

        else:
            print("\n You enterted an invalid value. Please enter [ Y/YES/N/NO ].")