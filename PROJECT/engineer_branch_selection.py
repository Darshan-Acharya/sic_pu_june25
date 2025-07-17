import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Data_acquistion import engg_enrollment_analysist

data = engg_enrollment_analysist.generate_data()
df = pd.DataFrame(data)
print(df.head())
#df = pd.read_csv("enrollment_data.csv")

# yearly_grouped_data = df["2005"]
# print(yearly_grouped_data.head())
# grouped = df.groupby(['Year', 'Branch'])['Enrollment'].sum().reset_index()
# print(df["year"].head)



