# Week 02 Data Note

## Dataset 1: Police Stations in Maiduguri

- **Source Link:** Google Earth Pro KML export
- **Number of Features:** 8
- **Key Columns:** `Stations`, `Northing`, `Easting`, `Elevation`
- **Geometry Type:** Point
- **Gaps or Missing Values Noticed:** No missing values in the Station names column. The original coordinates were inaccurate, so I updated them using KML data from Google Earth Pro.

## Dataset 2: [Admistrative Boundaries] admin 2

- **Source Link:**[https://data.humdata.org/dataset/cod-ab-nga/resource]
- **Number of Features:** [774]
- **Key Columns:** [adm2_name,adm2_pcode,adm2_name,area_sqm]
- **Geometry Type:** polygon [multiPolygon]
- **Gaps or Missing Values Noticed:** there is no missing value.

## Dataset 3: Roads (Nigeria)
- **Source Link:** [https://data.humdata.org/dataset/nigeria-roads)]
- **Number of Features:** 4709
- **Geometry Type:** Line
- **Key Columns:** RTT_DESCRI (Route Type), MED_DESCRI (Median), F_CODE_DES (Feature Code), DESCRIPTIO
- **Data Gaps / Missing Values:** The data set has 7 field and uses the 
EPSG4326 (WGS 84) coordinate system.the description colum has a 30 character limit, which truncates longer text value (e.g "other road and tr...").no blank cells were immeditely visible in the attribute table.