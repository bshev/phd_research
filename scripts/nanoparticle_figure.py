import h5py as h5
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from skimage.filters import threshold_otsu


# Reading images and metadata
img_list = []
metadata_list = []

for file in os.listdir('data/'):
    if 'nanoparticles' in file:
        with h5.File(f'data/{file}', 'r') as h5file:
            img = h5file['data'][:].astype(np.float32)
            metadata = {key: h5file['data'].attrs[key] for key in h5file['data'].attrs}

            img_list.append(img)
            metadata_list.append(metadata)

# Creating binary thresholds using otsu method
binlist = []
for i in img_list:
    t = threshold_otsu(i)
    binary = i > t
    binlist.append(binary)

# Select image index 3
idx = 3
img = img_list[idx]
binary = binlist[idx]
scale = metadata_list[idx].get('scale')

# Scale bar settings
SCALEBAR_HEIGHT = 50
SCALEBAR_OFFSET = 20
scalebar_length = 100 / scale  # 100 nm scalebar

# Create 2x1 figure
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Left: regular image with scale bar
ax[0].imshow(img, cmap='viridis')
ax[0].axis('off')

# Add scale bar
scalebar_coords = (SCALEBAR_OFFSET, img.shape[0] - SCALEBAR_OFFSET - SCALEBAR_HEIGHT)
scalebar = Rectangle(scalebar_coords, scalebar_length, SCALEBAR_HEIGHT,
                     facecolor='white', edgecolor='k')
ax[0].add_patch(scalebar)
ax[0].text(SCALEBAR_OFFSET, img.shape[0] - SCALEBAR_OFFSET - SCALEBAR_HEIGHT - SCALEBAR_OFFSET,
           '100 nm', fontsize=18, color='white')

# Right: binary image
ax[1].imshow(binary, cmap='Reds')
ax[1].axis('off')

plt.tight_layout()
plt.savefig('nanoparticles.png', dpi=300)
plt.show()
