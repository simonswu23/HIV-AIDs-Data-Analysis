"""
This file processes a data file of people
living with HIV and AIDS from 2011 to 2017
in the US and creates different data visualizations of
breakdowns between different affected demographics.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def gender(hiv_data):
    """
    Takes in the processed hiv/aids dataset
    and plots a line graph of the percent representation
    of different genders living with HIV/AIDS from 2011 to
    2017. Saves that graph as 'line_plot_gender.png'
    """
    g_counts = hiv_data[hiv_data['Category'] == 'Current Gender']
    g_counts = g_counts.groupby('Year')['Count'].sum().reset_index()

    t_men = hiv_data[hiv_data['Group'] == 'Transgender men'].reset_index()
    t_men_perc = t_men['Count'] / g_counts['Count']
    t_men['Percentage'] = t_men_perc * 100

    t_women = hiv_data[hiv_data['Group'] == 'Transgender women'].reset_index()
    t_women_perc = t_women['Count'] / g_counts['Count']
    t_women['Percentage'] = t_women_perc * 100

    c_men = hiv_data[hiv_data['Group'] == 'Cisgender men'].reset_index()
    c_men_perc = c_men['Count'] / g_counts['Count']
    c_men['Percentage'] = c_men_perc * 100

    c_women = hiv_data[hiv_data['Group'] == 'Cisgender women'].reset_index()
    c_women_perc = c_women['Count'] / g_counts['Count']
    c_women['Percentage'] = c_women_perc * 100

    nb = hiv_data[hiv_data['Group'] == 'Alternative Gender'].reset_index()
    nb_perc = nb['Count'] / g_counts['Count']
    nb['Percentage'] = nb_perc * 100

    fig, ax1 = plt.subplots()
    sns.lineplot(data=c_men, x='Year', y='Percentage',
                 label='Cis Men', ax=ax1)
    sns.lineplot(data=c_women, x='Year', y='Percentage',
                 label='Cis Women', ax=ax1)
    sns.lineplot(data=t_men, x='Year', y='Percentage',
                 label='Trans Men', ax=ax1, alpha=0.7)
    sns.lineplot(data=t_women, x='Year', y='Percentage',
                 label='Trans Women', ax=ax1)
    sns.lineplot(data=nb, x='Year', y='Percentage',
                 label='Alternative Gender', ax=ax1, linestyle="dashed")
    plt.xlabel('Year')
    plt.ylabel('Percentage Gender')
    plt.title("Gender Breakdown of People Living with HIV over Time")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.savefig('line_plot_gender.png', bbox_inches='tight')


def race(hiv_data):
    """
    Takes in the processed hiv/aids dataset
    and plots a line graph of the percent representation
    of different races living with HIV/AIDS from 2011 to
    2017. Saves that graph as 'line_plot_race.png'
    """

    r_counts = hiv_data[hiv_data['Category'] == 'Race/Ethnicity']
    r_counts = r_counts.groupby('Year')['Count'].sum().reset_index()

    ai_an = hiv_data[hiv_data['Group'] ==
                     'American Indian/Alaska Native'].reset_index()
    ai_an_perc = ai_an['Count'] / r_counts['Count']
    ai_an['Percentage'] = ai_an_perc * 100

    asian = hiv_data[hiv_data['Group'] == 'Asian*'].reset_index()
    as_perc = asian['Count'] / r_counts['Count']
    asian['Percentage'] = as_perc * 100

    black = hiv_data[hiv_data['Group']
                     == 'Black/African American'].reset_index()
    black_perc = black['Count'] / r_counts['Count']
    black['Percentage'] = black_perc * 100

    latine = hiv_data[hiv_data['Group'] == 'Latinx*'].reset_index()
    latine_perc = latine['Count'] / r_counts['Count']
    latine['Percentage'] = latine_perc * 100

    nh_pi = hiv_data[hiv_data['Group'] ==
                     'Native Hawaiian/Pacific Islander'].reset_index()
    nh_pi_perc = nh_pi['Count'] / r_counts['Count']
    nh_pi['Percentage'] = nh_pi_perc * 100

    white = hiv_data[hiv_data['Group'] == 'White'].reset_index()
    white_perc = white['Count'] / r_counts['Count']
    white['Percentage'] = white_perc * 100

    multi_r = hiv_data[hiv_data['Group'] == 'Multiple races'].reset_index()
    multi_r_perc = multi_r['Count'] / r_counts['Count']
    multi_r['Percentage'] = multi_r_perc * 100

    unknown = hiv_data[hiv_data['Group'] == 'Unknown race'].reset_index()
    unknown_perc = unknown['Count'] / r_counts['Count']
    unknown['Percentage'] = unknown_perc * 100

    fig, ax2 = plt.subplots()
    sns.lineplot(data=ai_an, x='Year', y='Percentage',
                 label='American Indian/Alaskan Native',
                 ax=ax2, linestyle="dashed")
    sns.lineplot(data=asian, x='Year', y='Percentage', label='Asian', ax=ax2)
    sns.lineplot(data=black, x='Year', y='Percentage', label='Black', ax=ax2)
    sns.lineplot(data=latine, x='Year', y='Percentage', label='Latinx', ax=ax2)
    sns.lineplot(data=nh_pi, x='Year', y='Percentage',
                 label='Native Hawaiian/Pacific Islander', ax=ax2)
    sns.lineplot(data=white, x='Year', y='Percentage', label='White', ax=ax2)
    sns.lineplot(data=multi_r, x='Year', y='Percentage',
                 label='Multiracial', ax=ax2)
    sns.lineplot(data=unknown, x='Year', y='Percentage',
                 label='Unknown', ax=ax2, linestyle="dotted")
    plt.xlabel('Year')
    plt.ylabel('Percentage Race')
    plt.title("Race Breakdown of People Living with HIV over Time")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.savefig('line_plot_race.png', bbox_inches='tight')


def m_transmission(hiv_data):
    """
    Takes in the processed hiv/aids dataset and plots
    a line graph of the percent representation of HIV/AIDS
    transmissions for adult and adolescent males from 2011 to 2017.
    Saves that graph as 'line_plot_gender.png'
    """

    transmission = hiv_data[hiv_data['Category'] ==
                            'Transmission Category: Male Adult or Adolescent']
    transmission = transmission.groupby('Year')['Count'].sum().reset_index()

    mmsc = hiv_data[hiv_data['Group'] ==
                    'Male-to-male sexual contact (MMSC)'].reset_index()
    mmsc_perc = mmsc['Count'] / transmission['Count']
    mmsc['Percentage'] = mmsc_perc * 100

    idu = hiv_data[hiv_data['Group'] ==
                   'Injection drug use (IDU)'].reset_index()
    idu_perc = idu['Count'] / transmission['Count']
    idu['Percentage'] = idu_perc * 100

    mmsc_idu = hiv_data[hiv_data['Group'] == 'MMSC and IDU'].reset_index()
    mmsc_idu_perc = mmsc_idu['Count'] / transmission['Count']
    mmsc_idu['Percentage'] = mmsc_idu_perc * 100

    hrh = hiv_data[hiv_data['Group'] ==
                   'High-risk heterosexual contact (HRH)**'].reset_index()
    hrh_perc = hrh['Count'] / transmission['Count']
    hrh['Percentage'] = hrh_perc * 100

    het = hiv_data[hiv_data['Group'] ==
                   'Heterosexual contact (Non-HRH)***'].reset_index()
    het_perc = het['Count'] / transmission['Count']
    het['Percentage'] = het_perc * 100

    perinatal = hiv_data[hiv_data['Group'] == 'Perinatal'].reset_index()
    perinatal_perc = perinatal['Count'] / transmission['Count']
    perinatal['Percentage'] = perinatal_perc * 100

    unknown_risk = hiv_data[hiv_data['Group'] ==
                            'Unknown risk'].reset_index()
    unknown_risk_perc = unknown_risk['Count'] / transmission['Count']
    unknown_risk['Percentage'] = unknown_risk_perc * 100

    other = hiv_data[hiv_data['Group'] == 'Other****'].reset_index()
    other_perc = other['Count'] / transmission['Count']
    other['Percentage'] = other_perc * 100

    fig, ax3 = plt.subplots()
    sns.lineplot(data=mmsc, x='Year', y='Percentage',
                 label='Male-Male Sexual Contact (MMSC)', ax=ax3)
    sns.lineplot(data=idu, x='Year', y='Percentage',
                 label='Injection Drug Use (IDU)', ax=ax3)
    sns.lineplot(data=mmsc_idu, x='Year', y='Percentage',
                 label='MMSC and IDU', ax=ax3)
    sns.lineplot(data=hrh, x='Year', y='Percentage',
                 label='High-Risk Heterosexual Contact', ax=ax3)
    sns.lineplot(data=het, x='Year', y='Percentage',
                 label='Heterosexual Contact (non high-risk)', ax=ax3)
    sns.lineplot(data=perinatal, x='Year', y='Percentage',
                 label='Perinatal', ax=ax3)
    sns.lineplot(data=unknown_risk, x='Year', y='Percentage',
                 label='Unknown Risk', ax=ax3)
    sns.lineplot(data=other, x='Year', y='Percentage',
                 label='Other', ax=ax3)
    plt.xlabel('Year')
    plt.ylabel('Percentage Transmission')
    plt.title("Male Adult and Adolescent HIV Transmission over Time")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.savefig('line_plot_transmission_m.png', bbox_inches='tight')


def f_transmission(hiv_data):
    """
    Takes in the processed hiv/aids dataset and plots
    a line graph of the percent representation of HIV/AIDS
    transmissions for adult and adolescent females from 2011 to 2017.
    Saves that graph as 'line_plot_gender.png'
    """

    tc_fm = 'Transmission Category: Female Adult or Adolescent'
    transmission = hiv_data[hiv_data['Category'] == tc_fm]
    transmission = transmission.groupby('Year')['Count'].sum().reset_index()

    idu = hiv_data[hiv_data['Group'] ==
                   'Injection drug use (IDU)'].reset_index()
    idu_perc = idu['Count'] / transmission['Count']
    idu['Percentage'] = idu_perc * 100

    hrh = hiv_data[hiv_data['Group'] ==
                   'High-risk heterosexual contact (HRH)**'].reset_index()
    hrh_perc = hrh['Count'] / transmission['Count']
    hrh['Percentage'] = hrh_perc * 100

    het = hiv_data[hiv_data['Group'] ==
                   'Heterosexual contact (Non-HRH)***'].reset_index()
    het_perc = het['Count'] / transmission['Count']
    het['Percentage'] = het_perc * 100

    perinatal = hiv_data[hiv_data['Group'] == 'Perinatal'].reset_index()
    perinatal_perc = perinatal['Count'] / transmission['Count']
    perinatal['Percentage'] = perinatal_perc * 100

    unknown_risk = hiv_data[hiv_data['Group'] ==
                            'Unknown risk'].reset_index()
    unknown_risk_perc = unknown_risk['Count'] / transmission['Count']
    unknown_risk['Percentage'] = unknown_risk_perc * 100

    other = hiv_data[hiv_data['Group'] == 'Other****'].reset_index()
    other_perc = other['Count'] / transmission['Count']
    other['Percentage'] = other_perc * 100

    fig, ax3 = plt.subplots()
    sns.lineplot(data=idu, x='Year', y='Percentage',
                 label='Injection Drug Use (IDU)', ax=ax3)
    sns.lineplot(data=hrh, x='Year', y='Percentage',
                 label='High-Risk Heterosexual Contact', ax=ax3)
    sns.lineplot(data=het, x='Year', y='Percentage',
                 label='Heterosexual Contact (non high-risk)', ax=ax3)
    sns.lineplot(data=perinatal, x='Year', y='Percentage',
                 label='Perinatal', ax=ax3)
    sns.lineplot(data=unknown_risk, x='Year', y='Percentage',
                 label='Unknown Risk', ax=ax3)
    sns.lineplot(data=other, x='Year', y='Percentage',
                 label='Other', ax=ax3)
    plt.xlabel('Year')
    plt.ylabel('Percentage Transmission')
    plt.title("Female Adult and Adolescent HIV Transmission over Time")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.savefig('line_plot_transmission_f.png', bbox_inches='tight')


def main():
    hiv_data = pd.read_csv('persons-living-with-hiv-aids-2011-2017.csv')
    gender(hiv_data)
    race(hiv_data)
    m_transmission(hiv_data)
    f_transmission(hiv_data)


if __name__ == '__main__':
    main()