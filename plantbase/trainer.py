from plantbase.models import CNN_basic

    ESTIMATOR = 'CNN_basic'
    EXPERIMENT_NAME = 'PlantBaseTrainer'

    def __init__(self, X, Y, **kwargs):

    def get_estimator(self):
        estimator = self.kwargs.get('estimator', self.ESTIMATOR)
        if estimator == 'CNN_basic':
            model = Sequential()
            model.add(Conv2D(30, (5,5), strides=(1,1), padding='valid', input_shape=(256,256, 3), activation='relu'))
            model.add(MaxPooling2D(3))
            model.add(Conv2D(60, (2, 2), padding='same', activation='relu'))
            model.add(MaxPooling2D(3))
            model.add(Conv2D(50, (2, 2), padding='same', activation='relu'))
            model.add(MaxPooling2D(3))
            model.add(Flatten())
            model.add(Dense(25))
            model.add(Activation('softmax'))
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        else:
            pass

    def set_pipeline(self):
        self.set_pipeline = Pipeline(steps=[('rgs', self.get_estimator())])

    def train(self):
        es = EarlyStopping(monitor='val_loss',
               patience=5,
               mode='min')
        history = model.fit(tmp_dataset,
                            callbacks=[es],
                            epochs=100,
                            batch_size=32)
