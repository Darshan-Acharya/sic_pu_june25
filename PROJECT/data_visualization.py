import pandas as pd
import matplotlib.pyplot as plt
import engineer_branch_selection as ebs
from Data_acquistion import engg_enrollment_analysist

simulator = engg_enrollment_analysist()  
simulator.generate_data()                
data = simulator.data                   


#reading the previously genearted .csv file 

def show_analysis():
    print("Which analysis would you like to see?")
    print("1. Enrollment Trends Over Years (Line Graph)")
    print("2. Enrollment Distribution for a Specific Year (Pie Chart)")
    print("3. Growth/Decline Percentage by Branch (Bar Chart)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    match choice:
        case '1':
            ebs.plot_enrollment_trends()
            show_analysis()
        case '2':
            year = input("Enter the year for the distribution pie chart (e.g., 2024): ")
            ebs.plot_yearly_distribution(year)
            show_analysis()
        case '3':
            ebs.plot_growth_decline()
            show_analysis()
        case '4':
            print("Exiting the program. Goodbye!")
        case _:
            print("Invalid choice. Please enter a number from 1 to 4.")
            show_analysis()#recursive call instead of the infinate while looping


show_analysis()


