import numpy as np
import rasterio

red_path = "data/raw/landsat/LC09_L2SP_191055_20260115_20260117_02_T1_SR_B4.TIF"
nir_path = "data/raw/landsat/LC09_L2SP_191055_20260115_20260117_02_T1_SR_B5.TIF"

with rasterio.open(red_path) as red_src:
    red = red_src.read(1, masked=True)
    profile = red_src.profile

with rasterio.open(nir_path) as nir_src:
    nir = nir_src.read(1, masked=True)

red = red * 0.0000275 - 0.2
nir = nir * 0.0000275 - 0.2

np.seterr(divide='ignore', invalid='ignore')
ndvi = (nir - red) / (nir + red)
ndvi = np.ma.masked_invalid(ndvi)

print("Min NDVI:", round(float(ndvi.min()), 2))
print("Max NDVI:", round(float(ndvi.max()), 2))
print("Mean NDVI:", round(float(ndvi.mean()), 2))

profile.update(dtype=rasterio.float32, count=1, compress='lzw')

with rasterio.open("data/processed/my_index.tif", "w", **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

print("Saved my_index.tif")