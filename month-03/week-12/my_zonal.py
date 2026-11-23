import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("data/raw/dem.tif") as src:
    wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

wards["mean_elevation_m"] = np.round(means, 1)

# Save as CSV in the week-12 folder
wards[["ward_name", "mean_elevation_m"]].to_csv("month-03/week-12/my_zonal.csv", index=False)
print("Saved my_zonal.csv")