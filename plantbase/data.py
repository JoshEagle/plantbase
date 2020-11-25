import pandas as pd

LOCAL_PATH = ''
GCP_PATH = ''


# Method to get training data (or portion of it) from GCP or local disk:

@simple_time_tracker

def get_data(local=False, **kwargs):

    # Add Client() here
    if local:
        path = LOCAL_PATH
    else:
        path = GCP_PATH
    df = pd.read_csv(path)

    return df


# Cleaning data from original source

def clean_df(df, test=False):

    # Cleaning adapted from exploratory Jupyter Notebook

    return df


if __name__ == '__main__':
    params = dict()
    df = get_data(**params)
