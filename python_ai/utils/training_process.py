import matplotlib.pyplot as plt
import tensorflow as tf
import pathlib
import os
import numpy as np
from tensorflow import keras
from keras import layers
from keras.models import Sequential
import time
import training_utils as util


dataset_dir = pathlib.Path('../dataset/Kanji_Images')
sample_upper_limit = 500
sample_lower_limit = 80
source_height = 64
source_width = 64
batch_size = 256
epochs = 50

util.feed_dataset()
util.clear_gitkeep()
util.cleanup()

l = os.listdir('../dataset/Kanji_Images')
np.save('../dataset/labels.npy', np.array(l))

util.dataset_normalization(sample_lower_limit, sample_upper_limit, source_height, source_width)
dataset_size = sum(len(os.listdir(f'../dataset/Kanji_Images/{directory}/')) for directory in os.listdir('../dataset/Kanji_Images'))

training_dataset = tf.keras.utils.image_dataset_from_directory (
    dataset_dir=dataset_dir,
    validation_split=0.1,
    subset='training',
    seed=39,
    image_size=(source_height, source_width),
    batch_size=batch_size
)

validation_dataset = tf.keras.utils.image_dataset_from_directory (
    dataset_dir=dataset_dir,
    validation_split=0.1,
    subset='validation',
    seed=39,
    image_size=(source_height, source_width),
    batch_size=batch_size
)

labels = training_dataset.class_names

model = Sequential([
    tf.keras.Sequential([
        layers.Resizing(64,64),
        layers.Rescaling(1./255)
    ]),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(len(labels), name='outputs')
])

optimizer_model = keras.optimizers.Adam(learning_rate=0.0005)
loss_model = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer=optimizer_model,
              loss=loss_model,
              metrics=['accuracy'])

training = model.fit(training_dataset,
                     validation_data=validation_dataset,
                     epochs=epochs)
model.save(f'../trained_models/fullmodel_{round(time.time() * 1000)}.keras')

accuracy = training.history['accuracy']
acc_value = training.history['val_accuracy']

loss = training.history['loss']
loss_value = training.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(range(epochs), accuracy, label='Training Accuracy')
plt.plot(range(epochs), acc_value, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(range(epochs), loss, label='Training Loss')
plt.plot(range(epochs), loss_value, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
