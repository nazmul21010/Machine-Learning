import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
import pandas as pd


df=pd.read_csv('student.csv')

sns.kdeplot(df['Attendance'],fill=True)
sns.set_style('ticks')
plt.show()
 