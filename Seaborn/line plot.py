import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
import pandas as pd
 

df=pd.read_csv('student.csv')

x=np.array([1,5,4,8,9,6,5,6,6,7,8,10])
y=np.array([5,20,4,6,9,7,8,20,14,23,14,15])
y2=np.array([12,58,4,7,8,9,6,5,7,8,15,45])
x2=np.array([0,58,4,7,8,9,6,5,8,8,20,45])


sns.lineplot(x=x,y=y,
             color='green',
             markers='.'
             )

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('x axis vs y asxis')
sns.lineplot(x=x,y=y2)
plt.show()