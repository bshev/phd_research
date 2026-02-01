import h5py as h5
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter, median_filter, gaussian_filter
from skimage.measure import label, regionprops
from matplotlib.patches import Rectangle

# Load HRSTEM image data and metadata
with h5.File('../data/HRSTEM.h5', 'r') as h5file:
    img = h5file['data'][:].astype(np.float32)
    metadata = {key: h5file['data'].attrs[key] for key in h5file['data'].attrs}

# Filter image
filtered_img = median_filter(img, 3)
filtered_img = gaussian_filter(filtered_img, 1, mode='constant')

# Local region to detect peaks
neighborhood = np.ones((10, 10)).astype(bool)
detected_peaks = (maximum_filter(filtered_img, footprint=neighborhood) == filtered_img).astype(np.int32)

# Verify that all detected peaks are a single pixel and find locations
peak_locations = []
label_image = label(detected_peaks)
for region in regionprops(label_image):
    assert region.area == 1
    peak_locations.append(region.centroid)

# Original window: 128:512 (384 pixels), 30% smaller = 268 pixels
# Center the smaller window in the same region
original_size = 384
new_size = int(original_size * 0.7)  # 268 pixels
padding = (original_size - new_size) // 2  # 58 pixels

start = 128 + padding  # 186
end = 512 - padding    # 454

# Plotting result with smaller window (30% reduction in both directions)
fig, ax = plt.subplots(1, 2, figsize=(16 * 0.7, 8 * 0.7))

im0 = ax[0].imshow(filtered_img[start:end, start:end], cmap='cividis')
ax[0].set_title("Filtered Data")

# Add scale bar to first image
scale_nm_per_pixel = metadata['scale']  # nm per pixel
scalebar_length_nm = 1.0  # 1 nm scale bar
scalebar_length_px = scalebar_length_nm / scale_nm_per_pixel

# Position scale bar in lower right
img_height, img_width = end - start, end - start
bar_x = img_width - scalebar_length_px - 10
bar_y = img_height - 15
bar_height = 5

ax[0].add_patch(Rectangle((bar_x, bar_y), scalebar_length_px, bar_height,
                           facecolor='white', edgecolor='white'))
ax[0].text(bar_x + scalebar_length_px / 2, bar_y - 5, '1 nm',
           color='white', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax[1].imshow(detected_peaks[start:end, start:end], cmap='viridis')
ax[1].set_title("Detected Peaks")

plt.tight_layout()
plt.savefig('../imgs/HRSTEMAtoms.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"Saved HRSTEMAtoms.png with {len(peak_locations)} peaks detected")
