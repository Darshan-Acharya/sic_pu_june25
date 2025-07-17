import Data_implementation as ebs  


def show_analysis():
    print("Which analysis would you like to see?")
    print("1. Enrollment Trends Over Years (Line Graph)")
    print("2. Enrollment Distribution for a Specific Year (Pie Chart)")
    print("3. Growth/Decline Percentage by Branch (Bar Chart)")
    print("4. Show Enrollment Heatmap")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

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
            df = ebs.df
            ebs.plot_enrollment_heatmap(df)
            show_analysis()
        case '5':
            print("Exiting the program. Goodbye!")
        case _:
            print("Invalid choice. Please enter a number from 1 to 5.")
            show_analysis()#recursive call instead of the infinate while looping for better readability


show_analysis()


