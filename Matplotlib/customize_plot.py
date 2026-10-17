import matplotlib.pyplot as plt
import numpy as np

x=np.array([2020,2021,2022,2023,2024,2025,2026])
y=np.array([1008,875,865,654,789,456,321])
y2=np.array([800,900,1000,1100,1200,1300,800])


line_style=dict(
    marker='.',
         markersize=15,
         markerfacecolor='white',
         linestyle='solid',
         color='black',
         linewidth=4
         )



plt.xlabel('Year',fontsize=14, fontweight='bold', color='black')
plt.ylabel('Death Rate',
           fontsize=14, fontweight='bold', color='black')
plt.title('Death Rate Over the Years',fontsize=16, fontweight='bold', color='black',fontfamily='arial')

#plt.grid(True)
#plt.grid(color='blue', linestyle='--', linewidth=0.5)

plt.plot(x,y,**line_style)
plt.plot(x,y2,**line_style)

plt.tick_params(axis='x', 
                colors='blue',
                )
plt.show()

