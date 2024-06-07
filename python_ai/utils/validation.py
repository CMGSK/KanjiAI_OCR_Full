import numpy as np
import tensorflow as tf
import pathlib
import os


dataset_dir = pathlib.Path('../dataset/Kanji_Images')  # Directory of the dataset

# Sum of all Kanji
dataset_size = sum(len(os.listdir('dataset/Kanji_Images/' + direc + '/')) for direc in os.listdir(
    '../dataset/Kanji_Images'))

batch_size = 32  # How many kanji will be analyzed per batch
source_height = 64  # Height pixels
source_width = 64  # Width pixels

# Creation of the dataset. Dataloader from Keras Utils
training_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_dir,  # Directory
    validation_split=0.2,  # the part you separate to test if you're training properly
    subset='training',  # Name of the subset
    seed=39,  # Sets a seed for the randomizer of the dataset
    image_size=(source_height, source_width),  # Size of the image
    batch_size=batch_size)  # Size of the batch

# Same process. Validation dataset
validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_dir,
    validation_split=0.2,
    subset='validation',
    seed=39,
    image_size=(source_height, source_width),
    batch_size=batch_size)


model = tf.keras.models.load_model('../trained_models/fullmodel.keras')  # Loading a pre-trained model.
# mtrx = []  # Validation matrix for a confusion matrix plot. Tad useless, not using it in the project.

for guess in os.listdir('../example_images/'):
    image = tf.keras.utils.load_img(f'example_images/{guess}', target_size=(source_height, source_width)) # Image load
    image_array = tf.keras.utils.img_to_array(image) # Transform image into an aray for the AI to analyze it
    image_array = tf.expand_dims(image_array, 0)  # Creates an empty batch with only my flattened image

    prediction = model.predict(image_array) # Call to the prediction method of the model.
    certainty = tf.nn.softmax(prediction[0]) # Returns the percentage of chance each label has to match the prediction
    # mtrx.append(certainty)  # Confusion matrix dataset

    top_labels = np.argsort(certainty)[-5:][::-1]  # Tf is this? Get last 5 then turn them around.
    top_certainty = certainty.numpy()[top_labels]  # Get the top 5 certainty predictions

    # Just print each name of predicted image with its correspondant 5 predictions
    print(f'Best 5 matches for {guess}:')
    for i in range(5):
        label_idx = top_labels[i]
        label_name = labels[label_idx]
        confidence = 100 * top_certainty[i]
        print(f'Guess {i}: {chr(int(label_name[2:], 16))} with a {confidence}% confidence')

# Confusion Matrix. Should be working provided imports are corrected. Not using it.
# cm = confusion_matrix(validation_dataset.class_names, mtrx)
# ConfusionMatrixDisplay.from_predictions(cm, validation_dataset.class_names, normalize=False)

# Data from the training dataset. Too big to plot it overflows 32Gb RAM.
# train = list(map(lambda i: i,training_dataset))
# xtrain = np.concatenate(list(map(lambda x: x[0], train)))
# ytrain = np.concatenate(list(map(lambda x: x[1], train)))

# Data from the validation dataset
# test = list(map(lambda i: i,validation_dataset)) # Lists the value from map of validation dataset
# xtest = np.concatenate(list(map(lambda x: x[0], test))) # Concatenates the list of images in test
# ytest = np.concatenate(list(map(lambda x: x[1], test)))  # Concatenates the list of labels in test
# ypred = model.predict(xtest) # Predicts xtest
# ypred = np.argmax(ypred, axis=1) # takes the prediction and compares it to the labels
# cm = confusion_matrix(y_true=ytest, y_pred=ypred) # Creates the confusion matrix
# plt.imshow(cm, vmax=cm.max(), vmin=0) # Defines the characteristics of the plot
# plt.show()
#
