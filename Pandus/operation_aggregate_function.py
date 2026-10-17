import pandas as pd

df=pd.read_csv("Business_Financial.csv")

# all numeric columns mean
#print(df.mean(numeric_only=True))
#print(f"{df['Revenue'].mean()} is the mean of Revenue column")
#print(f"{df['Profit'].mean()} is the mean of Profit column")

#print(f"{df['Profit'].sum()} is the sum of Profit column")
#print(f"{df['Profit'].max()} is the maximum of Profit column")
#print(f"{df['Profit'].min()} is the minimum of Profit column")
#print(f"{df['Profit'].count()} is the count of Profit column")

group=df.groupby('Sector')
print(group['Profit'].mean())
print(group['Profit'].sum())
print(group['Profit'].count())
print(group['Profit'].max())
print(group['Profit'].min())
