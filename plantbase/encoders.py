import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from plantbase.data import get_data, clean_df
# from plantbase.utils import utils

class ResizeImage(BaseEstimator, TransformerMixin):

    def __init__(self, image):
        self.image = image

    def transform(self):
        return self

    def fit(self):
        return self


if __name__ == '__main__':
    params = dict()
    df = get_data(**params)
    df = clean_df(df)
    resize = ResizeImage()
    df_fit = resize.fit(df)
    df_trans = resize.transform(df)
