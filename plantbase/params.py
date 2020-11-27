### GCP configuration - - - - - - - - - - - - - - - - - - -

# /!\ you should fill these according to your account

### GCP Project - - - - - - - - - - - - - - - - - - - - - -

PROJECT_ID = "plantbase"

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

BUCKET_NAME = 'plantbase_images'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# train data file location
# /!\ here you need to decide if you are going to train using the provided and uploaded data/train_1k.csv sample file
# or if you want to use the full dataset (you need need to upload it first of course)
BUCKET_TRAIN_DATA_PATH = '/train/'

##### Training  - - - - - - - - - - - - - - - - - - - - - -

# not required here

##### Model - - - - - - - - - - - - - - - - - - - - - - - -

# model folder name (will contain the folders for all trained model versions)
MODEL_NAME = 'plantbase_models'

# model version folder name (where the trained model.joblib file will be stored)
MODEL_VERSION = 'plantbase_v1'

### GCP AI Platform - - - - - - - - - - - - - - - - - - - -

