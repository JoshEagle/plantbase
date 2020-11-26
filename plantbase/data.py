import pandas as pd

LOCAL_PATH = ''
GCP_PATH = ''


# Method to get training data (or portion of it) from GCP or local disk:

@simple_time_tracker

def get_data(local=False, **kwargs):


    # root_path = os.getcwd()
    # #csv_path = os.path.join(root_path,'..','data') the absolute path don't work always so need to be reworked later on
    # csv_path = r'C:\Users\User\code\Joshymitzu\plantbase\plantbase\data'
    # plants_care= pd.read_csv(os.path.join(csv_path,'plants_info_enhanced.csv'))

    # directory = r"../raw_data/train"

    # tmp_dataset = image_dataset_from_directory(
    #     directory, labels='inferred', label_mode='int', class_names=None,
    #     color_mode='rgb', batch_size=32, image_size=(256, 256), shuffle=True, seed=None,
    #     validation_split=None, subset=None, interpolation='bilinear', follow_links=False





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
