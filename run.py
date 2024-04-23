import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive" 
    ] 


CREDS = Credentials.from_service_account_file ('creds.json')
SCOPED_CREDS = CREDS.with_scopes (SCOPE)
GSPREAD_CLIENT = gspread.authorize (SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open ('stephanie-python-project')


def opening_page():
    """
    Function to display welcome to the user, 
    describe the program & time required to the user and
    ask the user if they are ready to proceed? 
    """
    while True:
        print ("\nWelcome To Your Daily Meal & Ingredients Planner.\n")
        print ("This is a short Python program that will give you a")
        print("list of ingredients to go & buy (or check you already have)") 
        print ("based on your meal choices.\n")
        print ("It will take approx. 5 mins\n")
        print ("Are you ready to do this now? Y = Yes  N = No\n")
        user_decision = input ("Enter: \n")
        user_decision = user_decision.strip() 
        # remove whitespace before &/or after user input
        if user_decision == "Y" or user_decision == "y": 
            # allow uppercase or lowercase Y/y
            print("------------------------------------------------------------") 
            print("\nGreat, Let's Go!\n")
            break
        elif user_decision == "N" or user_decision == "n": 
            # allow uppercase or lowercase N/n
            ("--------------------------------------------------") 
            print("\nOK, See You Later. Bye!")
            print("--------------------------------------------------") 
            break
            return opening_page()
        else:
            print ("\nPlease Try Again")
            print ("\nOnly Enter Y or N")
            print("--------------------------------------------------")
            return opening_page()  


def meal_choices():
    """
    Function to provide user with available meal choices,
    Ask the user to make meal choices
    """
    while True:
        print ("Here are your meal choices\n")
        print ("Please pick the meal you wish to select\n")
        print ("\nFor Meal A : Omlette Enter A\n") 
        print ("\nFor Meal B : Beans on Toast Enter B\n")
        print ("\nFor Meal C : Salmon Dinner Enter C\n")
        print ("\nTo change your mind Enter N (for No)\n")
        user_meal_choice = input ("Enter: \n")
        user_meal_choice = user_meal_choice.strip() 
        # remove whitespace before &/or after user input
        if  user_meal_choice== "A" or user_meal_choice == "a": 
            # allow uppercase or lowercase A/a
            print("--------------------------------------------------") 
            print("\nAn Omlette it is!\n")
            print("\nYou will need:")
            print("\nEggs, Sunflower Oil & Butter")
            print("\nENJOY!")
            break
        if  user_meal_choice== "B" or user_meal_choice == "b": 
            # allow uppercase or lowercase B/b
            print("--------------------------------------------------") 
            print("\nBeans on Toast it is!\n")
            print("\nYou will need:")
            print("\nSliced Pan Bread, Tin of Baked Beans & Butter")
            print("\nENJOY!")
            break
        if  user_meal_choice== "C" or user_meal_choice == "c": 
            # allow uppercase or lowercase C/c
            print("--------------------------------------------------")
            print("\nSalmon it is!\n")
            print("\nYou will need:")
            print("\nSalmon Darne, Potatoes & Tin of Corn")
            print("\nENJOY!")
            break
        elif user_decision == "N" or user_decision == "n": 
            # allow uppercase or lowercase N/n
            print("--------------------------------------------------") 
            print("\nOK, See You Later. Bye!")
            print("--------------------------------------------------")
            break
            return opening_page()
        else:
            print ("\nPlease Try Again")
            print ("\nOnly Enter A, B, C or N")
            print("--------------------------------------------------")
            return meal_choices()


def main():
    """
    Run all program functions
    """
    opening_page()
    meal_choices()

main()