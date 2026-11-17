from pyproj import Transformer

# Set up the transformer to go from WGS84 to UTM 31N
to_utm = Transformer.from_crs("EPSG:4326", "EPSG:32631", always_xy=True)

# Transform a point
x, y = to_utm.transform(3.8964, 7.4443)
print("UTM easting:", round(x, 1), "northing:", round(y, 1))