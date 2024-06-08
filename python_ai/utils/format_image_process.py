from PIL import ImageOps, ImageFilter, Image
import numpy as np
from utils import image_utils


def modify(img):
    img.load()
    img = img.convert('L')

    clip = np.array(img)
    img = ((clip - clip.min()) * 255.0 / (clip.max() - clip.min())).astype(np.uint8)
    img = Image.fromarray(img)

    threshold = 150
    imgpos = img.point(lambda e: 255 if e > threshold else 0)
    while image_utils.is_pitch_black(imgpos):
        threshold += 3
        imgpos = img.point(lambda e: 255 if e > threshold else 0)

    img = imgpos.filter(ImageFilter.GaussianBlur(1))
    img = img.resize((64, 64), resample=4)

    corners = np.array(img)
    r = corners[0, 0] + corners[63, 0] + corners[0, 63] + corners[63, 63]
    if r != 0:
        img = ImageOps.invert(img)
    return img.convert('RGB')

