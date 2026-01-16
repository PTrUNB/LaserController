#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt

result = {}
f = open(sys.argv[1],'r')
x = []
v1 = []
v2 = []
v3 = []
v4 = []
for line in f:
    if ',' in line:
        data = line.replace('\n','').replace('V','').split(',')
        if len(data) == 5:
            print(data)
            x.append(float(data[0]))
            v1.append(float(data[1]))
            v2.append(float(data[2]))
            v3.append(float(data[3]))
            v4.append(float(data[4]))

print(x)
indices = np.argsort(x)

x = np.array(x)[indices]
v1 = np.array(v1)[indices]
v2 = np.array(v2)[indices]
v3 = np.array(v3)[indices]
v4 = np.array(v4)[indices]
fig, ax1 = plt.subplots()

ax1.plot(x,v1,marker='x')
ax1.plot(x,v2,marker='x')
ax1.plot(x,v3,marker='x')
ax1.plot(x,v4,marker='x')
ax1.set_xlabel('Vin')
ax1.set_ylabel('Vout')

ax2 = ax1.twinx()
ax2.plot(x[1:-1],(v1[2:]-v1[:-2])/(x[2:]-x[:-2]))
ax2.plot(x[1:-1],(v2[2:]-v2[:-2])/(x[2:]-x[:-2]))
ax2.plot(x[1:-1],(v3[2:]-v3[:-2])/(x[2:]-x[:-2]))
ax2.plot(x[1:-1],(v4[2:]-v4[:-2])/(x[2:]-x[:-2]))
ax2.set_ylabel('dVin/dVout')

plt.suptitle("Vin to Vout")
plt.title(sys.argv[1]+"\nVDD=+15V VEE=-15V")
plt.tight_layout()
plt.show()

