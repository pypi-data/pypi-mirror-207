import numpy as np
from envmap import EnvironmentMap, rotation_matrix
from matplotlib import pyplot as plt
from tools3d.spharm import SphericalHarmonic


#from spherical_harmonics import applyWindowing, getCoefficientsFromImage, getCoefficientsMatrix, getDiffuseCoefficients, l_from_idx

# def prefilter_diffuse(envmap):
# 	h, w, c = envmap.shape
# 	ibl_coeffs = applyWindowing(getCoefficientsFromImage(envmap, lmax=2))
# 	sh_basis_matrix = getCoefficientsMatrix(w, lmax=2)
# 	diffuse_coeffs = getDiffuseCoefficients(lmax=2)
# 	prefiltered_envmap = np.zeros((h, w, 3))
# 	for idx in range(0, ibl_coeffs.shape[0]):
# 		l = l_from_idx(idx)
# 		coeff_rgb = diffuse_coeffs[l] * ibl_coeffs[idx,:]
# 		prefiltered_envmap[:,:,0] += sh_basis_matrix[:,:,idx] * coeff_rgb[0]
# 		prefiltered_envmap[:,:,1] += sh_basis_matrix[:,:,idx] * coeff_rgb[1]
# 		prefiltered_envmap[:,:,2] += sh_basis_matrix[:,:,idx] * coeff_rgb[2]
# 	prefiltered_envmap[prefiltered_envmap < 0] = 0
# 	return prefiltered_envmap


e = EnvironmentMap("pano.jpg", "latlong")
#e.rotate(rotation_matrix(azimuth=np.pi/2, elevation=0, roll=np.pi/2-0.3))#.rotate(rotation_matrix(azimuth=0, elevation=np.pi/2))
#spharm = prefilter_diffuse(e.data[:,:,0:1])
spharm_repr = SphericalHarmonic(e, max_l=8)
spham_reconstruction = spharm_repr.reconstruct(31, max_l=4, clamp_negative=True)
spharm_repr.window()
spham_reconstruction_window = spharm_repr.reconstruct(31, max_l=4, clamp_negative=True)
#import pdb; pdb.set_trace()
e_ori = e.copy()
e.resize(64)
e_resized = e.copy()
e.blur(15)
print(e.data.mean(axis=(0,1)))
sa = e.solidAngles()[:,:,None]
print((sa*e_resized.data).mean(axis=(0,1)))
print((sa*e.data).mean(axis=(0,1)))
print((sa*spham_reconstruction).mean(axis=(0,1)))
print((sa*spham_reconstruction_window).mean(axis=(0,1)))
plt.subplot(321); plt.imshow(e_ori.data); plt.title("Original")
plt.subplot(322); plt.imshow(e.data); plt.title("Spatial blurring")
plt.subplot(323); plt.imshow(e_resized.data); plt.title("Resized (64)")
plt.subplot(324); plt.imshow(spham_reconstruction); plt.title("Spherical harmonics (frequency) blurring")
plt.subplot(325); plt.imshow(spham_reconstruction_window); plt.title("Spherical harmonics (frequency) blurring w/ window")
plt.show()
