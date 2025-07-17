from Data_acquistion import branches, df

import matplotlib.pyplot as plt

# Plotting the enrollment trends over the years
plt.figure(figsize=(12, 6)) # Set the figure size for better readability

# Iterate through each branch to plot its enrollment trend
for branch in branches["name"]:
    # Filter the DataFrame to get data for the current branch
    branch_data = df[df["Branch"] == branch]
    # Plot Year vs. Enrollment for the branch
    plt.plot(branch_data["Year"], branch_data["Enrollment"], label=branch)

plt.title("Engineering Branch Enrollment Trends (2005–2024) with Variable Growth") # Updated title
plt.xlabel("Year")       # Label for the X-axis
plt.ylabel("Enrollment") # Label for the Y-axis
plt.legend()             # Display the legend to identify branches
plt.grid(True)           # Add a grid for better readability
plt.tight_layout()       # Adjust plot to ensure everything fits without overlapping
plt.show()               # Display the plot

# Print the first 35 rows of the DataFrame to show the generated data
print(df.head(35))


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as ran

# Years from 2005 to 2024
years = list(range(2005, 2025))

# Define the engineering branches and their base enrollment counts
# The 'growth' factor has been removed as per your request.
branches = {
    "name": ["Computer Science", "Mechanical", "Electrical", "Civil", "Chemical", "Electronics", "Aerospace"],
    "base": [1200, 1500, 1300, 1100, 800, 950, 350],  # Base count of individuals for each branch in 2005
}

data = []
# This dictionary will store the enrollment count for each branch from the previous year.
# It's initialized to 0, but will be set to the base enrollment for 2005 in the first iteration.
previous_year_enrollment = {name: 0 for name in branches["name"]}

# Loop through each year to simulate enrollment
for year in years:
    # Loop through each engineering branch
    for i in range(len(branches["name"])):
        name = branches["name"][i]
        base = branches["base"][i]

        current_enrollment = 0
        if year == 2005:
            # For the initial year (2005), enrollment starts from the base value
            # with a small random variation to make it less deterministic.
            # Random variation between -2% and +5% of the base.
            random_initial_variation = ran.uniform(-2.0, 3.0, size = 6)
            current_enrollment = int(max(0, base * (1 + random_initial_variation / 100)))
        else:
            # For subsequent years, enrollment is based on the previous year's enrollment
            # and a new random growth/decline percentage.
            # Random growth/decline between -5% and +8% of the previous year's enrollment.
            random_growth_percent = ran.uniform(-5.0, 8.0)
            current_enrollment = int(max(0, previous_year_enrollment[name] * (1 + random_growth_percent / 100)))

        # Append the calculated enrollment data for the current year and branch
        data.append({
            "Year": year,
            "Branch": name,
            "Enrollment": current_enrollment
        })

        # Update the previous year's enrollment for this specific branch
        # This value will be used in the next iteration (for the next year).
        previous_year_enrollment[name] = current_enrollment

# Create a Pandas DataFrame from the collected data
df = pd.DataFrame(data)

