import numpy as np
from envmap import EnvironmentMap, rotation_matrix
from matplotlib import pyplot as plt


e = EnvironmentMap("pano.jpg", "latlong")
e.rotate(rotation_matrix(azimuth=np.pi/2, elevation=0, roll=np.pi/2-0.3))#.rotate(rotation_matrix(azimuth=0, elevation=np.pi/2))
e_ori = e.copy()
e.resize(64)
e_resized = e.copy()
e.blur(20)
print(e.data.mean(axis=(0,1)))
sa = e.solidAngles()[:,:,None]
print((sa*e_resized.data).mean(axis=(0,1)))
print((sa*e.data).mean(axis=(0,1)))
plt.subplot(131); plt.imshow(e_ori.data)
plt.subplot(132); plt.imshow(e.data)
plt.subplot(133); plt.imshow(e_resized.data)
plt.show()
