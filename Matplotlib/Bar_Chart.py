import matplotlib.pyplot as plt
 
import numpy as np

categories=np.array(["Grains","Fruits","Vegetables","Dairy","Meat"])
values=np.array([20,25,35,98,25])

#plt.barh(categories,values,color="skyblue")

plt.bar(categories,values,color="skyblue",edgecolor="black",linewidth=0.5)
plt.title("Daily Consumption of Food Categories",
          fontsize=14,
          fontfamily="arial",
          style="italic",
          color="black")

plt.xlabel("Food Categories")
plt.ylabel("Consumption")

#plt.xticks(rotation=45)
plt.tick_params(axis='x',
                colors='blue'
)
                

plt.show()