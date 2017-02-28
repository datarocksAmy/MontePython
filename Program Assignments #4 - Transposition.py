####################################################################################################################################################
##
## CS 101
## Program #4 Transposition
##
## Name: CHIA-HUI,AMY,LIN
## Email: clthf@mail.umkc.edu
##
## Creaetion Date: 03/04/2016
## Due Date:       03/14/2016
##
## PROBLEM : Read file and decode/uncode the file that the user wish for.
##           Output to the result to a new file.
##
##
## ALGORITHM :
##      1. Create function option_choice to as the user for transposition option.
##      2. Create function transpose to encode the string and return the transposed value.
##      3. Create function untranspose to take a transpose result back to the original value.
##      4. Create function prompt_read_file_name to get the file name from the user and open it in read mode.
##      5. Create function write_result_file to prompt the user for file name and open it to write the results into.
##      6. Ask the user for prompt by calling the function created in Step 1.
##      7. Open & prompt the read file by calling the function in Step 4.
##      8. Open & prompt the write file by calling the function in Step 5.
##      9. Iterate lines in the file.
##      10.Decode or uncode the lines based on the prompt from Step 6 and print the results in the file created in Step 5.
##      
##
## ERROR HANDLING:
##      Use try/except method to make sure the user input a valid value.
##
##
## OTHER COMMENTS:
##      Functions make the main code nice and clean!
##
####################################################################################################################################################
def option_choice():
    """ Ask the user for Tranposition Option. """
    error = True
    while error:
        error = False
        prompt = input("Please Choose a Transposition Option: \n 1. Encipher File \n 2. Decipher File \n Q. Quit\n =====>")
        if prompt == "1" or prompt == "2" or prompt == "Q" or prompt == "q":
            return prompt
        else:
            error = True
            print("\n Invalid Input. You must enter 1, 2 or Q \n ")

def transpose(line):
    """ Encodes the String & Return the Transposed Value """
    transpose_outcome = line[::2] + line[1::2]
    return transpose_outcome

def untranspose(line):
     """ Take a transpose message & return it back to the original """
     import math
     untranspose_outcome = ""
     iterate = 0
     j = 0
     i = math.ceil(len(line)/2)
     while iterate <= len(line):
        if j in range(0,i):
            if i in range(i,len(line)):
                untranspose_outcome += line[j]+line[i]
                i+=1
                j+=1

        iterate +=1
     if len(line)%2 != 0:
         untranspose_outcome += line[j]


     return untranspose_outcome


def prompt_read_file_name(prompt):
    """ Enter Transposition Option to ask for file name prompt and handle file error and return the open file in read mode."""
    import os
    while True:
        try:
            if prompt == "1":
                read_file_name = input(" Enter the name of the file to ENCIPHER ==> ")
                return open(read_file_name, mode = "r")

            if prompt == "2":
                read_file_name = input(" Enter the name of the file to DECODE ==> ")
                return open(read_file_name, mode = "r")

            if prompt == "q" or prompt == "Q":
                print(" Exiting Program. Hope you got the code you want! ")
                os._exit(0)
                break


        except FileNotFoundError:
            print(" Could not find the file specified. Try another file name.\n")
        except IOError:
            print(" Could not find the file specified. Try another file name.\n")


def write_results_file():
    """ Prompt for output file name from the user & return the open file in write mode. """
    while True:
        try:
            output_file_name = input(" Enter the name of the file to WRITE to ==> ")
            return open(output_file_name,"w")

        except FileNotFoundError:
            print(" Invalid Input. Try another file name.")
        except IOError:
            print(" Invalid Input. Try another file name.")


#-------------------------------------------- MAIN CODE --------------------------------------------#

#Ask User for Transposition Option
prompt = option_choice()

#Open the file and write the results to another file
open_file = prompt_read_file_name(prompt)
output_file = write_results_file()

for line in open_file:
    result = ""
    line = line.strip()
    if prompt == "1":
        result += transpose(line)
    
    
    if prompt == "2":
        result += untranspose(line)
        
    print(result,file=output_file)
        


open_file.close()
output_file.close()
