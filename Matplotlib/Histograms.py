import matplotlib.pyplot as plt
import numpy as np

scores=np.random.normal(loc=80,scale=50,size=100)

scores=np.clip(scores,0,100)

plt.hist(scores,
         bins=10,
         color='orange'
         )

plt.title('Exam Scores',fontsize=15,fontfamily='serif',fontweight='bold')
plt.xlabel('Score')
plt.ylabel('# Number of Students')
plt.show()