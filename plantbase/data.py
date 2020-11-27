import pandas as pd
# from google.cloud import storage
# from params import BUCKET_NAME, BUCKET_TRAIN_DATA_PATH
from tensorflow.keras.preprocessing import image_dataset_from_directory

LOCAL_PATH = '../raw_data/train'
# GCP_PATH = "gs://{}/{}".format(BUCKET_NAME, BUCKET_TRAIN_DATA_PATH)"


# Method to get training data (or portion of it) from GCP or local disk:

# @simple_time_tracker

def get_data(local=True, **kwargs):

    # Add Client() here
    # client = storage.Client()
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

    print(type(train_dataset))
    print(type(val_dataset))

    return (train_dataset, val_dataset)


# Cleaning data from original source

def clean_df(df, test=False):

    return df


if __name__ == '__main__':
    params = dict()
    df = get_data(**params)
