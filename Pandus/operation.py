import pandas as pd

df=pd.read_csv("student.csv",index_col="Name")

#Select by collumn
#print(df[["Name","Id","Session"]].to_string())

#select by rows
#print(df.loc["Student5"])

#print(df.loc["Student5":"Student10",["Id","Department"]])
print(df.iloc[0:11:2,0:3:2])

