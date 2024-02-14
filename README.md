# CISC-499-XAI-For-Waste-Management-Using-EA
This repository contains the files associated with our CISC499 capstone project, including our model, the datasets we obtained our information from, and any scientific articles we used as references.

Our capstone project aims to use Explainable AI (XAI) to provide insights and reasoning into the optimal route for waste collection in Brooklyn, US. The motivation behind this project is due to the vast amount of waste generated in large cities that go unmanaged. This waste goes unmanaged due to un-optimized collection routes and frequencies. By modelling Brooklyn's waste collection using an evolutionary algorithm (EA), we can obtain the route that minimizes the distance covered and maximizes fuel efficiency.

Using XAI to provide reasoning for our results will help policy-makers understand the logic behind the model we used, which increases the potential for our optimized route to be implemented.

To-Do: Model info

## Datasets
### BinLocations.csv:
Main dataset containing district, subdistrict, street names, latitude and longitude, as well as estimated monthy refuse collected in tons for over 6,500 pickup spots.
Uses information from both DSNY Monthly Tonnage Data and DSNY Litter Basket Inventory datasets.

### MeanRefuseData.csv:
Contains average refuse collected per month for each of the 18 districts in Brooklyn New York in tons, calculated using the DSNY Monthly Tonnage Dataset. Furthermore contains the number of pickup spots in each district found in the DSNY Litter Basket Inventory dataset, and uses this information to calculate the average refuse collected per pickup spot monthly.

### BrooklynSampleData.csv:
Public recycling bins dataset modified to only contain brooklyn locations. Due to its relatively small size compared to BinLocations.csv, it was used mainly to test functionality of distanceGenerator.py and ea.py.

### sample_dist_mat.csv:
Output of distanceGenerator.py given latitudes and longitudes from BrooklynSampleData.csv.

## Original Datasets
- DSNY Monthly Tonnage Data  
  link: https://data.cityofnewyork.us/City-Government/DSNY-Monthly-Tonnage-Data/ebb7-mvp5/about_data
- DSNY Litter Basket Inventory  
  link: https://data.cityofnewyork.us/dataset/DSNY-Litter-Basket-Inventory/8znf-7b2c/about_data
- Automated Traffic Volume Counts  
  link: https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt/about_data
- Public Recycling Bins  
  link: https://data.world/city-of-ny/sxx4-xhzg
