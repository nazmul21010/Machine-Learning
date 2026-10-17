import pandas as pd
df=pd.read_json("student_json.json")


print(df.to_string())
