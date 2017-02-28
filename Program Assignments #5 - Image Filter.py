####################################################################################################################################################
##
## CS 101
## Program #5 Image Filter
##
## Name: CHIA-HUI,AMY,LIN
## Email: clthf@mail.umkc.edu
##
## Creaetion Date: 03/18/2016
## Due Date:       03/27/2016
##
## PROBLEM : Read file and convert the image file to Gray scale or Vintage.
##           Output to the filtered file.
##
##
## ALGORITHM :
##      1. Create function filter_choice to as the user for filter option.
##      2. Create function grayscale to filter the image to gray scale by changing the red, blue and green pixel.
##      3. Create function vintage to filter the image to vintage by changing the blue pixel.
##      4. Create function read_file to get the file name from the user and open it in read mode, prompt the user if any error occurs.
##      5. Create function bad_header to check if the header or pixel is valid or not.
##      6. Create function save_result_file to prompt the user for file name and open it to write the results into.
##      7. Open & prompt the read file by calling the function in Step 1.
##      8. Check if the header or pixels are valid or not by callind the function in Step 5.
##      9. Prompt user for output file name, rerun for output if any error occurs.
##      10.Filter the image based on user's choice in Step 7 and write the result in the output file.
##      11.Close both files & End program.
##      
##
## ERROR HANDLING:
##      File name prompts and reading the ppm file line by line.
##
##
## OTHER COMMENTS:
##      Finally get the suite to run right at the last minute!
##
####################################################################################################################################################

def filter_choice():
    """ Ask the user for filter Option. """
    error = True
    while error:
        error = False
        prompt = input("Please Choose an Image Filter: \n 1. Convert Image to GrayScale \n 2. Convert Image to Vintage \n Q. Quit\n =====>")
        if prompt == "1" or prompt == "2" or prompt == "Q" or prompt == "q":
            return prompt
        else:
            error = True
            print("\n Invalid Input. You must enter 1, 2 or Q \n ")

def grayscale(testlines):
    """ Convert the image to Grayscale """
    i=3
    red_scale=3
    green_scale=4
    blue_scale=5
    test = []
    sum_test = []
    result = []
    k = 0
    sum_test_iterate = 0

    while i < len(testlines):
        if i == red_scale:
            testlines[i]=float(testlines[i])*0.299
            red_scale += 3

        if i == green_scale:
            testlines[i]=float(testlines[i])*0.587
            green_scale += 3

        if i == blue_scale:
            testlines[i]=float(testlines[i])*0.114
            blue_scale += 3
        test += [(testlines[i])]

        i += 1

    while k+3 < len(testlines):
        sum_test += [int(sum(test[k:k+3]))]
        k += 3

    while sum_test_iterate < len(sum_test):
        result += ([str(sum_test[sum_test_iterate])]*3)
        sum_test_iterate += 1
    grayscale_result =("".join(testlines[0:3]))+("\n".join(result))


    return print(grayscale_result,file=output_file)


def vintage(testlines):
     """ Convert the image to Vintage """
     i=3
     blue_scale=5
     result = []
     while i < len(testlines):
        if i == blue_scale:
            testlines[i]=str(int(int(testlines[i])*0.5))+"\n"
            blue_scale+=3
        result += [testlines[i]]
        i += 1
     vintage_scale = ("".join(testlines[0:3]))+("".join(result))
     return print(vintage_scale,file=output_file)



def read_file(prompt):
    """ Enter filter Option to ask for file name prompt and handle file error """
    import os
    while True:
        try:
            if prompt == "1" or prompt == "2":
                read_file_name = input(" Enter a valid filename to convert ==> ")
                return open(read_file_name, mode = "r")

            if prompt == "q" or prompt == "Q":
                print(" Exiting Program. See you later! ")
                os._exit(0)
                break


        except FileNotFoundError:
            print(" Could not find the file specified. Try another file name.\n")
        except IOError:
            print(" Could not find the file specified. Try another file name.\n")



def bad_header(testlines):
    """ Check if the header or the pixel is valid or not."""

    i=3
    while i < len(testlines):
        if testlines[0].strip() != "P3":
            print(" The files first line should be P3. ")
            errorfile = True
            return errorfile
            break

        if testlines[2].strip() != "255":
            print(" The color depth must be 255. ")
            errorfile = True
            return errorfile
            break


        if "0"< testlines[i].strip() < "255" == True:
            print(" There's error pixel in the file. ")
            errorfile = True
            return errorfile
            break
        i += 1

def save_results_file():
    """ Prompt for file name for saving results from the user. """
    while True:
        try:
            save_file_name = input(" Enter the name of the file you want to save to? ==> ")
            return open(save_file_name,"w")

        except FileNotFoundError:
            print(" Invalid Input. Try another file name.")
        except IOError:
            print(" Invalid Input. Try another file name.")


#-------------------------------------------- MAIN CODE --------------------------------------------#

#Ask User for Filter Choice
prompt = filter_choice()

#Check the header and pixels of the file
check = True
while check:
    check = False
    open_file = read_file(prompt)
    testlines = open_file.readlines()


    check_file = bad_header(testlines)
    if check_file == True:
        check = True

    else:
#Filter the file & save in a new file
        check = False
        output_file = save_results_file()
        if prompt == "1":
            result = grayscale(testlines)

        if prompt == "2":
            result = vintage(testlines)

        open_file.close()
        output_file.close()

        print(" Your file has been filtered and saved ")
