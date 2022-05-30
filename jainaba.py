
import pandas as pd
import geopandas as gpd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def load_in_data(art_coverage_by_country, persons_living_with_HIVAIDS,
                 group_countries, countries):
    """
    This loads data for the certain datasets. Will add more info abot each
    dataset in a bit.The data is not joined it is up to the person working
    on it to join what they need.
    """
    art_coverage_by_country_pd = pd.read_csv(art_coverage_by_country)
    persons_living_with_HIVAIDS_pd = pd.read_excel(persons_living_with_HIVAIDS)
    group_countries_pd = pd.read_csv(group_countries)
    countries_gpd = gpd.read_file(countries)

    return art_coverage_by_country_pd, persons_living_with_HIVAIDS_pd, group_countries_pd, countries_gpd


def merged_data(files):
    """

    """

    # Figure out merge issue
    art_coverage_by_country = files[0]
    persons_living_with_HIVAIDS = files[1]
    group_countries = files[2]
    countries = files[3]

    art_coverage_by_country = art_coverage_by_country.loc[:, art_coverage_by_country.columns != 'WHO Region']
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]

    art_coverage_country_continent = gpd.GeoDataFrame(art_coverage_by_country.merge(countries, left_on='Country',
                                                      right_on='SOVEREIGNT'))
    art_coverage_continent = art_coverage_country_continent.dissolve(by="CONTINENT", aggfunc="sum")
    print(art_coverage_country_continent.columns)
    human_info = gpd.GeoDataFrame(countries.merge(group_countries, left_on='SOVEREIGNT', right_on="Entity"))

    print(human_info.columns)
"""
“How does access to ART (HIV/AIDS treatment) compare across different countries?” 

# if the amount of ART accessibility in North America differs from that in a region such as Africa. 

# different countries and the estimated number of cases of HIV/AIDS that have been reported,the number of people receiving antiretroviral therapy (ART)

# the estimated ART coverage among people living with HIV.

Also looking at current gender, race/ethnicity with HIV/AIDS.   

# This will allow us  to investigate if there is a link between ART access and transmission and mortality rates on different continents.

"""
def contintent_art(files):
    art_coverage_by_country = files[0]
    persons_living_with_HIVAIDS = files[1]
    group_countries = files[2]
    countries = files[3]

    # if the amount of ART accessibility in North America differs from that in a region such as Africa. 
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_coverage_country_continent = gpd.GeoDataFrame(art_coverage_by_country.merge(countries, left_on='Country',
                                                      right_on='SOVEREIGNT'))
    art_coverage_continent = art_coverage_country_continent.dissolve(by="CONTINENT", aggfunc="sum")
    # print(art_coverage_continent.columns)

    recieving_art = art_coverage_country_continent['Reported number of people receiving ART']

    print(art_coverage_country_continent.columns)


    # if the amount of ART accessibility in North America differs from that in a region such as Africa for men vs women

    human_info = gpd.GeoDataFrame(countries.merge(group_countries, left_on='SOVEREIGNT', right_on="Entity"))

    # print(human_info.columns)

    



def main():
    files = load_in_data('/Users/jainabajawara/Downloads/art_coverage_by_country_clean.csv.xls',
                         '/Users/jainabajawara/Downloads/persons-living-with-hiv-aids-2011-2017.csv',
                         '/Users/jainabajawara/Downloads/deaths-and-new-cases-of-hiv.csv',
                         '/Users/jainabajawara/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
    # merged_data(files)
    contintent_art(files)



if __name__ == '__main__':
    main()
