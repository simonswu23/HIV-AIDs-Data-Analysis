# HIV-AIDs-Data-Analysis
We wanted to look at HIV/AIDS and see if anything has changed over the years for our project. HIV/AIDS has been around for years, and we wanted to see which countries have the highest infection rate, ART treatment, demographic categories around the United States, and how it looked over the years. From the datasets, we found we were able to create charts from our data and a map with a slider to see how the countries looked over the years.

[add instructions]

[standardize formatting]

## For the 2011-2017 US HIV/AIDs Data:
- dataset used should be labelled as 'persons-living-with-hiv-aids-2011-2017.csv' in directory
- run the main file to filter and plot data visualizations
- graphs are saved as png files to the directory
- no new libraries needed for this module

## From the Number of people living with HIV AIDS and ART (Anti Retro-viral Therapy) coverage among people living with HIV estimates Data:
- ***Dataset:***
For our data we used five different datasets. art_coverage_by_country_pd gives us the countries and the
estimated number of cases of HIV/AIDS that have been reported, the number of people
receiving antiretroviral therapy (ART), and the estimated ART coverage
among people living with HIV. Also, the min, max, and mean of the estimated
number of people living with HIV and estimated ART coverage among people
living with HIV. persons_living_with_HIVAIDS_pd dataset talks about the year
they got infected with HIV/AIDS. The category column explains the group so
that the category will say the age at the end of the year, current gender,
race/ethnicity, transmission category: male adult or adolescent,
transmission category:female adult or adolescent, and transmission
category: child (<12 Years Old at the End of Year); the group will answer
the category type. group_countries_pd dataset talks about the countries,
deaths, incidence, and prevalence. living_pd dataset explains the countries
from 2000 to 2020 estimated number of people living with HIV. countries_gpd
gives us the shape and information of the countries.

- ***Library:***
We used ploty express

- ***What the files does:***
With our file we used merged someone of the column together. With the art_coverage_by_continent file
we grouped the countries into continents, and then we found out the estimated ART coverage among people living with HIV_median. We created a total of all estimated ART coverage among people living with HIV_median within the continents. For the human_info_overall file we grouped the countries into continents, and then we found the total deaths, incidence, and prevalence of all ages in each continent. Then we total of each continent based on the data that was provided. For the contintent_HIV_AID file we grouped the countries into continents, and then we found the total HIV_median in each continent. Then we total HIV_median in each continent based on the data that was provided. For our slider file we created a map based on the data that was provided since the total cases were already added up based on the year in the country.   
