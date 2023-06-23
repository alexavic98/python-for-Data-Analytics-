#importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.ion()


#importing the dataframes
monthly_death = pd.read_csv(r"C:\Users\USER\Desktop\python training projects\handwashing\Data\monthly_deaths.csv")
yearly_death = pd.read_csv(r"C:\Users\USER\Desktop\python training projects\handwashing\Data\yearly_deaths_by_clinic.csv")

#explorin the data
monthly_death.info()
monthly_death.describe()
print(monthly_death.head(3))
print(monthly_death.isnull)
yearly_death.info()
yearly_death.describe()
print(yearly_death.head(3))

print(yearly_death["clinic"].describe())

#correlation
 

#evaluate the number of death from 1841 to 1846
print(yearly_death.groupby("clinic") ["deaths"].sum())

#calculatin for the proportion of deaths
yearly_death["death proportion"] = yearly_death["deaths"]/ yearly_death["births"]
print(yearly_death)

#separate the table into the two diff clinic

clinic_1 = yearly_death.where(yearly_death["clinic"] != "clinic 1")
clinic_2 = yearly_death.where(yearly_death["clinic"] != "clinic 2")
print(clinic_1)
print(clinic_2)


#visualise the number of death every year in the clinics

plt.hist(clinic_1["year"], clinic_1["deaths"], color= "green")
plt.title("deaths in clinic 1")
plt.xlabel("deaths",fontsize=14)
plt.ylabel("year", fontsize=14)
plt.show()
