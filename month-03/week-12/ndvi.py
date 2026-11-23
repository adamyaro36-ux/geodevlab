import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Note: You MUST change these file names to match the exact names of the bands in your data/raw/landsat/ folder!
red_path = "data/raw/landsat/LC09_L2SP_191055_20260115_20260117_02_T1_SR_B4.TIF"
nir_path = "data/raw/landsat/LC09_L2SP_191055_20260115_20260117_02_T1_SR_B5.TIF"

with rasterio.open(red_path) as red_src:
    red = red_src.read(1, masked=True)
    profile = red_src.profile

with rasterio.open(nir_path) as nir_src:
    nir = nir_src.read(1, masked=True)

# Apply scale factor
red = red * 0.0000275 - 0.2
nir = nir * 0.0000275 - 0.2

# Calculate NDVI
np.seterr(divide='ignore', invalid='ignore')
ndvi = (nir - red) / (nir + red)
ndvi = np.ma.masked_invalid(ndvi)

# Plot and save as PNG
plt.figure(figsize=(10, 8))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.title('NDVI Map')
plt.axis('off')
plt.savefig("month-03/week-12/ndvi_map.png", dpi=300, bbox_inches='tight')

# Save the NDVI as a GeoTIFF file for the next steps
profile.update(
    dtype=rasterio.float32,
    count=1,
    compress='lzw'
)

import os
if not os.path.exists("data/processed"):
    os.makedirs("data/processed")

with rasterio.open("data/processed/ndvi.tif", "w", **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)
print("NDVI map saved as ndvi_map.png")