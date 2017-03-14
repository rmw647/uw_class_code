from urllib.request import urlretrieve
import os
import zipfile
import pandas as pd


DATA_URL = 'https://s3.amazonaws.com/pronto-data/open_data_year_one.zip'


def download_if_needed(url, filename, force_download=False):
    """ Download url to filename if filename does not exist """
    if force_download or not os.path.exists(filename):
        print("Downloading file from {0}".format(url))
        urlretrieve(URL, filename)
    else:
        print("File {0} already exists".format(filename))


def load_trip_data(filename='open_data_year_one.zip'):
    """ Load trip data and read csv into dataframe """
    download_if_needed(DATA_URL, filename)
    zf = zipfile.ZipFile(filename)
    return pd.read_csv(zf.open('2015_trip_data.csv'))


def plot_age_distribution(column_name='birthyear'):
    """ Plot distribution of age column in dataframe """
    df = load_trip_data()
    if column_name in df.columns:
        df[column_name].value_counts().sort_index().plot(linestyle='steps-mid')
    else:
        print("Sorry bro. The data had no {} column".format(column_name))


def test_trip_data():
    df = load_trip_data()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (142846, 12)


def test_distribution_plot():
    plot_age_distribution()
