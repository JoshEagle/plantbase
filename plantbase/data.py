import pandas as pd
from google.cloud import storage
from plantbase.params import BUCKET_NAME, BUCKET_TRAIN_DATA_PATH

LOCAL_PATH = '../raw_data/train'
GCP_PATH = "gs://{}/{}".format(BUCKET_NAME, BUCKET_TRAIN_DATA_PATH)"


# Method to get training data (or portion of it) from GCP or local disk:

@simple_time_tracker

def get_data(local=False, **kwargs):

    # Add Client() here
    client = storage.Client()
    if local:
        path = LOCAL_PATH
    else:
        path = GCP_PATH

    train_dataset = image_dataset_from_directory(
            path, labels='inferred', label_mode='int',
            color_mode='rgb', batch_size=32, image_size=(256, 256), shuffle=True, seed=123,
            validation_split=0.2, subset="training", interpolation='bilinear', follow_links=False
            )

    val_dataset = image_dataset_from_directory(
            path, labels='inferred', label_mode='int',
            color_mode='rgb', batch_size=32, image_size=(256, 256), shuffle=True, seed=123,
            validation_split=0.2, subset="validation", interpolation='bilinear', follow_links=False
            )

    return train_dataset, val_dataset

# def get_data(nrows=10000, local=False, optimize=False, **kwargs):
#     """method to get the training data (or a portion of it) from google cloud bucket"""
#     # Add Client() here
#     client = storage.Client()
#     if local:
#         path = "data/test.csv"
#     else:
#         path = "gs://{}/{}".format(BUCKET_NAME, BUCKET_TRAIN_DATA_PATH)
#     df = pd.read_csv(path, nrows=nrows)
#     return df
# Cleaning data from original source

def clean_df(df, test=False):

    # Cleaning adapted from exploratory Jupyter Notebook

    return df


if __name__ == '__main__':
    params = dict()
    df = get_data(**params)
