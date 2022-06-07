"""
This file contains testing code for the
hivaids_inUS_2011_2017.py file
"""

import hivaids_inUS_2011_2017
import pandas as pd


def test_gender(dataset):
    """
    Tests the gender method
    with the test dataset,
    prints out data values and
    saves test picture to 'gender test.png'
    """
    hivaids_inUS_2011_2017.gender(dataset, show_data=True,
                                  png_name='gender test')


def test_race(dataset):
    """
    Tests the race method
    with the test dataset,
    prints out data values and
    saves test picture to 'race test.png'
    """
    hivaids_inUS_2011_2017.race(dataset, show_data=True,
                                png_name='race test')


def test_m_transmission(dataset):
    """
    Tests the m_transmission method
    with the test dataset,
    prints out data values and
    saves test picture to 'mt test.png'
    """
    hivaids_inUS_2011_2017.m_transmission(dataset, show_data=True,
                                          png_name='mt test')


def test_f_transmission(dataset):
    """
    Tests the f_transmission method
    with the test dataset,
    prints out data values and
    saves test picture to 'ft test.png'
    """
    hivaids_inUS_2011_2017.f_transmission(dataset, show_data=True,
                                          png_name='ft test')


def main():
    dataset = pd.read_csv('hiv_aids_2011-2017_test.csv')
    test_gender(dataset)
    test_race(dataset)
    test_m_transmission(dataset)
    test_f_transmission(dataset)


if __name__ == '__main__':
    main()
