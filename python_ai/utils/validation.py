import numpy as np
import tensorflow as tf
import pathlib
import os


dataset_dir = pathlib.Path('../dataset/Kanji_Images')

dataset_size = sum(len(os.listdir('dataset/Kanji_Images/' + direc + '/')) for direc in os.listdir('../dataset/Kanji_Images'))

batch_size = 32
source_height = 64
source_width = 64

training_dataset = tf.keras.utils.image_dataset_from_directory(
    directory=dataset_dir,
    validation_split=0.2,
    subset='training',
    seed=39,
    image_size=(source_height, source_width),
    batch_size=batch_size)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    directory=dataset_dir,
    validation_split=0.2,
    subset='validation',
    seed=39,
    image_size=(source_height, source_width),
    batch_size=batch_size)

model = tf.keras.models.load_model('../trained_models/fullmodel.keras')

labels = training_dataset.class_names

for guess in os.listdir('../example_images/'):
    image = tf.keras.utils.load_img(f'example_images/{guess}', target_size=(source_height, source_width))
    image_array = tf.keras.utils.img_to_array(image)
    image_array = tf.expand_dims(image_array, 0)

    prediction = model.predict(image_array)
    certainty = tf.nn.softmax(prediction[0])

    top_labels = np.argsort(certainty)[-5:][::-1]
    top_certainty = certainty.numpy()[top_labels]

    print(f'Best 5 matches for {guess}:')
    for i in range(5):
        label_idx = top_labels[i]
        label_name = labels[label_idx]
        confidence = 100 * top_certainty[i]
        print(f'Guess {i}: {chr(int(label_name[2:], 16))} with a {confidence}% confidence')
