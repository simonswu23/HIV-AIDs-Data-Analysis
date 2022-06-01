
# from unicodedata import category
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
    results:
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


def art_coverage_by_continent(files):
    art_coverage_by_country = files[0]
    countries = files[3]
    # if the amount of ART accessibility in North America differs from that in a region such as Africa.
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_coverage_country_continent = gpd.GeoDataFrame(art_coverage_by_country.merge(countries, left_on='Country',
                                                      right_on='SOVEREIGNT'))
    art_coverage_continent = art_coverage_country_continent.dissolve(by="CONTINENT", aggfunc="sum")

    art_reset = art_coverage_continent.reset_index()
    sns.relplot(data=art_reset, x="CONTINENT", y="Estimated ART coverage among people living with HIV (%)_median", kind="line", hue="CONTINENT")
    plt.savefig("Estimated ART coverage among people living with HIV (%)", bbox_inches='tight')
    plt.show()


def human_info_overall(files):
    group_countries = files[2]
    countries = files[3]
    human_info = gpd.GeoDataFrame(countries.merge(group_countries, left_on='SOVEREIGNT', right_on="Entity"))
    human_info_continent = human_info.dissolve(by="CONTINENT", aggfunc="sum")
    human_info_continent_reset = human_info_continent.reset_index()

    print(human_info_continent_reset.columns)

    fig, [[ax1], [ax2], [ax3]] = plt.subplots(1, 1, 1, figsize=(20, 10))
    human_info_continent.plot(ax=ax1, column="Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)", legend=True, vmin=0,
                              vmax=1)
    human_info_continent.plot(ax=ax2, column="Incidence - HIV/AIDS - Sex: Both - Age: All Ages (Number)", legend=True, vmin=0,
                              vmax=1)
    human_info_continent.plot(ax=ax3, column="Prevalence - HIV/AIDS - Sex: Both - Age: All Ages (Number)", legend=True, vmin=0,
                              vmax=1)
    ax1.set_title('Overall Deaths in Each Continent')
    ax2.set_title('Overall Incidence in Each Continent')
    ax3.set_title('Overall Prevalence in Each Continent')
    plt.savefig("Overall Facts in Each Continenet.png")
    plt.show()


def contintent_HIV_AID(files):
    art_coverage_by_country = files[0]
    countries = files[3]
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_coverage_continent = gpd.GeoDataFrame(art_coverage_by_country.merge(countries, left_on='Country',
                                              right_on='SOVEREIGNT'))
    people_living_with_HIV_by_continents = art_coverage_continent.dissolve(by="CONTINENT", aggfunc="sum")
    people_living_with_HIV_by_continents_reset = people_living_with_HIV_by_continents.reset_index()
    sns.relplot(data=people_living_with_HIV_by_continents_reset, x="CONTINENT", y="Estimated number of people living with HIV_median", kind="line", hue="CONTINENT")
    plt.savefig('Estimated number of people living with HIV', bbox_inches='tight')
    plt.show()


def main():
    files = load_in_data('/Users/jainabajawara/Downloads/art_coverage_by_country_clean.csv.xls',
                         '/Users/jainabajawara/Downloads/persons-living-with-hiv-aids-2011-2017.csv',
                         '/Users/jainabajawara/Downloads/deaths-and-new-cases-of-hiv.csv',
                         '/Users/jainabajawara/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
    # merged_data(files)
    # art_coverage_by_continent(files)
    # contintent_HIV_AID(files)
    human_info_overall(files)


if __name__ == '__main__':
    main()
