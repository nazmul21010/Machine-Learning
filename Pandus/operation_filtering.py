import pandas as pd

df=pd.read_csv("student.csv")

#match condition
#tall_name=df[df["Session"]>="2020-21"]
#tall_name=df[(df["Id"]>=10) & (df["Id"]<=20)]

#tall_name=df[(df["Session"]>"2020-21") & (df["Session"]<="2022-23")]
#tall_name=df[(df["Id"]>=10)|
#             (df["Id"]<=15)]
tall_name=df[(df["Session"]=="2022-23")&(df["Id"]<=27)]

print(tall_name)