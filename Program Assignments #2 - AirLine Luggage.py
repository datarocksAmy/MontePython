####################################################################################################################################################
##
## CS 101
## Program #2 AirLine Luggage
##
## Name: CHIA-HUI,AMY,LIN 
## Email: clthf@mail.umkc.edu
##
## Creaetion Date: 02/06/2016
## Due Date:       02/14/2016
##
## PROBLEM : Calculate the hops and percentage of on time for the luggage to Honolulu for the trial run the user wants.
##           Iterate the trials based on the percentage of each destination until the luggage reaches Honolulu.
##           
##
## ALGORITHM : 
##      1. Build functions for MCI, LVS, SEA, HNL based on each probability for the next destination.
##      2. Ask for number of trial run from the user and whether to show the detail result or not.
##      3. Continue the program if the number is greater than 0.
##      4. Assign probability range and start the string from MCI to the next one to get the result of each trial.
##      5. Count the occurance of hops in each trial and see how many times is on time. If the user wants the output for each trial, output the result, or else pass.
##      6. Calculate the on_time percentage.
##      7. Print on_time output, percentage and maximum hop.
##      7. Ask the user if he/she wants to run the program agian, if not, end the program.
##
## ERROR HANDLING:
##      When user enters a character, the program should ask for another prompt.
##
## OTHER COMMENTS:
##      Nope! Tons of loops going on!
##
####################################################################################################################################################

import random
    
#Luggage gets to MCI    
def MCI(result): 
    result += " MCI --> " 
    prob_MCI = random.randint(1,10)

    if 1<= prob_MCI <= 4:
        result = LVS(result)
    elif 5<= prob_MCI <=7:
        result = SEA(result)
    else:
        result = HNL(result)

    return result  

#Luggage gets to LVS  
def LVS(result):
    prob_LVS = random.randint(1,10)
    result += " LVS --> "

    if 1<= prob_LVS <= 3:
        result = MCI(result)      
    elif 4<= prob_LVS <=8:
       result =  SEA(result)
    else:
        result = HNL(result)
        
    return result
    
#Luggage gets to SEA
def SEA(result):
    result += " SEA --> "
    prob_SEA = random.randint(1,10)
    
    if prob_SEA == 1:
        result = MCI(result)
    elif 2<= prob_SEA <=7:
        result = LVS(result)
    else:
        result = HNL(result)

    return result
            
#Luggage gets to HNL
def HNL(result):
    return result + " HNL"



#-----------------------------------Main Program Starts Here-----------------------------------#
run = True
while run:
#Input: Number of trials & Output Details or not
    
    #Test if user_prompt is a number or not. 
    error = True
    while error:
        error = False
        user_prompt = input("\n How many trials do you want to run lost luggages?  ")
        
        if user_prompt.isdigit():
            user_prompt = int(user_prompt)
            pass
        
        else:
            error = True
            print("\n Invalid imput. You must enter a number. ")
            
    result_show = input("\n Do you want to output details [Y/YES/N/NO] ?  ").upper()
    on_time = 0
    total_hop_list = []
    
    
    while user_prompt <= 0:
        print(" Invalid imput. You must enter a number > 0 ")
        print()
        user_prompt = int(input("\n How many trials do you want to run lost luggages?  "))
   
    else:
        trial = 1
        while trial <= user_prompt:
    # Assign probability range
            prob = random.randint(1,10)
    # Original string
            result = "MCI -->"


            if (1<= prob <=4):
                result = LVS(result)
            elif (5<= prob <=7):
                result = SEA(result)
            else:
                result = HNL(result)
                
    #Trial Count    
            trial_result = ("\n Trial " + str(trial)+ ":  " + result)

        
    #Hops Count
            hops_count = "-->"
            trial_hops = trial_result.count(hops_count)
            total_hop_list.append(trial_hops)

            hop_list = str(trial_hops)
            trial+=1
            
            if hop_list in ["1","2"]:
                on_time += 1
                
     #Print out each trial if the user enters yes.               
            if result_show == ("Y" or "YES"):
                print(trial_result)
            else:
                pass
                            
    #On_time percentage           
    on_time_percentage = (on_time/(trial-1))*100.0
    on_time_text = "\n The luggage was on time {:.2f}% of the time. ".format(on_time_percentage)
    on_time_text.format(on_time_percentage)
        
    #Print Output & Max Hops
    print(on_time_text, "(", on_time , "/", trial-1, ")")
    print (" The max hops that occured was", max(total_hop_list),".")

    #User prompt for the second time & Output details if needed    
    run = False

    while True:
        second_user_prompt = input("\n Do you want to run again [Y/YES/N/NO]?  ").upper()

        
        if second_user_prompt == ("Y" or "YES"):
            run = True
            break
        
        elif second_user_prompt == ("N" or "NO"):
            break
            
        else:
            print("\n You entered an invalid answer. Please enter [Y/YES/N/NO].")
            
        result_show = input("Do you want to output details [Y/YES/N/NO] ?")
         
