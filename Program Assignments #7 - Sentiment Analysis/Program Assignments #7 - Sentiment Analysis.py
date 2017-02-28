####################################################################################################################################################
##
## CS 101
## Program #7 Sentiment Analysis
##
## Name: CHIA-HUI,AMY,LIN
## Email: clthf@mail.umkc.edu
##
## Creaetion Date: 04/17/2016
## Due Date:       04/24/2016
##
## PROBLEM : Read csv file to get stock prices on specific dates.
##           Output the buy and sell results of the chosen stock with calculated profit/loss.
##
##
## ALGORITHM :
##      1. Create function user_choice to get the choice from the user whether to do the analysis or exit the program.
##      2. Create function get_file_name to prompt the file name to score words and handle invalid file name.
##      3. Create function sort_option to ask user for the sort choice.
##      4. Create function occurence_count_dict to count the occurence of the words.
##      5. Create function ratingsort to collect ratings of the words.
##      6. Create function sum_rating to sum up the ratings.
##      7. Create function cal_avg_score to calculate average scores.
##      8. Create function val_std_dev to calculate standard deviations.
##      9. Create function result_tuple to put together occurences, averages and standard deviations in tuples.
##      10.Create function final_layout to print out the results.
##      11.Call functions in Step 1 to prompt for user choice.
##      12.Call function in Step 2 to get the file name of words to score from the user and handle error if occurs.
##      13.Call function created Step 3 to get the sorting choice from the user.
##      14.Create a dictionary for the word list.
##      15.Put the movie revies into a list.
##      16.Count occurences of words in the word list by calling function in Step 4.
##      17.Collect corresponding ratings of the words by using the function in Step 5.
##      18.Sum up the ratins by calling the function created in Step 6.
##      19.Calculate average scores and standard deviations for each word by using functions in Step 7 and 8.
##      20.Collect the results into the form of tuples using function in Step 9.
##      21.Output results by calling the functions in Step 10.
##
## ERROR HANDLING:
##      Read file name and input choices.
##
##
## OTHER COMMENTS:
##      Something is still wrong with the occurences, I'm missing some words for some reason.
##
####################################################################################################################################################
import os

def user_choice():
    """ Ask the user to do the analysis or quit. """
    error = True
    while error:
        error = False
        print("<<<<<<<< Python Sentiment Analysis >>>>>>>")
        print("------------------------------------------------")
        choice = input("1. Get sentiment for all words in a file. \nQ. Quit \n------------------------------------------------ \n=====>")

        if choice == "1":
            return choice
            break

        elif choice.upper() == "Q":
            print("\n Exiting Program. See you later! ")
            os._exit(0)
            break

        else:
            error = True
            print("\n You must choose one of the valid choices of 1 or Q. Please enter again. \n ")


def get_file_name(choice):
    """Prompt user for name of the file to score words & handle invalid file name."""
    while True:
        try:
            if choice == "1":
                file_name = input(" Enter the name of the file with words to score ==> ")
                file_open = open(file_name, mode = "r")
                return file_open

        except FileNotFoundError:
            print(" Could not find the file specified. Please try another file name.\n")
        except IOError:
            print(" Could not find the file specified. Please try another file name.\n")



def sort_option():
    """ Ask the user for sort option. """
    invalid = True
    while invalid:
        invalid = False
        print("[                 Sort Options                 ]")
        print("------------------------------------------------")
        option = input("1. Sort by Avg Ascending. \n2. Sort by Avg Descending. \n3. Sort by Standard Deviation Ascending. \n4. Sort by Standard Deviation Descending \n------------------------------------------------ \n=====>")

        if option == "1" or option == "2" or option == "3" or option == "4":
            return option

        else:
            invalid = True
            print("\n You must choose one of the valid choices of 1,2,3,4. Please enter again. \n ")


def occurence_count_dict(word_list, match_list):
    """Count the occurences of words in the word list."""
    i = 0
    occurence_count = {}
    while i < len(match_list):

        for word in word_list:
            if word in match_list[i]:
                try:
                    occurence_count[word] = occurence_count[word]+ match_list[i].count(word)
                except KeyError:
                    occurence_count[word] = 1
        i += 1


    return (occurence_count)

def ratingsort(word_list,match_list):
    """Put all ratings in a list sorted by words."""
    match_list_break = []
    k = 0
    while k < len(match_list):
        match_list_break.append(match_list[k].split())
        k+=1

    ratingsort = {}
    i = 0

    while i < len(match_list):
        for word_key, val_key in word_list.items():
            if word_key in match_list[i]:
                if match_list[i].count(word) > 1:
                    count = match_list[i].count(word)
                    ratingsort.setdefault(word_key, []).append(int(match_list_break[i][0]*count))
                else:
                    ratingsort.setdefault(word_key, []).append(int(match_list_break[i][0]))
        i += 1

    return(ratingsort)


def sum_rating(ratingsort):
    """Calculate the sum rating for each word."""
    sumrating = {}
    n = 0

    for ratingkey, ratingval in ratingsort.items():
        sumrating[ratingkey] = sum(ratingval)

    return sumrating

def cal_avg_score(sumrating,occurence):
    """Calculate average score for words."""
    avg_score_dict = {}
    for ratingkey in sumrating.keys():
        for occkey in occurence.keys():
            if ratingkey == occkey:
                avg_score_dict[ratingkey] = sumrating[ratingkey]/occurence[occkey]

    return avg_score_dict



def cal_std_dev(ratingsort, avg_score_dict, occurence):
    """Calculate standard deviation for words."""
    std_dict = {}
    for ratingkey, ratingval in ratingsort.items():
        r = 0
        std_sum = 0
        for avg_key in avg_score_dict.keys():
            for occkey in occurence.keys():
                if ratingkey == avg_key and ratingkey == occkey:
                    while r < len(ratingval):
                        std_sum += ((avg_score_dict[avg_key] - ratingval[r])**2)/occurence[occkey]
                        r += 1
                    std_dict[avg_key] = std_sum


    return std_dict

def result_tuple(occurence, avg_score_dict, std_dict):
    """Fetch occurence, avg score & std for corresponding words into tuples."""
    result_tuple = []
    result_list = []
    for occkey in occurence.keys():
        result_list.append([occkey,occurence[occkey],avg_score_dict[occkey], std_dict[occkey]])

    num = 0
    while num < len(result_list):
        result_tuple.append(tuple(result_list[num]))
        num += 1

    return result_tuple


def final_layout(option, result_tuple):
    """Sort by User Options & Format the final results."""
    if option == "1":
        result_tuple.sort(key=lambda item:item[2])
    if option == "2":
        result_tuple.sort(key=lambda item:item[2], reverse = True)
    if option == "3":
        result_tuple.sort(key=lambda item:item[3])
    if option == "4":
        result_tuple.sort(key=lambda item:item[3], reverse = True)

    print("{:<15s}{:>15s}{:>15s}{:>20s}".format("Word", "# of Occurrence", "Avg Score", "Std Deviation"))
    print("==================================================================")

    re = 0
    while re < len(result_tuple):
        print("{:<15s}{:>15.0f}{:>15.4f}{:>20.4f}".format(result_tuple[re][0], result_tuple[re][1], result_tuple[re][2], result_tuple[re][3]))
        re += 1

    print("__________________________________________________________________\n")

#------------------------------------------------------------ Main Code -----------------------------------------------------------#

#User's choice of analysis or exit the program
choice = user_choice()

#User's file name for words to score
file_open = get_file_name(choice)

#User sort option
option = sort_option()

main_file = open("movieReviews.txt", mode = "r")

#Create a dictionary for word list
word_list = {}
k = []

for word in file_open:
    word = word.strip().strip(".")
    word_list[word] = k

file_open.close()


#Put the lines in the main_file to a list
main_file.readline()
match_list = []

for match in main_file:
    match = match.strip()
    match_list.append(match)

main_file.close()


#Count occurences of words in the word list
occurence = occurence_count_dict(word_list, match_list)

#Collect corresponding rating of the words
ratingsort = ratingsort(word_list, match_list)

#Sum up the ratings for each word
sumrating = sum_rating(ratingsort)

#Calculate average score & standard deviation
avg_score_dict = cal_avg_score(sumrating,occurence)
std_dict = cal_std_dev(ratingsort, avg_score_dict, occurence)

#Put the results into the form of tuples
result_tuple = result_tuple(occurence, avg_score_dict, std_dict)

#Output Result
final_output = final_layout(option, result_tuple)
