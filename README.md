# What is Plantbase?
Plantbase is an app that uses a neural network to help the user identify a plant genus and provide plant care recommendations. 

# Why Plantbase?
Many plant owners today are not familiar with the care their plants actually need and end up improvising a care plan. Plantbase will help users determine the type of plant they have purchased and will provide them with detailed advice on how to care for their plants. 

# Where does the data come from? 

Image database:
- PlantView database contains 113,205 pictures belonging each to one of the 7 types of view reported into the meta-data, in a xml file (one per image) with explicit tags, used in the ImageCLEF/LifeCLEF project

Scrapping Royal Horticultural Society website
- The site contains 'growing guides' for each genus of plants, including advice on how to plant the flowers, how to perform on-going care, how to propagate, etc. 

Metaweather API:
- The API provides a 5-day weather forecast

# What models did we use?

Baseline model: Convolutional neural network with 3 convolutional layers separated by 3 pooling layers and followed by a Flattening and a Dense layer
-30% success rate (top probability is the correct species)

Transfer learning using VGG16 model from "Very Deep Convolutional Networks for Large-Scale Image Recognition”, K. Simonyan and A. Zisserman (University of Oxford)
- The model also uses convolutional & max pooling layers but uses 16 and was trained on +14M images
- 61 % success rate (top probability is the correct species), 86% success rate (top probability for top 3 genus)

# Data pre-processing

Our baseline model revealed two significant issues: 
-Overfitting: effective at predicting images in our training set but did not generalise well to our test data
-Class imbalance: predicting the majority class overly frequently

We used data augmentation and class weights to help resolve these issues 

# Predictions and recommendations on Streamlit app

Step 1: The user uploads an image a plan

Step 2: The model matches the plant with a genus 

Step 3: The app displays a generic image for the predicted genus (determined in Step 2) and asks the user to confirm this is the same type of plant

Step 4: 
- 4a: If the user confirms the predicted genus, the model matches the genus with a plant care plan specific to the genus and display the care plan + weather forecast
- 4b: If the user rejects the predicted genus, the app will display the next two nearest looking plant genus and will run Step 3 and 4a

# Going further
- Increase the number of images per genus
- Increase the number of plant genus
- Test higher quality images
- Provide more accurate weather based advice 


# Setting up the project

Create virtualenv and install the project:
```bash
  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
  $ make clean install test
```

Check for plantbase in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/plantbase`
- Then populate it:

```bash
  $ ##   e.g. if group is "{group}" and project_name is "plantbase"
  $ git remote add origin git@gitlab.com:{group}/plantbase.git
  $ git push -u origin master
  $ git push -u origin --tags
```

Functionnal test with a script:
```bash
  $ cd /tmp
  $ plantbase-run
```
# Install
Go to `gitlab.com/{group}/plantbase` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:
```bash
  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:
```bash
  $ git clone gitlab.com/{group}/plantbase
  $ cd plantbase
  $ pip install -r requirements.txt
  $ make clean install test                # install and test
```
Functionnal test with a script:
```bash
  $ cd /tmp
  $ plantbase-run
``` 
# Continus integration
## Github 
Every push of `master` branch will execute `.github/workflows/pythonpackages.yml` docker jobs.
## Gitlab
Every push of `master` branch will execute `.gitlab-ci.yml` docker jobs.
