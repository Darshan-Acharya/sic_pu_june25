import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)
df.to_csv('output.csv', index=False)
df = pd.read_csv('output.csv')  # Reads the CSV file
df.head()  # Displays the first 5 rows
print(df.isnull().sum())  # Counts missing values in each column
grouped = df.groupby('Age')['Salary'].mean() 
# Groups by Age and calculates mean salary
print(grouped)