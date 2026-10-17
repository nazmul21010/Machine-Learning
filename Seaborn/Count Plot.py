import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
import pandas as pd


df=pd.read_csv('student.csv')



sns.countplot(x="Math",
              hue='Gender',
              data=df)
plt.tight_layout()

plt.show()