import pandas as pd

data=[101.5,102.5,103.9,104.8]
data2=["A","B","C","D"]
data3=[True,False,True,True]

calories={"Day1":1750,"Day2":845,"Day":1420}


series=pd.Series(calories)


series.loc["Day3"] = 23500

print(series)

