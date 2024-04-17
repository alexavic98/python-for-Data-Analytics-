#Demand and Supply analysis means analyzing the relationship between the quantity demanded and the quantity supplied. 
# It helps businesses understand the factors influencing consumer demand to maximize profits.


#importing the necessary libraries and dataset

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\USER\Desktop\python training projects\Demand and supply\rides.csv")

#cleaning the dataset   
df_nulls = df.isnull().sum()
print(df_nulls)
#To drop the entire columns and rows with null values
#data = df.dropna()
#print(data)

#But we will prefare to fill in the nulls with the mean value
mean = df["Rides Completed"].mean()
int(mean)
print(mean)

np.where(df["Rides Completed"].isnull(),107, df["Rides Completed"])
print(df)

#Showing the relationship between the number of drivers active per hour and the number of rides active per hour
demand = df["Riders Active Per Hour"]
supply = df["Drivers Active Per Hour"]
plt.scatter(demand, supply)
plt.xlabel("demand")
plt.ylabel("supply")
plt.title("Relationship between demand and supply")
plt.show()

#calculating the elasticity of demand for rides concerning the number of active drivers per hour
avg_demand = df['Riders Active Per Hour'].mean()
avg_supply = df['Drivers Active Per Hour'].mean()
pct_change_demand = (max(df['Riders Active Per Hour']) - min(df['Riders Active Per Hour'])) / avg_demand * 100
pct_change_supply = (max(df['Drivers Active Per Hour']) - min(df['Drivers Active Per Hour'])) / avg_supply * 100

elasticity = pct_change_demand / pct_change_supply
print("Elasticity of demand with respect to the number of active drivers per hour:", elasticity)
#It signifies a moderately responsive relationship between the demand for rides and the number of active drivers per hour. 
# Specifically, this means that a 1% increase in the number of active drivers per hour would lead to a 0.82% decrease in the demand for rides, 
# while a 1% decrease in the number of active drivers per hour would lead to a 0.82% increase in the demand for rides.

#Calculating the supply ratio for each level of driver activity
df['Supply Ratio'] = df['Rides Completed'] / df['Drivers Active Per Hour']
print(df.head())
