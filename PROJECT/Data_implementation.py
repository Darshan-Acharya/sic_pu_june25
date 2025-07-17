import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Data_acquistion import engg_enrollment_analysist

df = pd.read_csv("enrollment_data.csv")

def plot_enrollment_trends():
    grouped = df.groupby(['Year', 'Branch'])['Enrollment'].sum().reset_index()
    plt.figure(figsize=(14, 8))
    for branch in grouped['Branch'].unique():
        branch_data = grouped[grouped['Branch'] == branch]
        plt.plot(branch_data['Year'], branch_data['Enrollment'], marker='o', label=branch)
    plt.title('Engineering Enrollment Trends by Branch (2005-2024)', color = "orange", fontsize = 25)
    plt.xlabel('Year')
    plt.ylabel('Enrollment')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_yearly_distribution(year):

    year = int(year)
    year_data = df[df['Year'] == year]
    plt.figure(figsize=(8, 8))
    plt.pie(year_data['Enrollment'], labels=year_data['Branch'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Enrollment Distribution by Branch in {year}', color = "orange", fontsize = 25)
    plt.axis('equal')
    plt.show()

def plot_growth_decline():
    first_year = df['Year'].min()
    last_year = df['Year'].max()

    first_year_data = df[df['Year'] == first_year].set_index('Branch')['Enrollment']
    last_year_data = df[df['Year'] == last_year].set_index('Branch')['Enrollment']

    growth = (last_year_data - first_year_data) / first_year_data * 100  # percentage growth

    plt.figure(figsize=(10, 6))
    growth_sorted = growth.sort_values()
    colors = ['green' if val >= 0 else 'red' for val in growth_sorted]
    growth_sorted.plot(kind='bar', color=colors)
    plt.ylabel('Growth % from {} to {}'.format(first_year, last_year))
    plt.title('Percentage Growth or Decline of Engineering Branch Enrollments', color = "orange", fontsize = 20)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.tight_layout()
    plt.show()