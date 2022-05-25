
import pandas as pd
# import geopandas as gpd


def load_in_data(art_coverage_by_country, persons_living_with_HIVAIDS,
                 group_countries, countries):
    """
    This loads data for the certain datasets. While add more info abot each
    dataset in a bit.The data is not joined it is up to the person working
    on it to join what they need.
    """
    art_coverage_by_country_pd = pd.read_csv(art_coverage_by_country)
    persons_living_with_HIVAIDS_pd = pd.read_excel(persons_living_with_HIVAIDS)
    group_countries = pd.read_csv(group_countries)
    # this does not work.
    # countries = pd.read_excel(countries)
    # print(countries)


def main():
    files = load_in_data('/Users/jainabajawara/Downloads/art_coverage_by_country\
        _clean.csv.xls',
                         '/Users/jainabajawara/Downloads/persons-living-with-hiv-aids\
                             -2011-2017.csv',
                         '/Users/jainabajawara/Downloads/deaths-and-new-cases-of\
                         -hiv.csv',
                         '/Users/jainabajawara/Downloads/countries_with_long&l\
                             at.xlxs')


if __name__ == '__main__':
    main()
