
# INFO 7374 - Data Analysis Using Python - Final Project

## Domestic flight data analysis 

### The analysis done is to assess the performance of various carriers based on the delay, passengers travelled and net income. The analysis has been done for the date range of September 2016 and December 2016. Weather data and financial data has been correlated to infer the impact on the Carrier performance.

## Data Collection:

### Download dataset for flight performance, revenue and passenger count

Data has been gathered in .csv format from transtats.bts.gov for the below records:

Step 1: The data of the flights operated everyday within the country was downloaded month wise for the period of Sep-2016 and Dec-2016 and saved in the Flight data folder.

Step 2: Number of passengers travelled on each carrier from Jan 2016 to Dec 2016.

Step 3: Net Income of carriers on each quarter

Step 4: Daily Weather data of Boston from Jan 2016 to Dec 2016


## Data Processing 

### 1: Number of flights having delay in Arrival  based on City

Step 1: Append the total number of flights from September 01, 2016 to December 31, 2016

Step 2: Merge the entire data into a DataFrame

Step 3: Create a dataframe with destination city, carrier delay, weather delay, nas delay, late aircraft delay and security delay columns.

Step 4: Replace the Delay column values as blank for those having '0' value.

Step 5: Group the destination cities with the count of delays.

Step 6: Sort the values based on carrier delay value and export it to a csv file

### 2: Revenue correlation with total distance covered

Step 1: Append the total number of flights from September 01, 2016 to December 31, 2016

Step 2: Merge the entire data into a DataFrame 

Step 3: Group Airline ID, origin city and destination city and take a sum of distance covered.

Step 4: From Finance data, get the net income for each carrier in third quarter.

Step 5: Calculate the distance covered and net income for each carrier

### 3: Count of flights take off on hourly basis for each day of the week 

Step 1: Append the total number of flights from September 01, 2016 to December 31, 2016

Step 2: Merge the entire data into a DataFrame 

Step 3: Take the hour value alone from the Departure time column value.

Step 4: Convert numeric value of day into name of day.

Step 5: For each City, take the count of flight for each hour and day of the week

### 4: Revenue correlation with count of passengers

Step 1: From passenger data, get the total number of passengers for each carrier

Step 2: From Finance data, get the net income for each carrier

Step 3: Calculate the profit/loss based on passenger count

### 5: Correlation between weather delay and weather data

Step 1: The daily flight data was taken for January 2016

Step 2: The number of flights originating from Boston is filtered

Step 3: The weather data for the month of January was filtered from Weather data

Step 4: The correlation between weather delay and data


## Data Analysis

### 1.  Number of flights having delay in Arrival  based on City

The below plot gives the hourly count for each day based on city


### 2. Revenue correlation with total distance covered



