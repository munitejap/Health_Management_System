"""PROJECT NAME: HEALTH MANAGEMENT SYSTEM
CODE WRITTEN BY : MUNITEJA P"""
import datetime # datetime  module for Getting the current time

def fmsfun(): # The Ultimate Function for Food Management System
    print("Please Enter (1/2/3/4) for Meal Options from :\n 1.BREAKFAST \n 2.LUNCH \n 3.SNACKS\n 4.DINNER ")
        # Getting the data about type of Meal
    meal = int(input())
    print("Enter enter the Items you have ate: ")
    mealitems = input()# Getting the Data about what they ate
    logdate1 = datetime.datetime.now() # Getting the time of logging this data
    try:
            f = open("FMS_Log_File", "a")# Open a log txt file in append mode to add the data without erasing previous data
            f.write(f"Logdate: {logdate1}    >  \t Mealtype : {meal}   >  \t Mealitems :{mealitems} \n")# Write data to file
            print("Data has been Logged Successfully => Be Healthy")

    except:
            print(f"Sorry the Output couldnt been Generated because of {Exception}")
    return 0

def mmsfun():#The Ultimate function for Medicine Management System
        print("Please Enter (1/2/3) for Medicine Options from :\n 1.Tablets \n 2.Syrups \n 3.Injectins")
        # Getting the data about type of Medicine
        medicine = int(input())
        print("Enter the Medicines you have taken: ")
        medicineitems = input()# Getting the Data about what they ate
        logdate2 = datetime.datetime.now() # Getting the time of logging this data
        try:
            f = open("MMS_Log_File", "a")# Open a log txt file in append mode to add the data without erasing previous data
            f.write(f"Logdate: {logdate2}    >  \t Medicinetype : {medicine}   >  \t Medicines Taken :{medicineitems} \n")# Write data to file
            print("Data has been Logged Successfully => Be Healthy")
        except:
            print(f"Sorry the Output couldnt been Generated because of {Exception}")
            return 0

def main():
    print("Please Press 1 to START or 0 to EXIT the Health_Management_System:")
    userinput =int(input()) # Getting Input from User to start or exit
    if userinput == 1:
         print("Getting Started with Health_Management_System....WELCOME \n ")
         print("Please Press 1 to get Food_Management_System or Press 2 to get Medicine_Management_System: ")
         userinput2 = int(input())
         if userinput2 == 1:
                fmsfun()
         elif userinput2 == 2:
                mmsfun()
         else:
                print("Please Check the input")
    elif userinput == 0:\
            print("Thank You,You have chosen to EXIT=> BE HEALTHY ")
    else:
        print("The Input entered is Invalid,Try Again \n")
        main()

main()
