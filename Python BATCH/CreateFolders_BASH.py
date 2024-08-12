import os
import calendar
import sys

def create_folders_and_files(month, year):
    # Get the current directory where the script is located
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Get the number of days in the given month
    num_days = calendar.monthrange(year, month)[1]
    #calendar.monthrange(year, month) Retuns Tuple
    #(weekday of the first day of the month,the number of days in the month)
    #The [1] accesses the second element, which is the number of days in the specified month.
    #So, num_days = no of days in month.

    # Create a folder for each day
    for day in range(1, num_days + 1):
        # Format the date as DD-MM-YYYY
        date_str = f"{day:02d}-{month:02d}-{year}"
        
        # Create the folder
        folder_path = os.path.join(current_directory, date_str)
        os.makedirs(folder_path, exist_ok=True)
        
        # Create the text file with default message
        file_path = os.path.join(folder_path, f"{date_str}.txt")
        with open(file_path, "w") as file:
            file.write("Bhole baba, I thank you for sunshine, Thank you for rain, Thank you for joy, Thank you for pain, It's a beautiful Day. Good Day Boss. ")

# Example usage:
# create_folders_and_files(2, 2023) # For February 2023
# Taking Inputes :
#month = int(input("Enter the month (MM): "))
#year = int(input("Enter the year (YYYY): "))
#create_folders_and_files(month, year)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        month = int(sys.argv[1])
        year = int(sys.argv[2])
        create_folders_and_files(month, year)
    else:
        print("Usage: python your_script.py MM YYYY")