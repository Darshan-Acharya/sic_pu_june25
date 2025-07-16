'''import pandas as pd
import matplotlib.pyplot as plt
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
plt.pie()
print(df)
df.to_csv('output.csv', index=False)
df = pd.read_csv('output.csv')  # Reads the CSV file
df.head()  # Displays the first 5 rows
print(df.isnull().sum())  # Counts missing values in each column
grouped = df.groupby('Age')['Salary'].mean() 
# Groups by Age and calculates mean salary
print(grouped)'''
import matplotlib.pyplot as plt

sizes = [30, 20, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['blue', 'red', 'green', 'purple']

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.show()