import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Business_Financial.csv')

type_count=df['Sector'].value_counts(ascending=True)

plt.bar(type_count.index, type_count.values,
        
        color=['green', 'orange', 'blue', 'red', 'purple'],
       edgecolor='black'
        )


plt.xlabel('Sector Type')
plt.ylabel('Count')
plt.title('Count of Businesses by Sector',fontsize=15)
plt.show()