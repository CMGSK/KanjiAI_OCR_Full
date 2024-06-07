def is_pitch_black(img):
    pixels = img.getdata()  # get flattened array of pixels
    # Check whether a pixel is black (0) and if % of black pixels exceeds 80, return True as it IS pitch black.
    blacks = 0
    for p in pixels:
        if p != 0:
            blacks += 1
    total = len(pixels)
    return (blacks / float(total)) > 0.90


