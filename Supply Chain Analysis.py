#importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


#importin the supply chain dataset
df = pd.read_csv(r"C:\Users\USER\Desktop\python training projects\Supplychain\supply_chain_data.csv")
df.describe()
df.head(3)
df.groupby("Product type")
print(df)
#sales by product type
#using pie chart to display the sales in percentage
grouped_data = df.groupby("Product type").sum()
plt.pie(grouped_data["Number of products sold"], labels=grouped_data.index, autopct='%1.1f%%')

plt.show()

#45% of the business comes from skincare products, 29.5% from haircare, and 25.5% from cosmetics
#location with their number of sales
mumbai_sales = df.groupby(df["Location"])
sales_by_location = mumbai_sales["Number of products sold"].sum()
print(sales_by_location)

#location with the highest number of sales using pie chart
grouped_location = df.groupby(df["Location"]).sum()
plt.pie(grouped_location["Number of products sold"], labels=grouped_location.index, autopct='%1.1f%%')
plt.show()
#kolkkata has the highest number of products sold (27.7%)
#total revenue generated from  different shipping carriers
grouped_shipping_carriers = df.groupby("Shipping carriers")
Revenue_generated = grouped_shipping_carriers["Revenue generated"].sum()
print(Revenue_generated)
plt.pie(Revenue_generated,  labels=Revenue_generated.index, autopct='%1.1f%%')
plt.title ("revenue generated from  different shipping carriers")

plt.show()
#carrier B is seen to have generated more revenue (43.3%)
#cost distribution by transportation mode
print(df.columns)
grouped_transportation_mode = df.groupby("Transportation modes")
transportation_modes = grouped_transportation_mode["Costs"].sum()
print(transportation_modes)
plt.pie(transportation_modes, labels=transportation_modes.index, autopct= "%1.1f%%")
plt.title("cost of different transportation modes")

plt.show()
#Sea modes of transportation cost lesser than other modes