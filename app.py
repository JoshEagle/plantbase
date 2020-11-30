import joblib
import pandas as pd
import pytz
import streamlit as st
import numpy as np
from PIL import Image,
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

st.header("PlantBase")
st.markdown("### A deep learning project to classify plant images and return plant care advice")

st.header("Please upload an image of the flower you would like to identify")
st.markdown("### The app works best when the picture is of the actual flower of the plant, rather than leaves or stem")


uploaded_file = st.file_uploader('')

if uploaded_file is not None:
    # load and preprocess the image
    img = Image.open(uploaded_file)
    img = Image.resize((256,256))
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    img = img_to_array(img)
    X_list = []
    X_list.append(img)
    X = np.stack(X_list, axis = 0)
    st.write(f"{X}")
    st.write(f"{type(X)}")
    st.write(f"{X_list}")
    st.write(f"X shape is {X.shape} ")


    # load model and predict
    # reconstructed_model = load_model('./model/cnn_1_ak/')
    # y_pred = reconstructed_model.predict(X)

    # rename_columns = {0: 'Ajuga',
    #              1: 'Allium',
    #              2: 'Campanula',
    #              3: 'Cirsium',
    #              4: 'Crataegus',
    #              5: 'Gentiana',
    #              6: 'Geranium',
    #              7: 'Iris',
    #              8: 'Malva',
    #              9: 'Narcissus',
    #              10: 'Ophrys',
    #              11: 'Rosa',
    #              12: 'Trifolium',
    #              13: 'Verbascum',
    #              14: 'Veronica',
    #              15: 'Viola'}

    # y_pred_df = pd.DataFrame(y_pred_recon, columns = rename_columns)
    # output = y_pred_recon_df.idxmax(axis=1)[0]
    # st.write(output)
    # transpose = y_pred_recon_df.T

