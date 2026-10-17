import matplotlib.pyplot as plt
import numpy as np


x=np.array([0,1,1,2,3,4,5,6,7,7,8])
y=np.array([55,60,65,62,68,70,75,78,82,85,87])

x2=np.array([0,1,2,3,4,4,5,5,9])
y2=np.array([50,55,60,65,70,75,80,85,90])

plt.title('Scatter Graph')
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')

plt.scatter(x,y,
            color='blue',
            alpha=0.5,
            s=120,
            label='Class A'
            )

plt.scatter(x2,y2,
            color='red',
            alpha=0.5,
            s=120,
            label='Class B'
            )


plt.legend()
plt.show()

