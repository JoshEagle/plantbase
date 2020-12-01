import joblib
import pandas as pd
import os
import pytz
import streamlit as st
import numpy as np
from PIL import Image
import streamlit.components.v1 as components
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
plants_care = pd.read_csv('plantbase/scraping/plant_info_wk2.csv')

# Page formatting and image display

st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown("<h1 style='text-align: left; color: red;'img/h1>", unsafe_allow_html=True)
img = st.image('plantbase/data/plantbase_logo.png', width=200, output_format='png') #exchange logo for something else?

st.title("PlantBase")

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


 #add button click here to confirm

if st.button('My plant'):
    result = add(1, 2)
    st.write('result: %s' % result)

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


Cultivation = st.write(plants_care['Cultivation'].to_string())

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


# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Cultivation
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
           st.write(plants_care['Cultivation'].to_string())
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
