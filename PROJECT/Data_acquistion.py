import pandas as pd
import Base as bas

df = bas.EnrollmentSimulator()

#group by the years
def group_data(self, group_by="Year"):
        if group_by not in ["Year", "Branch"]:
            print("Invalid grouping. Use 'Year' or 'Branch'.")
            return

        df = pd.DataFrame(self.data)
        grouped = df.groupby(group_by)["Enrollment"]

        print(f"\n Grouped Enrollment Data by {group_by}:\n")
        print(grouped)
        return grouped

high_salary = df[df['branch'] ]  # Filters rows based on Salary
print(high_salary)