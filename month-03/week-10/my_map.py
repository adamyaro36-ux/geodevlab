import geopandas as gpd
import matplotlib.pyplot as plt


polygons = gpd.read_file("analysis_ready.gpkg", layer="maiduguri_clipped")
points = gpd.read_file("data/processed/my_points.gpkg", layer="my_points")


fig, ax = plt.subplots(figsize=(8, 8))


polygons.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")


points.plot(ax=ax, color="#094923", markersize=30, zorder=2)


ax.set_title("Police Stations in Maiduguri")
ax.set_axis_off()


fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("My map saved!")