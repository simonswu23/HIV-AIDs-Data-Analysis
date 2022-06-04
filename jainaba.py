
# from unicodedata import category
import pandas as pd
import geopandas as gpd
import numpy as np
<<<<<<< HEAD
# import plotly
# import plotly.graph_objs as go
# import plotly.plotly as py
=======
import plotly
# import plotly.graph_objs as go
# import plotly.plotly as py

>>>>>>> 9d3a644023a8c4e34d01888425b2ca720b9b2ce1

import matplotlib.pyplot as plt
import seaborn as sns

# #DataLore
# Colab

sns.set()


def load_in_data(art_coverage_by_country, persons_living_with_HIVAIDS,
                 group_countries, countries, living):
    """
<<<<<<< HEAD
    These five datasets are what we used for our data on HIV/AIDS.
    art_coverage_by_country_pd gives us the countries and the estimated number
    of cases of HIV/AIDS that have been reported, the number of people
    receiving antiretroviral therapy (ART), and the estimated ART coverage
    among people living with HIV. Also, the min, max, and mean of the estimated
    number of people living with HIV and estimated ART coverage among people
    living with HIV.persons_living_with_HIVAIDS_pd dataset talks about the year
    they got infected with HIV/AIDS. The category column explains the group so
    that the category will say the age at the end of the year, current gender,
    race/ethnicity, transmission category: male adult or adolescent,
    transmission category:female adult or adolescent, and transmission
    category: child (<12 Years Old at the End of Year); the group will answer
    the category type. group_countries_pd dataset talks about the countries,
    deaths, incidence, and prevalence. living_pd dataset explains the countries
    from 2000 to 2020 estimated number of peopleliving with HIV. countries_gpd
    gives us the shape and information of the countires.
=======
    This loads data for the certain datasets. Will add more info abot each
    dataset in a bit.The data is not joined it is up to the person working
    on it to join what they need.
    results:
>>>>>>> 9d3a644023a8c4e34d01888425b2ca720b9b2ce1
    """
    art_coverage_by_country_pd = pd.read_csv(art_coverage_by_country)
    persons_living_with_HIVAIDS_pd = pd.read_excel(persons_living_with_HIVAIDS)
    group_countries_pd = pd.read_csv(group_countries)
    countries_gpd = gpd.read_file(countries)
    living_pd = pd.read_csv(living)


    return art_coverage_by_country_pd, persons_living_with_HIVAIDS_pd, group_countries_pd, countries_gpd, living_pd


def merged_data(files):
    """
    We used merged_data to make sure our data was working and if we could view
    what we merged and whether or not it was correct. It's more of a test
    function.
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
<<<<<<< HEAD


def art_coverage_by_continent(files):
    """
    We wanted to see which continent had the highest ART coverage with this
    graph. First we grouped the countries into continents, and then we found
    out the estimated ART coverage among people living with HIV_median. We created
    a total of all estimated ART coverage among people living with HIV_median
    within the continents. Our results showed us that Africa had the highest
    ART coverage among people living with HIV_median and Europe came in second.
    The Seven seas had the lowest ART coverage among people living with
    HIV_median within the continents.
    """
    art_coverage_by_country = files[0]
    countries = files[3]
    # if the amount of ART accessibility in North America differs from that in a region such as Africa.
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_coverage_country_continent = art_coverage_by_country.merge(countries, left_on='Country',
                                                      right_on='SOVEREIGNT')

    art_coverage_continent = art_coverage_country_continent.groupby("CONTINENT")["Estimated ART coverage among people living with HIV (%)_median"].sum()
    art_coverage_continent.plot(kind = "bar")
    plt.xticks(rotation=25)
    plt.title("Estimated ART coverage among people living with HIV (%)") # the find year 
    plt.ylabel("Estimated Number Of ART coverage among people living with HIV (%)")
    plt.savefig("Estimated ART coverage among people living with HIV", bbox_inches='tight')
    plt.show()


def human_info_overall(files):
    """
    For this graph, we wanted to see which continents overall had the highest
    deaths, incidence, and prevalence of all ages. First, we grouped the
    countries into continents, and then we found the total deaths, incidence,
    and prevalence of all ages. Our chart shows the deaths, incidence, and
    prevalence of all ages in three different colors. Blue is for deaths,
    orange is for incidence, and green is for prevalence. Africa had the
    highest deaths, incidence, and prevalence, and Asia came in second.
    Africa and Asia had a massive difference in deaths, incidence, and
    prevalence. When you look at the chart, you will be able to see that.
    """

    group_countries = files[2]
    countries = files[3]
    countries = countries.loc[:, ['SOVEREIGNT',"CONTINENT"]]
    human_info = (countries.merge(group_countries, left_on='SOVEREIGNT', right_on="Entity"))
    human_information = human_info.loc[:, ["CONTINENT", "Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)",
                                          "Incidence - HIV/AIDS - Sex: Both - Age: All Ages (Number)",
                                          "Prevalence - HIV/AIDS - Sex: Both - Age: All Ages (Number)"]]
    human_info_continent = human_information.groupby("CONTINENT").sum()
  
    human_info_rest= human_info_continent.reset_index()

    human_info_rest.plot(x= "CONTINENT", y=["Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)", "Incidence - HIV/AIDS - Sex: Both - Age: All Ages (Number)", "Prevalence - HIV/AIDS - Sex: Both - Age: All Ages (Number)"], kind="bar")
    plt.title('Overall Deaths, Incidence, and Prevalence in Each Continent')
    plt.xticks(rotation=25)
    plt.ticklabel_format(style='plain', axis='y')
=======


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
>>>>>>> 9d3a644023a8c4e34d01888425b2ca720b9b2ce1
    plt.savefig("Overall Facts in Each Continenet.png")
    plt.show()


def contintent_HIV_AID(files):
<<<<<<< HEAD
    """
    For this graph, we wanted to see which continents have the highest number
    of people living with HIV_median. First, we grouped the countries into
    continents, and then we found the total cases in each continent. Our chart
    showed us that Africa had the highest number of people living with
    HIV_median in the dataset. Africa was really high compared to the other
    continents, and we really can't compare the results due to a big
    difference. The Seven Seas had the lowest number of people living with
    HIV_median.
    """
    art_coverage_by_country = files[0]
    countries = files[3]
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_coverage_continent = art_coverage_by_country.merge(countries, left_on='Country',
                                              right_on='SOVEREIGNT')
    people_living_with_HIV_by_continents = art_coverage_continent.groupby("CONTINENT")["Estimated number of people living with HIV_median"].sum()

    people_living_with_HIV_by_continents.plot(kind = "bar")
    plt.savefig('Estimated number of people living with HIV', bbox_inches='tight')
    plt.xticks(rotation=25)
    plt.title('Estimated number of people living with HIV') # the find year 
    plt.ylabel('Estimated number of people living with HIV')
    plt.show()
=======
    art_coverage_by_country = files[0]
    countries = files[3]
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_coverage_continent = gpd.GeoDataFrame(art_coverage_by_country.merge(countries, left_on='Country',
                                              right_on='SOVEREIGNT'))
    people_living_with_HIV_by_continents = art_coverage_continent.dissolve(by="CONTINENT", aggfunc="sum")
    people_living_with_HIV_by_continents_reset = people_living_with_HIV_by_continents.reset_index()

    print(art_coverage_continent.columns)
    # sns.relplot(data=people_living_with_HIV_by_continents_reset, x="CONTINENT", y="Estimated number of people living with HIV_median", kind="line", hue="CONTINENT")
    # plt.savefig('Estimated number of people living with HIV', bbox_inches='tight')
    # plt.show()
>>>>>>> 9d3a644023a8c4e34d01888425b2ca720b9b2ce1


def slider(files):
    """
    We wanted to create a map of the world to see if HIV/AIDS is similar or
    different in all parts of the world. We also wanted to see if the infection
    rate had increased or decreased from 2000 to 2020. The dataset already had
    it in years, so from 2000, 2005, 2010, 2015, and 2020, it had no data for
    all the years or some of the countries. From the map, we can see that South
    Africa's cases were high in 2000, but from 2005 to 2020, South Africa's
    cases increased. South Africa also had the highest HIV/AIDS infection rates
    for 20 years out of other countries. For India, the colors on the map
    changed each year, and I thought it was increasing, but the fact-value
    numeric increased, so in 2000 the infected was around 3.5M, and in 2005,
    it was still 3.5M, and in 2010 it was 3M and 2015 it was around 2.5M, and
    in 2020 it was around 2.5M. It decreased slowly over the years by 1M, but
    we also need to factor in the value numeric when we look at the years. The
    map is interactive, so if you hover over the country, it will tell you the
    name, year, and cases.
    """
    countries = files[3]
    estimated_number_of_people_living = files[4]

    estimated_num_people_living = estimated_number_of_people_living .loc[:, [ 'Location', 'Period','FactValueNumeric']]

    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]

    estimated_num_people_living_by_country = gpd.GeoDataFrame(estimated_num_people_living.merge(countries, left_on='Location',
                                              right_on='SOVEREIGNT'))


    year = 2000

    # your color-scale
    scl = [[0.0, '#ffffff'],[0.2, '#b4a8ce'],[0.4, '#8573a9'],
        [0.6, '#7159a3'],[0.8, '#5732a1'],[1.0, '#2c0579']] # purples

    data_slider = []
    for year in estimated_num_people_living_by_country['Period'].unique():
<<<<<<< HEAD
        df_segmented = estimated_num_people_living_by_country[(['Period']== year)]

        for col in df_segmented.columns:
            df_segmented[col] = df_segmented[col].astype(str)

        data_each_yr = dict(
                            type='choropleth',
                            locations = df_segmented['SOVEREIGNT'],
                            z=df_segmented['FactValueNumeric'].astype(float),
                            # locationmode='USA-states',
                            colorscale = scl,
                            colorbar= {'title':'# Living People'})

        data_slider.append(data_each_yr)

    steps = []
    for i in range(len(data_slider)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data_slider)],
                    label='Year {}'.format(i + 2000))
        step['args'][1][i] = True
        steps.append(step)

=======
        df_segmented =  estimated_num_people_living_by_country[(['Period']== year)]

        for col in df_segmented.columns:
            df_segmented[col] = df_segmented[col].astype(str)

        data_each_yr = dict(
                            type='choropleth',
                            locations = df_segmented['SOVEREIGNT'],
                            z=df_segmented['FactValueNumeric'].astype(float),
                            # locationmode='USA-states',
                            colorscale = scl,
                            colorbar= {'title':'# Living People'})

        data_slider.append(data_each_yr)

    steps = []
    for i in range(len(data_slider)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(data_slider)],
                    label='Year {}'.format(i + 2000))
        step['args'][1][i] = True
        steps.append(step)

>>>>>>> 9d3a644023a8c4e34d01888425b2ca720b9b2ce1
    sliders = [dict(active=0, pad={"t": 1}, steps=steps)]

    layout = dict(title ='# of People Living with HIV-AIDS',
                sliders=sliders)

    fig = dict(data=data_slider, layout=layout)
    periscope.plotly(fig)

def main():
    files = load_in_data('/Users/jainabajawara/Downloads/art_coverage_by_country_clean.csv.xls',
                         '/Users/jainabajawara/Downloads/persons-living-with-hiv-aids-2011-2017.csv',
                         '/Users/jainabajawara/Downloads/deaths-and-new-cases-of-hiv.csv',
                         '/Users/jainabajawara/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp',
                         '/Users/jainabajawara/Downloads/data.csv')
<<<<<<< HEAD
    # merged_data(files)
    # art_coverage_by_continent(files)
    # human_info_overall(files)
    # contintent_HIV_AID(files)
    slider(files)
=======

    # merged_data(files)
    # art_coverage_by_continent(files)
    # contintent_HIV_AID(files)
    # human_info_overall(files)
    # slider(files)
>>>>>>> 9d3a644023a8c4e34d01888425b2ca720b9b2ce1


if __name__ == '__main__':
    main()
