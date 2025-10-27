import os
import numpy as np
import matplotlib.pyplot as plt

print("Working directory:", os.getcwd())

with open("C:/Users/EmDie/Desktop/praktika 5b/Cluster66.txt", "r") as filedata:
    all_data = [line.split() for line in filedata.readlines()]

all_data = all_data[1:]
soubor = np.array([list(map(float, row)) for row in all_data])

# Store the computed r values
r_values = []

for i in range(573):
    vx = soubor[i][6]
    vy = soubor[i][7]
    vz = soubor[i][8]
    x = soubor[i][3]
    y = soubor[i][4]
    z = soubor[i][5]
    v = np.array([vx, vy, vz])
    u = np.array([x, y, z])
    u2 = float(np.sqrt(np.pow(x,2) + np.pow(y,2) + np.pow(z,2)))
    z_array = np.array([x/u2, y/u2, z/u2])
    r = np.dot(v, z_array)  # dot product to get scalar result
    r_values.append(r)
    mean_r = np.dot(v, z_array)
    r_values.append(r)
mean_r= np.mean(r_values)
print("Mean projection", mean_r)
 

# Fixed plot
plt.figure(figsize=(8, 6))
plt.hist(r_values, bins=50, alpha=0.7, edgecolor='black')
plt.xlim(-1, 1)
plt.xlabel("r values")
plt.ylabel("Frequency")
plt.title("Distribution of r values")
plt.grid(True, alpha=0.3)
plt.show()

