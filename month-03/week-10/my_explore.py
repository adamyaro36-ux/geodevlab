import geopandas as gpd

file_path = "analysis_ready.gpkg"


print("Layers in file:")
print(gpd.list_layers(file_path))


layer_name = "maiduguri_clipped" 


my_layer = gpd.read_file(file_path, layer=layer_name)


print(my_layer.head())
print("Rows and columns:", my_layer.shape)
print(my_layer.geom_type.value_counts())
print("CRS:", my_layer.crs)
print("Bounds:", my_layer.total_bounds)