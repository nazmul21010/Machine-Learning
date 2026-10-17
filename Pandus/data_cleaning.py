import pandas as pd


df=pd.read_csv('Business_Financial.csv')

#droping the columns which are not required for the analysis
#df=df.drop(columns=["Sector","Id"])

#handling missing values by filling them with the mean of the respective columns

#df=df.dropna(subset=['Sector'])

#df=df.fillna({'Sector':"None"})

#Fix inconsistent data by standardizing the format of the 'Sector' column

#df['Sector']=df['Sector'].replace({'IT': "it",
                                   
#                                 'None':"Retail"})

#Standardize text
#df["Sector"]= df["Sector"].str.upper()

# fix data type
#df['Revenue']=df['Revenue'].astype(float)

#remove duplicates

df=df.drop_duplicates()

print(df.to_string()) 