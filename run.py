import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('stephanie-python-project')

#sales = SHEET.worksheet('sales')
#data = sales.get_all_values()
#print(data)


# example function
def get_sales_data():
    """
    Get sales figures from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is: {data_str}")

def opening_page():
    """
    Function to display welcome to the user, 
    describe the program & time required to the user and
    ask the user if they are ready to proceed? 
    or exit if they do not wish to proceed
    """
    while True:
        print ("\nWelcome To Your Daily Meal & Ingredients Planner.\n")
        print ("This is a short Python program that will show you a shopping")
        print("list of ingredients based on your meal choices for tomorrow.\n")
        print ("It will take approx. 5 mins\n")
        print ("Are you ready to do this now? Y = Yes  N = No\n")
        user_decision = input ("Enter: \n")
        user_decision = user_decision.strip() # remove whitespace before &/or after user input
        if user_decision == "Y" or user_decision == "y": # allow uppercase or lowercase Y/y
            print("------------------------------") # 30 * - character
            print("\nGreat, Let's Go!\n")
            break
        elif user_decision == "N" or user_decision == "n": # allow uppercase or lowercase N/n
            ("------------------------------") # 30 * - character
            print("\nOK, See You Later. Bye!")
            break
        else:
            print ("\nPlease Try Again")
            print ("\nOnly Enter Y or N")
            print("------------------------------") # 30 * - character
            return opening_page()         


def main():
    """
    Run all program functions
    """
    opening_page()


main()








# note to self on code used: always check if input method used to ensure \n used where input will be entered before"


# Testing opening_page() function
# Capital Y 
# Lowercase y 
# Capital N 
# Lowercase n  
# White Space before &/or after 
# Invalid input 