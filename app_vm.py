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


#care and plants info import

plants_care = pd.read_csv('plantbase/scraping/plant_info_wk2.csv')

# Page formatting and image display
st.set_option('deprecation.showfileUploaderEncoding', False)
img = st.image('plantbase/data/plantbase_logo.png', style= 'left', width=700, output_format='png') #exchange logo for something else?

st.write('')
st.markdown("<h3 style='text-align: center; color: green;'>Welcome to PlantBase, your best friend in growing outdoors shrub</h3>", unsafe_allow_html=True)

st.write('')
st.markdown("<h3 style='text-align: center; color: green;'>We will identify the plant of your dreams, and return your compatibility. </h3>", unsafe_allow_html=True)
st.write('')
st.write('')
st.markdown("<h5 style='text-align: left; color: black;'> Please upload an image of the FLOWER from plant you would like to identify. </h5", unsafe_allow_html=True)

#file selector, upload from your pc
uploaded_file = st.file_uploader('', type=("png", "jpg"))

if uploaded_file is not None:
    # load and preprocess the image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    img = img.resize((224,224))
    img = img_to_array(img)
    X_list = []
    X_list.append(img)
    X = np.stack(X_list, axis = 0)

    # load model and predict with tensorflow load_model
    local_model = load_model('/home/jupyter/saved_models/josh_vgg_v2')
    # reconstructed_model = load_model('/home/jupyter/saved_models/josh_vgg_v2')
    y_pred = local_model.predict(X)
    # key for renaming columns
    rename_columns = {0: 'Ajuga',
                 1: 'Allium',
                 2: 'Campanula',
                 3: 'Cirsium',
                 4: 'Crataegus',
                 5: 'Gentiana',
                 6: 'Geranium',
                 7: 'Iris',
                 8: 'Malva',
                 9: 'Narcissus',
                 10: 'Ophrys',
                 11: 'Rosa',
                 12: 'Trifolium',
                 13: 'Verbascum',
                 14: 'Veronica',
                 15: 'Viola'}
    # convert pred to dataframe with names columns
    y_pred_df = pd.DataFrame(y_pred)
    y_pred_df = y_pred_df.rename(columns = rename_columns)
    #st.write(y_pred_df)
    pred1 = y_pred_df.idxmax(axis=1)[0]

#------------------------------------------------------------------

    name = st.subheader(f"**We think your plant is {pred1}**")
    st.write('')
    # name = st.subheader(f"**Your plant name is {plants_care['Genus name'].iloc[0]}**")

    plant_features = ['Genus','Details', 'Cultivation', 'Propagation', 'Suggested planting locations and garden types', 'Pruning', 'Pests', 'Diseases ']

#----------------two pictures under  the plant Genus---------------

    path = ('plantbase/data/plant_examples') # exchange once data is in virtual machine

    pred1_img1= Image.open(f'{path}/{pred1}.jpg')
    pred1_img2= Image.open(f'{path}/{pred1}{"2.jpg"}')
    def flowers():
        for file in os.listdir(path):
            if pred1 in file:
                return pred1_img1, pred1_img2

    pred1_img1 = pred1_img1.resize((200,200))
    pred1_img2 = pred1_img2.resize((200,200))

    col1, col2 = st.beta_columns(2)
    col1.image(pred1_img1, use_column_width=True)
    col2.image(pred1_img2, use_column_width=True)

    cnn_model = load_model('/home/jupyter/saved_models/augmented_basic_cnn')
    cnn_preds = cnn_model.predict(X)
    cnn_preds_df = pd.DataFrame(cnn_preds)
    cnn_preds_df = cnn_preds_df.rename(columns = rename_columns)
    cnn_top_3 =pd.DataFrame(cnn_preds_df.apply(lambda x:list(cnn_preds_df.columns[np.array(x).argsort()[::-1][:3]]), axis=1).to_list(),
                                              columns=['first', 'second', 'third'])
    if pred1 == cnn_top_3['first'][0]:
        pred2 = cnn_top_3['second'][0]
        pred3 = cnn_top_3['third'][0]
    elif pred1 == cnn_top_3['second'][0]:
        pred2 = cnn_top_3['first'][0]
        pred3 = cnn_top_3['third'][0]
    else:
        pred2 = cnn_top_3['first'][0]
        pred3 = cnn_top_3['second'][0]


    pred2_img = Image.open(f'{path}/{pred2}.jpg').resize((200,200))
    pred3_img = Image.open(f'{path}/{pred3}.jpg').resize((200,200))

    st.markdown(f'We think your plant is {pred1}. Does that look right to you?')

    if st.button(f'Yes, my plant looks like {pred1}!'):

        plant_name = pred1

        def how_to_grow(plant_name, plants_care, plant_features):
            if plant_name in list(plants_care['Genus name']):
                feature = plants_care.iloc[plants_care.index[plants_care['Genus name'] == plant_name]][plant_features].iloc[0]
            return feature

        st.markdown("<h1 style='text-align: left; color: green;'>How to grow your plant</h1>", unsafe_allow_html=True)

        # # bootstrap 4 collapse example
        components.html(
            f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script><div id='accordion'><div class='card'><div class='card-header' id='headingOne'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>{'Here is something you did not know about your plant...'}</button></h5></div><div id='collapseOne' class='collapse' aria-labelledby='headingOne' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Genus')}</div></div></div><div class='card'><div class='card-header' id='headingZero'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseZero' aria-expanded='true' aria-controls='collapseZero'>{'Details'}</button></h5></div><div id='collapseZero' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Details')}</div></div></div><div class='card'><div class='card-header' id='headingTwo'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>{'Cultivation'}</button></h5></div><div id='collapseTwo' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Cultivation')}</div></div></div><div class='card'><div class='card-header' id='headingTree'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTree' aria-expanded='true' aria-controls='collapseTree'>{'Propagation'}</button></h5></div><div id='collapseTree' class='collapse' aria-labelledby='headingTree' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Propagation')}</div></div></div><div class='card'><div class='card-header' id='headingFour'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>{'Suggested planting locations and garden types'}</button></h5></div><div id='collapseFour' class='collapse' aria-labelledby='headingFour' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Suggested planting locations and garden types')}</div></div></div><div class='card'><div class='card-header' id='headingFive'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>{'Pruning'}</button></h5></div><div id='collapseFive' class='collapse' aria-labelledby='headingFive' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pruning')}</div></div></div><div class='card'><div class='card-header' id='headingSix'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>{'Pests'}</button></h5></div><div id='collapseSix' class='collapse' aria-labelledby='headingSix' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pests')}</div></div></div><div class='card'><div class='card-header' id='headingSeven'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSeven' aria-expanded='true' aria-controls='collapseSeven'>{'Diseases'}</button></h5></div><div id='collapseSeven' class='collapse' aria-labelledby='headingSeven' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Diseases')}</div></div></div></div>",
            height=600)

    st.markdown(f'Otherwise, does your plant look like {pred2} or {pred3}?')

    col1, col2 = st.beta_columns(2)
    col1.image(pred2_img, use_column_width=True)
    col1.subheader(pred2)
    if st.button(f'My plant actually looks like {pred2}.'):

        plant_name = pred2

        def how_to_grow(plant_name, plants_care, plant_features):
            if plant_name in list(plants_care['Genus name']):
                feature = plants_care.iloc[plants_care.index[plants_care['Genus name'] == plant_name]][plant_features].iloc[0]
            return feature

        st.markdown("<h1 style='text-align: left; color: green;'>How to grow your plant</h1>", unsafe_allow_html=True)

        # # bootstrap 4 collapse example
        components.html(
            f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script><div id='accordion'><div class='card'><div class='card-header' id='headingOne'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>{'Here is something you did not know about your plant...'}</button></h5></div><div id='collapseOne' class='collapse' aria-labelledby='headingOne' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Genus')}</div></div></div><div class='card'><div class='card-header' id='headingZero'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseZero' aria-expanded='true' aria-controls='collapseZero'>{'Details'}</button></h5></div><div id='collapseZero' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Details')}</div></div></div><div class='card'><div class='card-header' id='headingTwo'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>{'Cultivation'}</button></h5></div><div id='collapseTwo' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Cultivation')}</div></div></div><div class='card'><div class='card-header' id='headingTree'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTree' aria-expanded='true' aria-controls='collapseTree'>{'Propagation'}</button></h5></div><div id='collapseTree' class='collapse' aria-labelledby='headingTree' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Propagation')}</div></div></div><div class='card'><div class='card-header' id='headingFour'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>{'Suggested planting locations and garden types'}</button></h5></div><div id='collapseFour' class='collapse' aria-labelledby='headingFour' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Suggested planting locations and garden types')}</div></div></div><div class='card'><div class='card-header' id='headingFive'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>{'Pruning'}</button></h5></div><div id='collapseFive' class='collapse' aria-labelledby='headingFive' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pruning')}</div></div></div><div class='card'><div class='card-header' id='headingSix'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>{'Pests'}</button></h5></div><div id='collapseSix' class='collapse' aria-labelledby='headingSix' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pests')}</div></div></div><div class='card'><div class='card-header' id='headingSeven'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSeven' aria-expanded='true' aria-controls='collapseSeven'>{'Diseases'}</button></h5></div><div id='collapseSeven' class='collapse' aria-labelledby='headingSeven' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Diseases')}</div></div></div></div>",
            height=600)

    col2.image(pred3_img, use_column_width=True)
    col2.subheader(pred3)
    if st.button(f'My plant actually looks like {pred3}.'):

        plant_name = pred3
        def how_to_grow(plant_name, plants_care, plant_features):
            if plant_name in list(plants_care['Genus name']):
                feature = plants_care.iloc[plants_care.index[plants_care['Genus name'] == plant_name]][plant_features].iloc[0]
            return feature

        st.markdown("<h1 style='text-align: left; color: green;'>How to grow your plant</h1>", unsafe_allow_html=True)

        # # bootstrap 4 collapse example
        components.html(
            f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script><div id='accordion'><div class='card'><div class='card-header' id='headingOne'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseOne' aria-expanded='true' aria-controls='collapseOne'>{'Here is something you did not know about your plant...'}</button></h5></div><div id='collapseOne' class='collapse' aria-labelledby='headingOne' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Genus')}</div></div></div><div class='card'><div class='card-header' id='headingZero'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseZero' aria-expanded='true' aria-controls='collapseZero'>{'Details'}</button></h5></div><div id='collapseZero' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Details')}</div></div></div><div class='card'><div class='card-header' id='headingTwo'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTwo' aria-expanded='true' aria-controls='collapseTwo'>{'Cultivation'}</button></h5></div><div id='collapseTwo' class='collapse' aria-labelledby='headingZero' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Cultivation')}</div></div></div><div class='card'><div class='card-header' id='headingTree'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseTree' aria-expanded='true' aria-controls='collapseTree'>{'Propagation'}</button></h5></div><div id='collapseTree' class='collapse' aria-labelledby='headingTree' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Propagation')}</div></div></div><div class='card'><div class='card-header' id='headingFour'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFour' aria-expanded='true' aria-controls='collapseFour'>{'Suggested planting locations and garden types'}</button></h5></div><div id='collapseFour' class='collapse' aria-labelledby='headingFour' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Suggested planting locations and garden types')}</div></div></div><div class='card'><div class='card-header' id='headingFive'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseFive' aria-expanded='true' aria-controls='collapseFive'>{'Pruning'}</button></h5></div><div id='collapseFive' class='collapse' aria-labelledby='headingFive' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pruning')}</div></div></div><div class='card'><div class='card-header' id='headingSix'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSix' aria-expanded='true' aria-controls='collapseSix'>{'Pests'}</button></h5></div><div id='collapseSix' class='collapse' aria-labelledby='headingSix' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Pests')}</div></div></div><div class='card'><div class='card-header' id='headingSeven'><h5 class='mb-0'><button class='btn btn-link collapsed' data-toggle='collapse' data-target='#collapseSeven' aria-expanded='true' aria-controls='collapseSeven'>{'Diseases'}</button></h5></div><div id='collapseSeven' class='collapse' aria-labelledby='headingSeven' data-parent='#accordion'><div class='card-body'>{how_to_grow(plant_name, plants_care, 'Diseases')}</div></div></div></div>",
            height=600)

st.markdown("<h1 style='text-align: left; color: green;'>London 5 day weather forecast</h1>", unsafe_allow_html=True)

st.markdown("Plants can be sensitive, and weather can be volatile. \
    This exclusive London trial of PlantBase is rolling out in London, so we've specialised the weather forecast for you. \
    You'll see alerts here where there are unusual weather conditions that could harm your plants.")

weather = pd.read_csv('plantbase/weather_API/44418-today.csv')

weather_states = ['Snow','Sleet','Hail','Thunderstorm','Heavy Rain']

for i in range(5):
    for j in range(len(weather_states)):
        if weather['weather_state_name'][i] == weather_states[j]:
            st.markdown(f"Warning! {weather_states[j]} forecast on {weather['applicable_date'][i]}.")
    if int(weather['min_temp'][i].split()[0]) <= 1:
        st.markdown(f"Warning! Frosty conditions expected on {weather['applicable_date'][i]}.")
    if int(weather['max_temp'][i].split()[0]) >= 28:
        st.markdown(f"Warning! Heat wave expected on {weather['applicable_date'][i]}.")
    if int(weather['wind_speed'][i].split()[0]) >= 32:
        st.markdown(f"Warning! Gale force winds expected on {weather['applicable_date'][i]}.")

weather_st = st.dataframe(weather)
