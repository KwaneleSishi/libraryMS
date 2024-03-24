#Task 3: Data analysis using python (lists and data frames for managing books and members). 
""" Task 3: Data analysis using python (lists and data frames for managing books and members). 
You are provided with insurance dataset on blackboard. Please logon on blackboard and download the dataset. Write a python code to: 
§	Read the dataset. 
§	Inspects its column by displaying the first 10 records. 
§	Display records for make and usage for sets_num that are more than 40. 
§	Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes
     """
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
file_path = "C:/Users/HP/Downloads/motor_insure.csv/motor_data11-14lats.csv"
insurance_data = pd.read_csv(file_path)

# Inspect the first 10 records
print("First 10 records:")
print(insurance_data.head(10))

# Displaying records for make and usage for sets_num that are more than 40
filtered_data = insurance_data[insurance_data['sets_num'] > 40]
print("\nRecords for make and usage for sets_num that are more than 40:")
print(filtered_data[['make', 'usage']])

# Plotting a basic graph
plt.figure(figsize=(10, 6))
plt.scatter(insurance_data['carrying_capacity'], insurance_data['effective_yr'], color='blue')
plt.title('Carrying Capacity vs. Effective Year')
plt.xlabel('Carrying Capacity')
plt.ylabel('Effective Year')
plt.grid(True)
plt.show()