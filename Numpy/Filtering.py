import numpy as np

ages=np.array([[21,17,13,19,20,18,89,26,12,15,45],
               
               [22,16,14,18,21,17,50,25,13,14,44],])


teenagers=ages[ages<18]
#adults=ages[(ages>=18) & (ages<40)]
seniors=ages[ages>=50]


adults=np.where(ages>=18,ages,0)

print(adults)
