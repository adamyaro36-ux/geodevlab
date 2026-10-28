# Month 1 Summary

## My Question
Which ward in Maiduguri Metropolitan Council, Borno State is more than 5 km from a police station?

## Operation Chosen
I used a Spatial Join (Join Attributes by Nearest). 
**Why:** I chose this operation because it allowed me to calculate the exact distance from the center of every ward to its closest police station, which I could then use to answer my question.

## Expectations vs. Results
*   **What I Expected:** I expected to find roughly 3 or 4 wards that were more than 5 km away, likely on the outer edges of the map. I also expected the final table to have exactly 15 rows (one for each ward).
*   **What I Got:** I got 16 rows because one ward was exactly equidistant from two different police stations, creating a duplicate. More importantly, I found that **zero** wards are more than 5 km away. The maximum distance of any ward to a police station was approximately 1.49 km (1489 meters).

## What Surprised Me
I was very surprised that no ward is further than 1.5 km from a station. This shows that the police stations are very centrally and evenly distributed across the Metropolitan Council. I was also surprised that the tool created a duplicate row for one of the wards (Maisandari) because it couldn't decide which of two equidistant stations to pick.

## Data I Still Need
The straight-line distance (as the crow flies) doesn't account for actual travel time. I still need the road network data to calculate how long it actually takes to drive from the outer wards to the police stations. I also need data on the capacity and staffing of these police stations to know if they can actually serve the populations of these wards.