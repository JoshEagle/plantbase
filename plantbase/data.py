import pandas as pd
# from google.cloud import storage
# from params import BUCKET_NAME, BUCKET_TRAIN_DATA_PATH
from tensorflow.keras.preprocessing.image import ImageDataGenerator

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

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        rotation_range=90,
        validation_split = 0.2)

    valid_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split = 0.2)

    train_generator = train_datagen.flow_from_directory(
                    path,
                    target_size=(img_height, img_width),
                    batch_size=32,
                    class_mode='binary',
                    subset='training',
                    seed = 123
                    )

    val_generator = valid_datagen.flow_from_directory(
                        directory, # same directory as training data
                        target_size=(img_height, img_width),
                        batch_size=32,
                        class_mode='binary',
                        subset='validation',
                        seed = 123)

    return (train_generator, val_generator)



if __name__ == '__main__':
    params = dict()
    df = get_data(**params)
