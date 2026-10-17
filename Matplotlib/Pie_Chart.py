import matplotlib.pyplot as plt
import numpy as np

categories=['C','C++','Java','Python','PHP']
values=np.array([255,206,308,355,200])

plt.title("Programming Languages",fontsize=15,fontfamily='serif')

colors=['blue','orange','green','red','purple']

plt.pie(values,
        labels=categories,
        colors=colors,
        explode=[0,0,0,0.1,0],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )


plt.show()
