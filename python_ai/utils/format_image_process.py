from PIL import ImageOps, ImageFilter, Image
import numpy as np
from utils import image_utils

# Trigger debugging control actions to check behaviour locally
debug = False


def modify(img):
    img.load()
    img = img.convert('L')  # Convert to BnW

    # BnW clipping contrast
    clip = np.array(img)
    # Scale pixels from its range to luminosity channel range
    img = ((clip - clip.min()) * 255.0 / (clip.max() - clip.min())).astype(np.uint8)
    img = Image.fromarray(img)

    # Posterization
    threshold = 150  # Threshold for posterization
    imgpos = img.point(lambda e: 255 if e > threshold else 0)  # Posterize based on luminosity (trial and error number)
    # If the image is too dark we gotta increase the threshold to get a clear kanji
    while image_utils.is_pitch_black(imgpos):
        threshold += 3
        imgpos = img.point(lambda e: 255 if e > threshold else 0)

    img = imgpos.filter(ImageFilter.GaussianBlur(1))  # Antialiasing
    img = img.resize((64, 64), resample=4)  # resize into 64x64

    # If the corner pixels are white, we have to invert it so kanji is white instead. Otherwise, just let it be.
    # This will trigger a RuntimeWarning. Do not mind, it cannot overflow.
    corners = np.array(img)
    r = corners[0, 0] + corners[63, 0] + corners[0, 63] + corners[63, 63]
    if r != 0:
        img = ImageOps.invert(img)
    if debug:
        img.show()
    return img.convert('RGB')  # Convert it to RGB since AI expects 3 channels


if debug:
    modify(Image.open('../example_images/test.jpg'))
