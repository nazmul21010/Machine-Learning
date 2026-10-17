import matplotlib.pyplot as plt
import numpy as np

x=np.array([2020,2021,2022,2023,2024,2025,2026])
y=np.array([1008,875,865,654,789,456,321])

plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Death Rate')
plt.show()
