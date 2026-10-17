import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
import pandas as pd
 

df=pd.read_csv('student.csv')

sns.barplot(x='Gender', y='Math', data=df,
            
            palette=['pink','green'],
            edgecolor='black'
         )

sns.set_style('whitegrid')
sns.set_palette('crest')

legend_elements = [
    Patch(facecolor='orange', label='Male'),
    Patch(facecolor='green', label='Female')
]

plt.legend(handles=legend_elements)


plt.title('Male vs Female')
plt.tick_params(axis='both',colors='red')

plt.legend(handles=legend_elements)

plt.show()