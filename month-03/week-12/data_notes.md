# Week 12 Data Notes

I used the teaching data provided by the instructor for both the guided practicals and the independent challenge.

## Rasters Used:
* **DEM:** `dem.tif` (provided in `data/raw/`). It covers the Ibadan North area with a CRS of EPSG:32631.
* **Landsat Bands:** `LC09_L2SP_191055_20260115_20260117_02_T1_SR_B4.TIF` (Red) and `LC09_L2SP_191055_20260115_20260117_02_T1_SR_B5.TIF` (NIR). These are Landsat 9 Level-2 surface reflectance products provided in `data/raw/landsat/`.

## Vector Data Used:
* **Wards:** `wards.gpkg` (provided in `data/processed/`). Used for clipping the DEM and calculating zonal statistics.
* **Facilities:** `facilities.gpkg` (provided in `data/processed/`). Used for sampling elevation points.

*Note: No large raster files (`.tif`) are committed to this repository as per the assignment instructions.*