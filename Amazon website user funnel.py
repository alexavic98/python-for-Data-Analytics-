#importing the necessary libraries
import pandas as pd 
import matplotlib as plt

#loading in the dataframe as df
df = pd.read_csv(r"C:\Users\USER\Desktop\python training projects\Amazon Website User Funnels\user_data.csv")
print(df.head(5))

#checking for missing values
null_values = df.isnull().sum() 
print(null_values)
# no missing value in the dataframe

#Showing the number of users at different  stages of the funnel
user_diff_stages = df["stage"].value_counts()
print(user_diff_stages)
# funnel stages of the website are homepage, product_page, cart, checkout, purchase.

#calculate the number of users and conversions for each stage
diff_stages = ["""homepage, product_page, cart, checkout, purchase"""]

for stages in diff_stages:
    stage_users = df[df["stage"] == stages]
    num_users = stage_users["user_id"].value_counts()
    print(num_users)
    
    
    
    