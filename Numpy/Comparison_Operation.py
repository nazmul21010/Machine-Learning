import numpy as np

scores=np.array([85,70,68,94,75])

#print(scores>80)

scores[scores>70]=0

print(scores)