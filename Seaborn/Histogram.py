import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
import pandas as pd


df=pd.read_csv('student.csv')

sns.histplot(df['Science'],bins=40,color='green',)

plt.show()
 