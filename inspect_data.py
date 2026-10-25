import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue # Skip empty cells
        values.append(float(raw))
        
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

# Call the function for your two columns
area_result = inspect_column("wards.csv", "area_km2")
pop_result = inspect_column("wards.csv", "population")

# Print the results
print("Area:", area_result)
print("Population:", pop_result)