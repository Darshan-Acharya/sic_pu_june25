import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as ran
years = list(range(2005, 2025))#as per the two decades of the data 

# Engineering branches
branches = [
    "Computer Science",
    "Mechanical",
    "Electrical",
    "Civil",
    "Chemical",
    "Electronics",
    "Aerospace"
]

# Base enrollments excluding the diploma students and the Master student for optimization
base_enrollments = {
    "Computer Science": 1200,
    "Mechanical": 1500,
    "Electrical": 1300,
    "Civil": 1100,
    "Chemical": 800,
    "Electronics": 900,
    "Aerospace": 350
}

# Growth rates per year (can be positive or negative for trend)
growth_rates = {
    "Computer Science": 0.05,  # 5% annual growth
    "Mechanical": -0.01,       # slight decline
    "Electrical": 0.01,        # slight growth
    "Civil": 0.00,             # stable
    "Chemical": -0.02,         # decline
    "Electronics": 0.02,       # moderate growth
    "Aerospace": 0.03          # moderate growth
}

ran.uniform(-2.0, 5.0)  # for reproducibility
data = []

for year in years:
    for branch in branches:
        years_since_2005 = year - 2005
        # Calculate enrollment with compound growth + noise
        mean_enrollment = base_enrollments[branch] * ((1 + growth_rates[branch]) ** years_since_2005)
        # Add random noise +- around 5% of mean enrollment
        noise = np.random.normal(0, 0.05 * mean_enrollment)
        enrollment = int(max(0, mean_enrollment + noise))  # no negatives
        
        data.append({
            "Year": year,
            "Branch": branch,
            "Enrollment": enrollment
        })

# Create DataFrame
df = pd.DataFrame(data)

# Display first 15 rows to check
print(df.head(20))

