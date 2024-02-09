# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:46:56 2023

@author: Harsh
"""

with open("sample2.txt", "r") as input_file:
    with open("temp2.txt", "w") as output_file:
        # Iterate all lines from the file
        for line in input_file:
            # If the substring is not in a line, write it to the temporary file
            if "jhingaalalala" not in line.strip("\n"):
                output_file.write(line)

# Replace the original file with the temporary file
import os
os.replace("temp2.txt", "sample2.txt")

booking_id = input("Enter your Reservation ID: ")
with open("sample1.txt", "r") as input_file:
    with open("temp1.txt", "w") as output_file:
        # Iterate all lines from the file
        for line in input_file:
            # If the line contains the booking_id, ask the user what they want to modify
            if booking_id in line:
                print("Reservation details:")
                print(line)
                
                modification = input("What do you want to modify? (e.g., date, time, number of people): ")
                # add more conditions based on what aspects the user wants to modify
                if modification.lower() == "date":
                    new_date = input("Enter the new date (in YYYY-MM-DD format): ")
                    line = line.replace(f'"date": "{line.split(",")[2].split(":")[1].strip()}"', f'"date": "{new_date}"')
                elif modification.lower() == "time":
                    new_time = input("Enter the new time (in HH:MM format): ")
                    line = line.replace(f'"time": "{line.split(",")[3].split(":")[1].strip()}"', f'"time": "{new_time}"')
                elif modification.lower() == "number of people":
                    new_num_people = input("Enter the new number of people: ")
                    line = line.replace(f'"number of people": "{line.split(",")[4].split(":")[1].strip()}"', f'"number of people": "{new_num_people}"')
                else:
                    print("invalid input")

            # Write the modified or unmodified line to the temporary file
            output_file.write(line)
input_file.close()

os.replace('temp1.txt', 'sample1.txt')
