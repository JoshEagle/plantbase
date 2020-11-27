import time
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import pandas as pd


def get_test_data():
    test_df = pd.read_csv("../plantbase/data/test_data.csv").drop(columns = "Unnamed: 0")
    columns = np.sort(test_df.genus.unique())
    rename_columns = {}
    col_index = 0
    for n in columns:
        rename_columns[col_index] = n
        col_index += 1
    X_list = []
    y_list = []

    for index, row in test_df.iterrows():
        img = load_img(rf"../raw_data/test/{row.id}.jpg", target_size=(256, 256))
        img = tensorflow.keras.preprocessing.image.img_to_array(img)
        #img = tensorflow.expand_dims(img, 0)
        X_list.append(img)
        y_list.append((row.genus, row.id))
    #y_true_df = pd.DataFrame(y_list, columns = ['true_genus', 'id'])
    X_test = np.stack(X_list, axis=0)
    y_true = np.stack(y_list, axis = 0)

    return X_test, y_true



    y_pred = model.predict(X_test)
    y_pred_df = pd.DataFrame(y_pred)
    y_pred_df = y_pred_df.rename(columns = rename_columns)

    y_pred_df['pred_genus'] = y_pred_df.idxmax(axis = 1)
    prediction_review = (y_pred_df['pred_genus'] == y_true_df['true_genus'])
    prediction_vec_df = y_pred_df[['pred_genus']].copy()
    prediction_vec_df['true_genus'] = y_true_df['true_genus'].copy()
    prediction_vec_df['result'] = (y_pred_df['pred_genus'] == y_true_df['true_genus'])
    prediction_vec_df['false'] = prediction_vec_df['result'].apply(lambda x: 1 if x == False else 0)
    prediction_vec_df['true'] = prediction_vec_df['result'].apply(lambda x: 1 if x == True else 0)
    true_pos_neg = prediction_vec_df.groupby('true_genus').sum().drop(columns=['result'])
    true_pos_neg['percent_true'] = true_pos_neg['true'] / (true_pos_neg['true'] + true_pos_neg['false'])
    success_ratio = round(true_pos_neg[['percent_true']]*100).sort_values(by='percent_true', ascending=False)

    return success_ratio







# Decorators below:


def simple_time_tracker(method):

    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', method.__name__.upper())
            kwargs['log_time'][name] = int((te - ts))
        else:
            print(method.__name__, round(te - ts, 2))
        return result

    return timed
