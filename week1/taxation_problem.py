#input
employee_name = input("Enter the employee name: ")
employee_ID = input("Enter the employee ID: ")
monthly_salary = int(input("Enter the basic monthly salary: "))
special_allowance = int(input("Enter the special allowance: "))
bonus = int(input("Enter the bonus (per year in %): "))
bonus/=100
gross_monthly_salary = monthly_salary + special_allowance 
gross_annual_salary = gross_monthly_salary * 12
gross_annual_salary += gross_annual_salary *bonus

#display
print("Employee ID: ",employee_ID)
print("Monthly salary is: ",gross_monthly_salary)
print("Gross annual salary(including bonus): ",gross_annual_salary)

#taxable income and standard deduction 
gross_annual_salary -= 50000
tax = 0
if gross_annual_salary >= 0 and gross_annual_salary <= 300000:
    tax = gross_annual_salary*0
elif gross_annual_salary <= 600000:
    tax = gross_annual_salary*(5/100)
elif gross_annual_salary <= 900000:
    tax  = gross_annual_salary*(10/100)
elif gross_annual_salary <= 1200000:
   tax = gross_annual_salary*(15/100)
elif gross_annual_salary <= 1500000:
    tax = gross_annual_salary*(20/100)
else:
    tax = gross_annual_salary*(30/100)

#rebate     
if gross_annual_salary <= 700000:
    tax = 0
tax += gross_annual_salary*(4/100)

print("Tax applied for you (including health and educaion tax)", tax)
net_annual_salary = gross_annual_salary - tax
print("The net salary after deduction of all taxes: ", net_annual_salary)
