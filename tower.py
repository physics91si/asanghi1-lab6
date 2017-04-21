#!/anaconda/bin/python                                                          

import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate as inte

time, velocity=np.loadtxt('droptower_vdata.txt', unpack=True)

distanceArray=inte.cumtrapz(velocity,initial=0) +30
print(distanceArray)
accelArray=np.diff(velocity)
print(accelArray)
x2=np.arange(10)
plt.figure()
plt.plot(time,distanceArray)
plt.title('displacement')
plt.savefig('displacement.png')


plt.figure()
plt.plot(time,velocity)
plt.savefig('velocity.png')

plt.figure()
plt.plot(x2,accelArray)
plt.savefig('accel.png')
