
## Month 1 :GIS FOUNDATIONS AND DATA ECOSYSTEM
## Week 1: Project Brief

### Part 1: The question
Which ward in Maiduguri Metropolitan Council, Borno State is more than 5 km from a police station?

### Part 2: Why it matters
This question identifies wards in Maiduguri Metropolitan Council where both inhabitants and security personnel have to travel 5 km to report or contain a situation that requires urgent security intervention. The Federal Government of Nigeria, Borno State Government, and stakeholders can use this information for the siting of emergency police outposts and the rehabilitation of dilapidated road networks in underserved wards, for better urban security and safety.

### Part 3: The data needed
1. Nigeria ward-level data
2. Nigeria LGA-level data
3. Nigeria state boundary data
4. Police stations in MMC, Borno State, Nigeria
5. Road data for MMC, Borno State, Nigeria

### Part 4: Where each dataset came from

| Data | Source |
|------|--------|
| Nigeria ward-level data | GRID3 NGA Operational Wards v3.0 (July 2020) – 128 MB. https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v3-0/about |
| Nigeria LGA-level data | GRID3 NGA Operational LGA Boundaries (December 2020) – 2.6 MB. https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about |
| Nigeria state boundary data | GRID3 NGA Operational State Boundaries (December 2020) – 645 KB. https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/about |
| Police stations in MMC, Borno State | GRID3 NGA Police Station Locations (September 2020) – 76.3 KB. https://data.grid3.org/search?q=police — Maiduguri data was unavailable on GRID3 and OpenStreetMap, so I obtained it from Google Earth Pro as XYZ, exported and converted it to a shapefile. Google Earth Pro: https://www.google.com/earth/versions/#earth-pro |
| Road data for MMC, Borno State | Extracted using the QuickOSM plugin in QGIS. https://plugins.qgis.org/plugins/QuickOSM/ |

### Part 5: What I would build
An interactive web map of Maiduguri Metropolitan Council showing every ward in relation to its distance to the nearest police station, flagging wards that are beyond 5 km from a police station, as well as possible monthly-updated crime danger zones/wards sourced from ACLED data. This supports better attention from the public and security personnel, and the map can be updated monthly as new police outposts are added. It would be accessible on computer or mobile to aid better management and monitoring of urban security and security infrastructure.


## Week 02 : Data Note

### Dataset 1: Police Stations in Maiduguri

- **Source Link:** Google Earth Pro KML export
- **Number of Features:** 8
- **Key Columns:** `Stations`, `Northing`, `Easting`, `Elevation`
- **Geometry Type:** Point
- **Gaps or Missing Values Noticed:** No missing values in the Station names column. The original coordinates were inaccurate, so I updated them using KML data from Google Earth Pro.

### Dataset 2: [Admistrative Boundaries] admin 2

- **Source Link:**[https://data.humdata.org/dataset/cod-ab-nga/resource]
- **Number of Features:** [774]
- **Key Columns:** [adm2_name,adm2_pcode,adm2_name,area_sqm]
- **Geometry Type:** polygon [multiPolygon]
- **Gaps or Missing Values Noticed:** there is no missing value.

### Dataset 3: Roads (Nigeria)
- **Source Link:** [https://data.humdata.org/dataset/nigeria-roads)]
- **Number of Features:** 4709
- **Geometry Type:** Line
- **Key Columns:** RTT_DESCRI (Route Type), MED_DESCRI (Median), F_CODE_DES (Feature Code), DESCRIPTIO
- **Data Gaps / Missing Values:** The data set has 7 field and uses the 
EPSG4326 (WGS 84) coordinate system.the description colum has a 30 character limit, which truncates longer text value (e.g "other road and tr...").no blank cells were immeditely visible in the attribute table.

---

## Month 2: DEVELOPMENT ENVIROMENT AND EARLY PYTHON

## Week 5: Set up Python, VS Code and the terminal. hello.py runs

## WEEK 6: Enviroments and project setup with UV and added pandas. check.py prints the pandas version
## WEEK 7: Python,the six ideas:analyse.py reads wards.csv convert each area and classify each ward.
