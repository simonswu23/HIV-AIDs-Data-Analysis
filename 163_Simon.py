import pandas as pd
import matplotlib.pyplot as plt


# import geopandas as gpd
# not working -- troubleshoot

def main():
    hiv_data = pd.read_csv('C:\\Users\\simon\\Downloads\\persons-living-with-hiv-aids-2011-2017.csv')
    print(hiv_data)

if __name__ == '__main__':
    main()
