
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # for chart

sns.set()


def load_in_data(art_coverage_by_country, persons_living_with_HIVAIDS,
                 group_countries, countries, living):
    """
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

    """
    art_coverage_by_country_pd = pd.read_csv(art_coverage_by_country)
    persons_living_with_HIVAIDS_pd = pd.read_excel(persons_living_with_HIVAIDS)
    group_countries_pd = pd.read_csv(group_countries)
    countries_gpd = gpd.read_file(countries)
    living_pd = pd.read_csv(living)

    return (art_coverage_by_country_pd, persons_living_with_HIVAIDS_pd,
            group_countries_pd, countries_gpd, living_pd)


def merged_data(files):
    """
    We used merged_data to make sure our data was working and if we could view
    what we merged and whether or not it was correct. It's more of a test
    function.
    """
    # Figure out merge issue
    art_coverage_country = files[0]
    group_countries = files[2]
    countries = files[3]

    not_who_region = art_coverage_country[art_coverage_country.columns !=
                                          'WHO Region']
    art_coverage_country = art_coverage_country.loc[:, not_who_region]
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_coverage = art_coverage_country.merge(countries, left_on='Country',
                                              right_on='SOVEREIGNT')
    print(art_coverage.columns)
    human_info = countries.merge(group_countries, left_on='SOVEREIGNT',
                                 right_on="Entity")
    print(human_info.columns)


def art_coverage_by_continent(files):
    """
    We wanted to see which continent had the highest ART coverage with this
    graph. First we grouped the countries into continents, and then we found
    out the estimated ART coverage among people living with HIV_median.
    We created a total of all estimated ART coverage among people living
    with HIV_median within the continents. Our results showed us that Africa
    had the highest ART coverage among people living with HIV_median and
    Europe came in second.The Seven seas had the lowest ART coverage
    among people living with HIV_median within the continents.
    """
    art_coverage_by_country = files[0]
    countries = files[3]
    countries = countries.loc[:, ['SOVEREIGNT', 'geometry', 'CONTINENT']]
    art_country = art_coverage_by_country.merge(countries, left_on='Country',
                                                right_on='SOVEREIGNT')

    art_coverage_continent = art_country.groupby("CONTINENT")
    ["Estimated ART coverage among people living with HIV (%)_median"].sum()
    art_coverage_continent.plot(kind="bar")
    plt.xticks(rotation=25)
    plt.title("Estimated ART coverage among people living with HIV (%)")
    plt.ylabel("Estimated Number Of ART coverage"
               "among people living with HIV (%)")
    plt.savefig("Estimated ART coverage among"
                "people living with HIV", bbox_inches='tight')
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
    countries = countries.loc[:, ['SOVEREIGNT', "CONTINENT"]]
    info = (countries.merge(group_countries, left_on='SOVEREIGNT',
                            right_on="Entity"))
    info = info.rename(columns={"Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)":
                                'Deaths',
                                "Incidence - HIV/AIDS - Sex: Both - Age: All Ages (Number)":
                                "Incidence",
                                "Prevalence - HIV/AIDS - Sex: Both - Age: All Ages (Number)":
                                'Prevalence'})
    print(info.columns)
    human_information = info.loc[:, ["CONTINENT",
                                     "Deaths",
                                     "Incidence",
                                     "Prevalence"]]
    print(human_information.columns)
    human_info_continent = human_information.groupby("CONTINENT").sum()
    human_info_rest = human_info_continent.reset_index()
    human_info_rest.plot(x="CONTINENT", y=["Deaths",
                                           "Incidence",
                                           "Prevalence"],
                         kind="bar")
    plt.title('Overall Deaths, Incidence, and Prevalence in Each Continent')
    plt.xticks(rotation=25)
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig("Overall Facts in Each Continenet.png")
    plt.show()


def contintent_HIV_AID(files):
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
    art_continent = art_coverage_by_country.merge(countries,
                                                  left_on='Country',
                                                  right_on='SOVEREIGNT')
    HIV_continents = art_continent.groupby("CONTINENT")["Estimated number of people living with HIV_median"].sum()

    HIV_continents.plot(kind="bar")
    plt.savefig('Estimated number of people living with HIV',
                bbox_inches='tight')
    plt.xticks(rotation=25)
    plt.title('Estimated number of people living with HIV')  # the find year
    plt.ylabel('Estimated number of people living with HIV')
    plt.show()


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
    estimated_number_of_people_living = files[4]

    estim_num_living = estimated_number_of_people_living .loc[:, ['Location',
                                                                  'Period',
                                                                  'FactVal'
                                                                  'ueNumeric']]
    print(estim_num_living.columns)
    gapminder = px.data.gapminder()
    print(gapminder.columns)

    silderinfo = gapminder.merge(estim_num_living,
                                 left_on='country',
                                 right_on='Location')

    fig = px.choropleth(silderinfo, locations='iso_alpha',
                        color='FactValueNumeric', hover_name='country',
                        animation_frame='Period',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        projection='natural earth')
    plt.savefig('Slider.png', bbox_inches='tight')
    fig.show()


def main():
    art_coverage_by_country = ('/Users/jainabajawara/Downloads/'
                               'art_coverage_by_country_clean.csv.xls')
    living_hiv_aids_2011_2017 = ('/Users/jainabajawara/Downloads/'
                                 'persons-living-with-hiv-aids-2011-2017.csv')
    deaths_and_new_cases_of_hiv = ('/Users/jainabajawara/Downloads/'
                                   'deaths-and-new-cases-of-hiv.csv')
    countries = ('/Users/jainabajawara/Downloads/'
                 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
    data = '/Users/jainabajawara/Downloads/data.csv'

    files = load_in_data(art_coverage_by_country, living_hiv_aids_2011_2017,
                         deaths_and_new_cases_of_hiv, countries, data)
    # merged_data(files)
    # art_coverage_by_continent(files)
    # human_info_overall(files)
    # contintent_HIV_AID(files)
    slider(files)


if __name__ == '__main__':
    main()
