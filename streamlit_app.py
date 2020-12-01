import joblib
import pandas as pd
import os
import pytz
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

#page layout
# def local_css(file_name): # taking values from app_style folder
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#         uploaded_file = st.file_uploader('')
#         local_css("style.css")

#care and plants info import
plants_care = pd.read_csv('plants/scraping/plants_info.csv')
#plants_images_info = pd.read_csv('priority_plants_VF.csv')

# Page formatting and image display
#@st.cashe
#def read logo(n_)
st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown("<h1 style='text-align: left; color: red;'img/h1>", unsafe_allow_html=True)
img = st.image('plantbase/data/plantbase_logo.png', width=200, output_format='png') #exchange logo for something else?

st.title("#PlantBase")

st.write('')
st.markdown("### Welcome to PlantBase, your best friend in growing outdoors shrub")

st.write('')
st.subheader('We will identify the plant of your dreams, and return your compatibility.')
st.write('Follow the instructions below to get started.')
st.write('')
st.write('')
st.write("")


st.header("Please upload an image of the flower you would like to identify")
st.markdown("### The app works best when the picture is of the actual flower of the plant, rather than leaves or stem")

#file selector, upload from your pc
uploaded_file = st.file_uploader('', type=("png", "jpg"))


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

#-----------------------

# code for load & model prediction

#-----------------------

#code to show 3 top predictions

st.write('')
st.subheader('Please select picture of your flower')
st.write('')
st.write('')
st.write("")
 # Show prediction results

if st.button('This is My plant'):
    st.write('plant name') # add plant name
# else:
#     st.write('Goodbye')

 #add button click here to confirm
# def button
# if st.button('My plant'):
#     result = add(1, 2)
#     st.write('result: %s' % result)

# show image of choosen flower

#st.subheader(f"**Your plant name is{plants_care['Species'].iloc[0]}**")
st.write('')
st.write('')
st.write("")

st.write('')
st.subheader("Here is something you did not know about your flower...")
#add wrapper
# st.write(plants_care['Genus description'].to_string())
# st.write(plants_care['Genus details'].to_string())



st.write('')
st.subheader("***How to grow your plant***")
st.subheader("Cultivation")

#def wrapper(self)

#add wrapper
#st.write(plants_care['How to grow_Cultivation'].to_string())

st.subheader("Propagation")
#add wrapper
#st.write(plants_care['How to grow_ Propogation'].to_string())

st.subheader("Where to plant")
#add wrapper
#st.write(plants_care['How to grow_ Suggested planting locations and garden types'].to_string())

st.subheader("Pruning")
#add wrapper
#st.write(plants_care['How to care_ Pruning'].to_string())

st.subheader("Pests")
#add wrapper
#st.write(plants_care['How to care_Pests'].to_string())

st.subheader("Diseases")
#add wrapper
#st.write(plants_care['How to care_Diseases'].to_string())



#-----------------------------------

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




# not used code
# st.markdown('**Please describe the room conditions for the plant**')

# display = ("Click me",
#            "Little sun",
#            "Medium sun",
#            "Full sun")

# options = list(range(len(display)))
# value_light = st.selectbox("How much sun will the plant have?", options, format_func=lambda x: display[x])

# st.write("")
# st.write("")

# display = ("Click me, too",
#           "Once a month (Little)",
#           "Twice a month (Sometimes)",
#            "Once a week (Often)",
#             "Twice a week (Very often)")
# options = list(range(len(display)))
# value_water = st.selectbox("How often will you be able to water the plant?", options, format_func=lambda x: display[x])
