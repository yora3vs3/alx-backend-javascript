
# importing necessary libraries
import tensorflow as tf
from keras import layers
import numpy as np

# defining the model architecture
model = tf.keras.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(7,)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy',
              metrics=['accuracy'])

# loading the data into the model
# load mental health data from a numpy array file
data = np.load('mental_health_data.npy')
X = data[:, :-1]  # input features
y = data[:, -1]  # target labels

# training the model on the loaded data
model.fit(X, y, epochs=50)  # train for 50 epochs

# saving the trained model for use in android app
tf.keras.models.save_model(model, 'mental_health_app_model')




