import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([1,4,9,16,25])

fig,axes=plt.subplots(2,2)
axes[0,0].plot(x,y,
               color='red'
               )
axes[0,0].set_title("0,0 plot")

axes[0,1].plot(x*2,y*3,
               color='blue'
               )
axes[1,0].plot(x-2,y*3,
               color='green'
               )

axes[1,0].set_title("1,0 plot")

axes[1,1].plot(x*2,y*3,
               color='orange'
               )
axes[1,1].set_title("1,1 plot")


axes[0,1].set_title("0,1 plot")


plt.tight_layout()


plt.show()