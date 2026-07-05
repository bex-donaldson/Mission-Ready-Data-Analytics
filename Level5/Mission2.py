# Mission 2: Exploring and Analyzing Data with Pandas
# Objective:

# In this mission, you will perform Exploratory Data Analysis (EDA) and basic data manipulation using Pandas. You will work with a dataset that includes information about employees and apply various data transformation techniques, including handling missing values, filtering, and performing basic data analysis.

# Dataset Overview:

# The dataset contains the following columns:
# employee_id: Unique identifier for each employee.
# name: Name of the employee.
# age: Age of the employee.
# department: The department where the employee works (e.g., HR, Engineering, Marketing).
# salary: Annual salary of the employee.
# work_experience: Number of years of work experience the employee has.

# Task 1: Load the Data
# Objective: Load the dataset into a Pandas DataFrame.

# Instructions:
# Create a DataFrame from the provided dataset.
# Display the first few rows of the dataset to ensure it loaded correctly.

import pandas as pd

# Create a basic dataset
data = {
    'employee_id': range(1, 21),
    'name': ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack', 'Karen', 'Leo', 'Mia', 'Nina', 'Olivia', 'Paul', 'Quinn', 'Rita'],
    'age': [22, 25, 28, 35, 40, 42, 50, 60, 65, 30, 28, 24, 37, 41, 48, 33, 29, 32, 45, 38],
    'department': ['HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales'],
    'salary': [50000, 60000, 55000, 75000, 80000, 85000, 100000, 110000, 120000, 65000, 67000, 72000, 85000, 90000, 95000, 48000, 67000, 70000, 80000, 88000],
    'work_experience': [1, 3, 5, 7, 10, 12, 15, 18, 20, 3, 1, 6, 4, 8, 5, 7, 3, 2, 6, 5],
}


df = pd.DataFrame(data)

display(df.head(5))

# Task 2: Data Exploration
# Objective: Explore the dataset to get an understanding of its structure.

# Instructions:
# Check for missing values in the dataset.
# Get the summary statistics of numeric columns (age, salary, work_experience).

# Check for missing values
missing_values = df.isnull()
rows_with_nulls = df[missing_values.any(axis=1)]

display(rows_with_nulls)

# Age Calculations
mean_age = df['age'].mean()
median_age = df['age'].median()
mode_age = df['age'].mode()[0]
std_age = df['age'].std()

print(f"Average Age: {mean_age}, Median Age: {median_age}, Mode Age: {mode_age}, Age Std Dev: {std_age}")

# Salary Calculations
mean_salary = df['salary'].mean()
median_salary = df['salary'].median()
mode_salary = df['salary'].mode()[0]
std_salary = df['salary'].std()

print(f"Average Salary: {mean_salary}, Median Salary: {median_salary}, Mode Salary: {mode_salary}, Salary Std Dev: {std_salary}")

# Work Experience Calculations
mean_work_experience = df['work_experience'].mean()
median_work_experience = df['work_experience'].median()
mode_work_experience = df['work_experience'].mode()[0]
std_work_experience = df['work_experience'].std()

print(f"Average Work Experience: {mean_work_experience}, Median Work Experience: {median_work_experience}, Mode Work Experience: {mode_work_experience}, Work Experience Std Dev: {std_work_experience}")

# Task 3: Data Transformation
# Objective: Perform basic data transformations such as creating new columns and renaming existing ones.

# Instructions:
# Create a new column called years_to_retirement by subtracting the age from 65.
# Rename the salary column to annual_salary.
# Sort the DataFrame based on work_experience in descending order.

# Creating a new Column 'years_to_retirement', calculating years by subtracting age from 64 
df['years_to_retirement'] = df['age'].apply(lambda x: 65 - x)
display(df)

# Renaming the 'salary' column to 'annual_salary'
df.rename(columns={'salary': 'annual_salary'}, inplace=True)
display(df)

# Sorting by 'work_experience' in descending order - for data to be ascending then ascending=False, for descending then ascending=true
sorted_df = df.sort_values(by='work_experience', ascending=False)
display(sorted_df)

# Task 4: Handling Missing Data
# Objective: Handle missing data (if any).

# Instructions:
# Introduce some missing values in the annual_salary column.
# Handle the missing data by either filling it with the mean salary or dropping the rows with missing values.

new_rows = pd.DataFrame({
    'employee_id': [21, 22, 23],
    'name': ['Sam', 'Tom', 'Uma'],
    'age': [34, 45, 29],
    'department': ['HR', 'Finance', 'Marketing'],
    'annual_salary': [None, None, None],
    'work_experience': [5, 10, 3]
})

# Create a new dataframe without modifying the original
df_new = pd.concat([df, new_rows], ignore_index=True)
df_new['years_to_retirement'] = 65 - df_new['age']
display(df_new)

# Handling missing values by filling them with the mean salary
mean_salary = df['annual_salary'].mean()
df_filled = df_new.copy()
df_filled['annual_salary'] = df_filled['annual_salary'].fillna(mean_salary)
display(df_filled.tail())

# Task 5: Data Filtering and Selection
# Objective: Select specific data based on conditions.

# Instructions:
# Filter the data to show only employees who are older than 30.
# Select only the columns name, age, and annual_salary.

filtered_df = df[df['age'] > 30]
final_filtered_df = filtered_df[['name', 'age', 'annual_salary']]
display(final_filtered_df)

# Task 6: Data Aggregation
# Objective: Perform group-based aggregation.

# Instructions:
# Group the data by department and calculate the average salary for each department.

average_salary_by_department = df.groupby('department')['annual_salary'].mean().reset_index()
display(average_salary_by_department)
