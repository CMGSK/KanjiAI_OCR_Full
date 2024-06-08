def is_pitch_black(img):
    pixels = img.getdata()
    blacks = 0
    for p in pixels:
        if p != 0:
            blacks += 1
    total = len(pixels)
    return (blacks / float(total)) > 0.90


