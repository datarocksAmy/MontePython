########################################################################
##
## CS 101
## Program #1 Drone Flight Time
##
## Name: CHIA-HUI,AMY,LIN 
## Email: clthf@mail.umkc.edu
##
## Creaetion Date: 01/28/2016
## Due Date:       01/31/2016
##
## PROBLEM : Calculate the total power supply by batteries for motors and the flight time of a drone.
##           Convert the flight time from hours to minutes & minutes/seconds.
##
## ALGORITHM : 
##      1. Get input batteries(mAh), number of motors on the drone and how mnay Amps drawn per motor from the user.
##      2. Convert batteries mAh into Amp Hours(Amps)by dividing mAh to 1000.
##      3. Calculuate total Amps for the drone by multiplying number of motors and Amps per motor.
##      4. Calculate flight time of the drone by dividing batteries Amps to total drone motors Amps.
##      5. Convert flight time from hours to minutes by multiplying 60.
##      6. Use built-in function divmod to get flight time seperately(interger/decimals). Multiply the decimals by 60 to convert time from minutes to seconds.
##      7. Print the results. (Total Amps used -> flight time in minutes --> flight time in minutes and seconds)
##
## ERROR HANDLING:
##      None.
##
## OTHER COMMENTS:
##      If enter the number of motors on the drone and the Amps drawn for PER motor are both 0, we'll get a Zero Division Error.
##      Since the drone needs at least one motor to fly, the case will unlikely to happen.
##
########################################################################


#Input Variables : batteries mAh, number of motors, Amps per motor
batteries_mAh = int(input("\n Enter the batteries rated by mAh (milliamp/hours): "))
number_motor = int(input(" Enter the numbers of motors on the drone: "))
Amps_per_motor = int(input(" Enter the Amps drawn for PER motor: "))


#Calculations :

#Convert Amp to mAh
batteries_Amps = batteries_mAh / 1000
#Total Amps for drone
drone_total_Amps = number_motor * Amps_per_motor

#Convert flight time from hour to minutes
time_drone_fly_hr = batteries_Amps / drone_total_Amps
time_drone_fly_min = time_drone_fly_hr * 60

#Get flight time in minutes and seconds seperately
(i, d) = divmod(time_drone_fly_min,1)
drone_time_min = int(i)
drone_time_sec = int(d*60)


#Output: Print Results
print("\n {RESULTS} \n", " -Total use of Amps of your drone:",drone_total_Amps, "Amps. \n",
      " -The drone flight time:",time_drone_fly_min, "minutes.\n  -Which is:", drone_time_min,"minutes and",drone_time_sec, "seconds.")
