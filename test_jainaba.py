"""
This file contains testing code for the
jainaba.py file
"""

import jainaba as multidata


def sample(files):
    art_coverage_country = files[0]
    living_2010_2017 = files[1]
    group_countries = files[2]
    countries = files[3]
    estimated_number_of_people_living = files[4]

    art_coverage_country = art_coverage_country.sample(n=10, replace=True)
    living_2010_2017 = living_2010_2017.sample(n=10, replace=True)
    group_countries = group_countries.sample(n=10, replace=True)
    countries = countries.sample(n=10, replace=True)
    living = estimated_number_of_people_living.sample(n=10, replace=True)

    return (art_coverage_country, living_2010_2017,
            group_countries, countries, living)


def test_art_coverage_by_continent(sampled_version):
    """
    Tests the gender method
    with the test dataset,
    prints out data values and
    saves test picture to 'gender test.png'
    """
    multidata.art_coverage_by_continent(sampled_version)
    plt.savefig('Estimated ART coverage among people living with HIV test',
                bbox_inches='tight')


def test_human_info_overall(sampled_version):

    multidata.human_info_overall(sampled_version)


def test_contintent_HIV_AID(sampled_version):
    """
    Tests the race method
    with the test dataset,
    prints out data values and
    saves test picture to 'race test.png'
    """
    multidata.contintent_HIV_AID(sampled_version, show_data=True,
                                 png_name='Estimated number of people living with HIV test')


def test_slider(sampled_version):
    """
    Tests the m_transmission method
    with the test dataset,
    prints out data values and
    saves test picture to 'mt test.png'
    """
    multidata.contintent_HIV_AID(sampled_version, show_data=True,
                                 png_name='slider test')


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

    files = multidata.load_in_data(art_coverage_by_country, living_hiv_aids_2011_2017,
                                   deaths_and_new_cases_of_hiv, countries, data)
    sampled_version = sample(files)
    test_art_coverage_by_continent(sampled_version)
    test_human_info_overall(sampled_version)
    test_contintent_HIV_AID(sampled_version)
    test_slider(sampled_version)


if __name__ == '__main__':
    main()
