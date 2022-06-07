import hivaids_inUS_2011_2017
import pandas as pd


def test_gender(dataset):
    hivaids_inUS_2011_2017.gender(dataset, show_data=True,
                                  png_name='gender test')


def test_race(dataset):
    hivaids_inUS_2011_2017.race(dataset, show_data=True,
                                png_name='race test')


def test_m_transmission(dataset):
    hivaids_inUS_2011_2017.m_transmission(dataset, show_data=True,
                                          png_name='mt test')


def test_f_transmission(dataset):
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