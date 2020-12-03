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


plants_care = pd.read_csv('plantbase/scraping/plant_info_wk2.csv')

img = st.image('plantbase/data/plantbase_logo.png', style= 'left', width=700, output_format='png') #exchange logo for something else?


st.markdown("<h3 style='text-align: center; color: green;'>Welcome to PlantBase, your best friend in growing outdoors shrub</h3>", unsafe_allow_html=True)

st.write('')
st.markdown("<h3 style='text-align: center; black: green;'>We will identify the plant of your dreams, and return your compatibility. </h3>", unsafe_allow_html=True)
#.write('Follow the instructions below to get started.')
st.write('')
st.write('')
st.markdown("<h5 style='text-align: left; black: black;'> Please upload an image of the FLOWER from plant you would like to identify. </h5", unsafe_allow_html=True)

#st.markdown("### The app works best when the picture is of the actual flower of the plant, rather than leaves or stem")
#file selector, upload from your pc

uploaded_file = st.file_uploader('', type=("png", "jpg"))


if uploaded_file is not None:
    # load and preprocess the image
    img = Image.open(uploaded_file)
    img = img.resize((224,224))
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    img = img_to_array(img)
    X_list = []
    X_list.append(img)
    X = np.stack(X_list, axis = 0)


    # show image of choosen flower

    st.write('')
    name = st.subheader(f"**Your plant name is {plants_care['Genus name'].iloc[0]}**")
#--------------------------two pictures-----------

    plant_name = plants_care['Genus name'].iloc[0]
    path = ('plantbase/data/plant_examples')

    plant= Image.open(f'{path}/{plant_name}.jpg')
    plant2= Image.open(f'{path}/{plant_name}{"2.jpg"}')
    def flowers():
        for file in os.listdir(path):
            if plant_name in file:
                plant, plant2
            return plant, plant2
    plant.resize((224,224)) # the picturs are not equal
    plant2.resize((224,224))

    st.image([plant,plant2], width=100)
#----------------------------buttons -----------------
    plant_features= ['Genus','Details', 'Cultivation', 'Propagation', 'Suggested planting locations and garden types', 'Pruning', 'Pests', 'Diseases ']
    #plant_name = plants_care['Genus name'].iloc[0] # only for internal testing
    plant_folders = ('plantbase/raw_data/train')

    # plant1= st.image([plant])
    # plant2= st.image([plant2])

    # if st.button('This is NOT my plant'):
    #     st.write('Sorry that was wrong, is this your picture?')
    #     right_plant = st.radio('Which is your plant?',
    #     (plant1, plant2)


        # if right_plant == 'plant1'

        #     st.markdown(f"**This is your plant{st.image([plant])}**")
        # else:
        #     st.markdown(f"**This is your plant{st.image([plant2])}**")



    # if st.button('This is my plant'):
    #     def how_to_grow(plant_name, plants_care, plant_features):
    #         if plant_name in list(plants_care['Genus name']):
    #             feature = plants_care.iloc[plants_care.index[plants_care['Genus name'] == plant_name]][plant_features].iloc[0]
    #         return feature

    #         st.markdown("<h1 style='text-align: left; color: green;'>How to grow your plant</h1>", unsafe_allow_html=True)

    #         components.html(
    #         f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script><div id='accordion'><div class='card'><div class='card-header' id='headingOne'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>{'Here is something you did not know about your plant...'}</button></h5></div><div id='collapseOne' class='collapse' aria-labelledby='headingOne' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Genus')}</div></div></div><div class='card'><div class='card-header' id='headingZero'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseZero' aria-expanded='true' aria-controls='collapseZero'>{'Details'}</button></h5></div><div id='collapseZero' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Details')}</div></div></div><div class='card'><div class='card-header' id='headingTwo'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>{'Cultivation'}</button></h5></div><div id='collapseTwo' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Cultivation')}</div></div></div><div class='card'><div class='card-header' id='headingTree'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTree' aria-expanded='true' aria-controls='collapseTree'>{'Propagation'}</button></h5></div><div id='collapseTree' class='collapse' aria-labelledby='headingTree' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Propagation')}</div></div></div><div class='card'><div class='card-header' id='headingFour'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>{'Suggested planting locations and garden types'}</button></h5></div><div id='collapseFour' class='collapse' aria-labelledby='headingFour' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Suggested planting locations and garden types')}</div></div></div><div class='card'><div class='card-header' id='headingFive'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>{'Pruning'}</button></h5></div><div id='collapseFive' class='collapse' aria-labelledby='headingFive' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pruning')}</div></div></div><div class='card'><div class='card-header' id='headingSix'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>{'Pests'}</button></h5></div><div id='collapseSix' class='collapse' aria-labelledby='headingSix' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pests')}</div></div></div><div class='card'><div class='card-header' id='headingSeven'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSeven' aria-expanded='true' aria-controls='collapseSeven'>{'Diseases'}</button></h5></div><div id='collapseSeven' class='collapse' aria-labelledby='headingSeven' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Diseases')}</div></div></div></div>",
    #         height=600,
    #         )

        # if st.button('This is my plant'):
        #     def how_to_grow(plant_name, plants_care, plant_features):
        #         if plant_name in list(plants_care['Genus name']):
        #             feature = plants_care.iloc[plants_care.index[plants_care['Genus name'] == plant_name]][plant_features].iloc[0]
        #         return feature

        #     st.markdown("<h1 style='text-align: left; color: green;'>How to grow your plant</h1>", unsafe_allow_html=True)

        #     components.html(
        #     f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script><div id='accordion'><div class='card'><div class='card-header' id='headingOne'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>{'Here is something you did not know about your plant...'}</button></h5></div><div id='collapseOne' class='collapse' aria-labelledby='headingOne' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Genus')}</div></div></div><div class='card'><div class='card-header' id='headingZero'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseZero' aria-expanded='true' aria-controls='collapseZero'>{'Details'}</button></h5></div><div id='collapseZero' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Details')}</div></div></div><div class='card'><div class='card-header' id='headingTwo'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>{'Cultivation'}</button></h5></div><div id='collapseTwo' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Cultivation')}</div></div></div><div class='card'><div class='card-header' id='headingTree'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTree' aria-expanded='true' aria-controls='collapseTree'>{'Propagation'}</button></h5></div><div id='collapseTree' class='collapse' aria-labelledby='headingTree' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Propagation')}</div></div></div><div class='card'><div class='card-header' id='headingFour'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>{'Suggested planting locations and garden types'}</button></h5></div><div id='collapseFour' class='collapse' aria-labelledby='headingFour' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Suggested planting locations and garden types')}</div></div></div><div class='card'><div class='card-header' id='headingFive'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>{'Pruning'}</button></h5></div><div id='collapseFive' class='collapse' aria-labelledby='headingFive' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pruning')}</div></div></div><div class='card'><div class='card-header' id='headingSix'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>{'Pests'}</button></h5></div><div id='collapseSix' class='collapse' aria-labelledby='headingSix' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pests')}</div></div></div><div class='card'><div class='card-header' id='headingSeven'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSeven' aria-expanded='true' aria-controls='collapseSeven'>{'Diseases'}</button></h5></div><div id='collapseSeven' class='collapse' aria-labelledby='headingSeven' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Diseases')}</div></div></div></div>",
        #     height=600,
        # )





    # if st.button('This is my plant'):
    #     def how_to_grow(plant_name, plants_care, plant_features):
    #         if plant_name in list(plants_care['Genus name']):
    #             feature = plants_care.iloc[plants_care.index[plants_care['Genus name'] == plant_name]][plant_features].iloc[0]
    #         return feature

    #     st.markdown("<h1 style='text-align: left; color: green;'>How to grow your plant</h1>", unsafe_allow_html=True)

    #     components.html(
    #     f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script><div id='accordion'><div class='card'><div class='card-header' id='headingOne'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>{'Here is something you did not know about your plant...'}</button></h5></div><div id='collapseOne' class='collapse' aria-labelledby='headingOne' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Genus')}</div></div></div><div class='card'><div class='card-header' id='headingZero'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseZero' aria-expanded='true' aria-controls='collapseZero'>{'Details'}</button></h5></div><div id='collapseZero' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Details')}</div></div></div><div class='card'><div class='card-header' id='headingTwo'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>{'Cultivation'}</button></h5></div><div id='collapseTwo' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Cultivation')}</div></div></div><div class='card'><div class='card-header' id='headingTree'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTree' aria-expanded='true' aria-controls='collapseTree'>{'Propagation'}</button></h5></div><div id='collapseTree' class='collapse' aria-labelledby='headingTree' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Propagation')}</div></div></div><div class='card'><div class='card-header' id='headingFour'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>{'Suggested planting locations and garden types'}</button></h5></div><div id='collapseFour' class='collapse' aria-labelledby='headingFour' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Suggested planting locations and garden types')}</div></div></div><div class='card'><div class='card-header' id='headingFive'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>{'Pruning'}</button></h5></div><div id='collapseFive' class='collapse' aria-labelledby='headingFive' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pruning')}</div></div></div><div class='card'><div class='card-header' id='headingSix'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>{'Pests'}</button></h5></div><div id='collapseSix' class='collapse' aria-labelledby='headingSix' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pests')}</div></div></div><div class='card'><div class='card-header' id='headingSeven'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSeven' aria-expanded='true' aria-controls='collapseSeven'>{'Diseases'}</button></h5></div><div id='collapseSeven' class='collapse' aria-labelledby='headingSeven' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Diseases')}</div></div></div></div>",
    #     height=600,
    # )
=======
    # #load model and predict with tensorflow load_model
    # reconstructed_model = load_model('/home/jupyter/saved_models/josh_vgg_v2')
    # y_pred = reconstructed_model.predict(X)
    # # key for renaming columns
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
    # # convert pred to dataframe with names columns
    # y_pred_df = pd.DataFrame(y_pred)
    # y_pred_df = y_pred_df.rename(columns = rename_columns)
    # st.write(y_pred_df)
    # plant_name = y_pred_df.idxmax(axis=1)[0]
    # st.write(plant_name)

#--------------delete? -------
    # transpose = y_pred_df.T
    # plant_info = plants_info_df[plants_info_df.genus.str.contains(output)]

#-----------------------


    #code to show 3 top predictions

    # st.write('')
    # st.subheader('Please select picture of your flower')
    # st.write('')
    # st.write('')
    # st.write("")
     # Show prediction results

     #add button click here to confirm
    # def button
    # if st.button('My plant'):
    #     result = add(1, 2)
    #     st.write('result: %s' % result)

    # show image of choosen flower

    #name= st.subheader(f"**Your plant name is {plant_name}**")
    st.write('')
    name = st.subheader(f"**Your plant name is {plants_care['Genus name'].iloc[0]}**")

    plant_features= ['Genus','Details', 'Cultivation', 'Propagation', 'Suggested planting locations and garden types', 'Pruning', 'Pests', 'Diseases ']

    #plant_name= plant_name # this plant name has to be here otherwise code is crushing with error UnboundLocalError: local variable referenced before assignment
    plant_name = plants_care['Genus name'].iloc[0] # only for internal testing
    # plant_folders = ('plantbase/raw_data/train')

    # def plant_image(plant_folders)
    #     if plant_name in

    # if st.button('This is NOT my plant'):
    #     st.write('') # code if not this plant then search for others
    # # else:
    # #     st.write('Goodbye')


    def how_to_grow(plant_name, plants_care, plant_features):
        if plant_name in list(plants_care['Genus name']):
            feature = plants_care.iloc[plants_care.index[plants_care['Genus name'] == plant_name]][plant_features].iloc[0]
        return feature

    st.markdown("<h1 style='text-align: left; color: green;'>How to grow your plant</h1>", unsafe_allow_html=True)

    # # bootstrap 4 collapse example
    components.html(
        f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script><div id='accordion'><div class='card'><div class='card-header' id='headingOne'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>{'Here is something you did not know about your plant...'}</button></h5></div><div id='collapseOne' class='collapse' aria-labelledby='headingOne' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Genus')}</div></div></div><div class='card'><div class='card-header' id='headingZero'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseZero' aria-expanded='true' aria-controls='collapseZero'>{'Details'}</button></h5></div><div id='collapseZero' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Details')}</div></div></div><div class='card'><div class='card-header' id='headingTwo'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>{'Cultivation'}</button></h5></div><div id='collapseTwo' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Cultivation')}</div></div></div><div class='card'><div class='card-header' id='headingTree'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTree' aria-expanded='true' aria-controls='collapseTree'>{'Propagation'}</button></h5></div><div id='collapseTree' class='collapse' aria-labelledby='headingTree' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Propagation')}</div></div></div><div class='card'><div class='card-header' id='headingFour'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>{'Suggested planting locations and garden types'}</button></h5></div><div id='collapseFour' class='collapse' aria-labelledby='headingFour' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Suggested planting locations and garden types')}</div></div></div><div class='card'><div class='card-header' id='headingFive'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>{'Pruning'}</button></h5></div><div id='collapseFive' class='collapse' aria-labelledby='headingFive' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pruning')}</div></div></div><div class='card'><div class='card-header' id='headingSix'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>{'Pests'}</button></h5></div><div id='collapseSix' class='collapse' aria-labelledby='headingSix' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pests')}</div></div></div><div class='card'><div class='card-header' id='headingSeven'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSeven' aria-expanded='true' aria-controls='collapseSeven'>{'Diseases'}</button></h5></div><div id='collapseSeven' class='collapse' aria-labelledby='headingSeven' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Diseases')}</div></div></div></div>",
        height=600,
    )

#---------------------------------------------------

#code used:
# bootstrap 4 collapse example
# components.html(
#     """
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#     <div id="accordion">

#       <div class="card">
#         <div class="card-header" id="headingOne">
#           <h5 class="mb-0">
#             <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
#             Cultivation
#             </button>
#           </h5>
#         </div>
#         <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
#           <div class="card-body">
#            cultivation
#           </div>
#         </div>
#       </div>

#     </div>
#     """,
#     height=600,
# )

st.markdown("<h1 style='text-align: left; color: green;'>London 5 day weather forecast</h1>", unsafe_allow_html=True)
weather = pd.read_csv('plantbase/weather_API/44418-today.csv')
weather_st = st.dataframe(weather)

