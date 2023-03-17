import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,1,1,1,1,1,1,1,1,1]
colors = [1,2,3,4,5,6,7,8,9,10]

# plt.scatter(x,y, s=200, c=colors, cmap="bwr")
plt.scatter(x,y, s=200, c=colors, cmap="viridis") #'viridis, plasma, Greys
cbar = plt.colorbar(orientation="vertical", pad=0.05)
cbar.set_label(label="Concentrations", size=15)
plt.show()