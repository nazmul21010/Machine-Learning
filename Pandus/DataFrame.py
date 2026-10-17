import pandas as pd

data = {
    
    "Name":["Spnogebob","Partrick","Squidward","Nazmul"],
    "Age":[30,35,50,45]
}

df=pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3","Employee 4"])

#add a new column
df["job"]=["Cook","N/A","Cashier","Oli"]

#add a new row
new_row=pd.DataFrame([{"Name":"Sandy","Age":28, "job":"Engineer"},
                      
                      {"Name":"Nazmul Islam","Age":25, "job":"Govement"}
                      ],index=["Employee 5","Employee 6"]) 


df=pd.concat([df,new_row])
print(df)
