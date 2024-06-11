import io
import numpy as np
import tensorflow as tf
from PIL import Image
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from utils import format_image_process as fip
model = tf.keras.models.load_model('./trained_models/fullmodel.keras')
labels = np.load('./dataset/labels.npy')

app = FastAPI()


@app.post('/')
async def predict(file: UploadFile):
    image = Image.open(io.BytesIO(file.file.read()))
    image = fip.modify(image)
    image_array = tf.keras.utils.img_to_array(image)

    image_array = tf.expand_dims(image_array, 0)

    prediction = model.predict(image_array)
    certainty = tf.nn.softmax(prediction[0])

    top_labels = np.argsort(certainty)[-5:][::-1]
    top_certainty = certainty.numpy()[top_labels]

    print(f'Best 5 matches:')
    result = []
    for i in range(5):
        d = {}
        label_idx = top_labels[i]
        label_name = labels[label_idx]
        confidence = 100 * top_certainty[i]
        d["character"] = chr(int(label_name[2:], 16))
        d["confidence"] = confidence
        print(f'Guess {i + 1}: {chr(int(label_name[2:], 16))} with a {confidence:02.2f}% confidence')
        result.append(d)
    result = {"result": result}
    return JSONResponse(content=result, media_type='application/json charset=utf-8')
