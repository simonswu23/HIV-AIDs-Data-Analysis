import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    hiv_data = pd.read_csv('C:\\Users\\simon\\Downloads\\persons-living-with-hiv-aids-2011-2017.csv')

    # By Gender
    g_counts = hiv_data[hiv_data['Category'] == 'Current Gender']
    g_counts = g_counts.groupby('Year')['Count'].sum().reset_index()
    #print(g_counts)

    t_men = hiv_data[hiv_data['Group'] == 'Transgender men'].reset_index()
    t_men_perc = t_men['Count'] / g_counts['Count']
    t_men['Percentage'] = t_men_perc * 100
    #print(t_men)

    t_women = hiv_data[hiv_data['Group'] == 'Transgender women'].reset_index()
    t_women_perc = t_women['Count'] / g_counts['Count']
    t_women['Percentage'] = t_women_perc * 100
    #print(t_women)

    c_men = hiv_data[hiv_data['Group'] == 'Cisgender men'].reset_index()
    c_men_perc = c_men['Count'] / g_counts['Count']
    c_men['Percentage'] = c_men_perc * 100
    #print(c_men)

    c_women = hiv_data[hiv_data['Group'] == 'Cisgender women'].reset_index()
    c_women_perc = c_women['Count'] / g_counts['Count']
    c_women['Percentage'] = c_women_perc * 100
    #print(c_women)

    nb = hiv_data[hiv_data['Group'] == 'Alternative Gender'].reset_index()
    nb_perc = nb['Count'] / g_counts['Count']
    nb['Percentage'] = nb_perc * 100
    #print(nb)

    # By Race
    r_counts = hiv_data[hiv_data['Category'] == 'Race/Ethnicity']
    r_counts = r_counts.groupby('Year')['Count'].sum().reset_index()
    #print(r_counts)

    ai_an = hiv_data[hiv_data['Group'] == 'American Indian/Alaska Native'].reset_index()
    ai_an_perc = ai_an['Count'] / r_counts['Count']
    ai_an['Percentage'] = ai_an_perc * 100
    #print(ai_an)

    asian = hiv_data[hiv_data['Group'] == 'Asian*'].reset_index()
    as_perc = asian['Count'] / r_counts['Count']
    asian['Percentage'] = as_perc * 100
    #print(asian)

    black = hiv_data[hiv_data['Group'] == 'Black/African American'].reset_index()
    black_perc = black['Count'] / r_counts['Count']
    black['Percentage'] = black_perc * 100
    #print(black)

    latine = hiv_data[hiv_data['Group'] == 'Latinx*'].reset_index()
    latine_perc = latine['Count'] / r_counts['Count']
    latine['Percentage'] = latine_perc * 100
    #print(latine)

    nh_pi = hiv_data[hiv_data['Group'] == 'Native Hawaiian/Pacific Islander'].reset_index()
    nh_pi_perc = nh_pi['Count'] / r_counts['Count']
    nh_pi['Percentage'] = nh_pi_perc * 100
    #print(nh_pi)

    white = hiv_data[hiv_data['Group'] == 'White'].reset_index()
    white_perc = white['Count'] / r_counts['Count']
    white['Percentage'] = white_perc * 100
    #print(white)

    multi_r = hiv_data[hiv_data['Group'] == 'Multiple races'].reset_index()
    multi_r_perc = multi_r['Count'] / r_counts['Count']
    multi_r['Percentage'] = multi_r_perc * 100
    #print(multi_r)

    unknown = hiv_data[hiv_data['Group'] == 'Unknown race'].reset_index()
    unknown_perc = unknown['Count'] / r_counts['Count']
    unknown['Percentage'] = unknown_perc * 100
    #print(unknown)

if __name__ == '__main__':
    main()
