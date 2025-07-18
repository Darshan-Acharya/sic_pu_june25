import pandas as pd
import random as ran

class engg_enrollment_analysist:
    def __init__(self, start_year=2005, end_year=2024):
        self.start_year = start_year
        self.end_year = end_year
        self.years = list(range(start_year, end_year + 1))
        
        # Branch names and base enrollment values
        self.branches = {
            "name": ["Computer Science", "Mechanical", "Electrical", "Civil", "Chemical", "Electronics", "Aerospace"],
            "base": [1600, 1000, 1000, 900, 700, 950, 350] # Base enrollment for 2005
        }

        # Generate random growth rate between -2% and +5% for each branch
        self.growth_rates = [ran.uniform(-0.02, 0.05) for _ in self.branches["name"]]
        self.data = []

    def generate_data(self):
        for year in self.years:
            for i in range(len(self.branches["name"])):
                name = self.branches["name"][i]
                base = self.branches["base"][i]
                growth = self.growth_rates[i]

                # Calculate years since start of the enrollment for better stabilization for the random data
                years_elapsed = year - self.start_year

                # compound growth calculation for the stabalized random data generation
                mean_enrollment = base * ((1 + growth) ** years_elapsed)

                random_variation = ran.uniform(-0.02, 0.05)
                enrollment = int(max(0, mean_enrollment * (1 + random_variation)))

                self.data.append({
                    "Year": year,
                    "Branch": name,
                    "Enrollment": enrollment
                })
        return self.data

    def save_to_csv(self, filename="enrollment_data.csv"):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

simulator = engg_enrollment_analysist()
simulator.generate_data()
simulator.save_to_csv("enrollment_data.csv")               
data = simulator.data 
