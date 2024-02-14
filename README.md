# CISC-499-XAI-For-Waste-Management-Using-EA
This repository contains the files associated with our CISC499 capstone project, including our model, the datasets we obtained our information from, and any scientific articles we used as references.

Our capstone project aims to use Explainable AI (XAI) to provide insights and reasoning into the optimal route for waste collection in Brooklyn, US. The motivation behind this project is due to the vast amount of waste generated in large cities that go unmanaged. This waste goes unmanaged due to un-optimized collection routes and frequencies. By modelling Brooklyn's waste collection using an evolutionary algorithm (EA), we can obtain the route that minimizes the distance covered and maximizes fuel efficiency.

Using XAI to provide reasoning for our results will help policy-makers understand the logic behind the model we used, which increases the potential for our optimized route to be implemented.

## Model

Individuals of the population are a location of a trash bin, b<sub>i</sub>, and a permutation of the locations of every trash bin and their distance from b<sub>i</sub>.
For example, if we had a population size of 5 (5 trash bins), one such individual could be [(b<sub>1</sub>, [dists<sub>1</sub>]), (b<sub>2</sub>, [dists<sub>2</sub>]), (b<sub>3</sub> , [dists<sub>3</sub>]), (b<sub>4</sub>, [dists<sub>4</sub>]), (b<sub>5</sub>, [dists<sub>5</sub>])], where each b<sub>i</sub> corresponds to the location of a trash bin and each array dists<sub>i</sub> is an array of tuples of the locations of every trash bin and their distance from b<sub>i</sub>. As an example, for the individual (b<sub>1</sub>, [dists<sub>1</sub>]), b<sub>1</sub> is the location of a trash bin and:
dists<sub>1</sub> = [(b<sub>1</sub>, 0), (b<sub>2</sub>, p), (b<sub>3</sub>, q), (b<sub>4</sub>, r), (b<sub>5</sub>, s)], where
- b<sub>1</sub> and b<sub>2</sub> are p km apart
- b<sub>1</sub> and b<sub>3</sub> are q km apart
- b<sub>1</sub> and b<sub>4</sub> are r km apart
- b<sub>1</sub> and b<sub>5</sub> are s km apart

To calculate the fitness of each individual, we first calculate the penalty of the individual as the total cost. An individual’s penalty is the sum of the distances between each successive trash bin in its permutation as well as some arbitrary value based on the traffic congestion of the roads between the successive bins (see datasets section for information on the traffic congestion dataset used). This method favours individuals whose permutations include bins that are closer to one another and use roads that are less congested. Collection routes which use less congested roads minimize the time that collection vehicles are idling in traffic, which in turn minimizes the total collection time. Therefore, every individual will, at this point, have a negative value for their penalty.
We then find the individual with the highest penalty and add this value to the penalty of every individual in the population. This will result in the worst individual having a fitness of 0 and every other individual having some value higher than this. Thus, the best individuals will have the highest fitness values.

At the time of writing, our EA uses hardcoded examples for testing. With data pre-processing now completed, we will implement the remaining functions required in our EA and test it using the data extracted from the datasets.
Functions currently implemented are subject to change.

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

## Articles Referenced
- An innovative medical waste management system in a smart city using XAI and vehicle routing optimization (doi: 10.12688/f1000research.138867.2).
This article uses XAI techniques and vehicle route optimization for a medical waste management system. It was referenced in order to gain an understanding of how XAI techniques have been implemented in similar problems.
