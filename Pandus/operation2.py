import pandas as pd

#practies

df=pd.read_csv("student.csv",index_col="Name")

name=input("Enter the name of the student: ")

try:
    print(df.loc[name])
except KeyError:
    print(f"{name} not found.")