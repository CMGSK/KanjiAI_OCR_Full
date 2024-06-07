import os
import random
import shutil
from os import path, mkdir
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm
import tensorflow as tf
from kanji_lists import JLPT
import random
import io
from PIL import Image
import numpy as np
from timeit import default_timer as timer


def cleanup():
    d = '../dataset/Kanji_Images/'
    for dir in os.listdir(d):
        if len(os.listdir(d + dir)) < 3:
            shutil.rmtree(d + dir)


def keep_dir_structures():
    for dir in os.listdir('../dataset/Kanji_Images/'):
        if not '.gitkeep' in os.listdir(f'../dataset/Kanji_Images/{dir}/'):
            f = open(f'../dataset/Kanji_Images/{dir}/.gitkeep', 'x')
            f.close()


def clear_gitkeep():
    for dir in os.listdir('../dataset/Kanji_Images/'):
        if '.gitkeep' in os.listdir(f'../dataset/Kanji_Images/{dir}/'):
            os.remove(f'../dataset/Kanji_Images/{dir}/.gitkeep')


def save_labels():
    l = os.listdir('../dataset/Kanji_Images/')
    np.save('../dataset/labels.npy', np.array(l))


def feed_dataset():
    t = timer()
    for f, font in enumerate(os.listdir('../kanji_fonts/')):
        current_font = mfm.FontProperties(fname=f'../kanji_fonts/{font}')
        for k, kanji in enumerate(JLPT.TANOS):
            buf = io.BytesIO()

            plt.figure(figsize=(64 / 100, 64 / 100))
            plt.text(x=0.0,
                     y=0.0,
                     s=kanji,
                     ha='left',
                     va='bottom',
                     fontproperties=current_font,
                     size=48)

            plt.xlim((0.05, 0.3))
            plt.ylim((0.05, 0.4))
            plt.tight_layout()

            plt.axis('off')
            plt.savefig(buf, format='png')
            buf.seek(0)
            x = plt.imread(buf)

            if Image.fromarray(((1 - x[:, :, 0]) * 255).astype(np.uint8)).getbbox():
                dest = f'../dataset/Kanji_Images/U+{hex(ord(kanji))[2:].upper()}'
                if not path.isdir(dest):
                    mkdir(dest)
                Image.fromarray(((1 - x[:, :, 0]) * 255).astype(np.uint8)).save(
                    f'{dest}/U+{hex(ord(kanji))[2:]}_{font[:-4]}.png')
            plt.close()

            if k % 100 == 0 or k == 2211:
                print(f'{k}/{f + 1} - [2211/7] - Time: {timer() - t}')
    print('Total time: ' + str(timer() - t))


def normalization(target: int, sh: int, sw: int):
    dir = '../dataset/test'
    for utf in os.listdir(dir):
        cnt = 0
        maxrnd = len(content := os.listdir(f'{dir}/{utf}/'))
        while len(os.listdir(f'{dir}/{utf}/')) < target:
            with Image.open(f'{dir}/{utf}/{content[random.randint(0, maxrnd-1)]}') as img:
                img = img.resize((sw+random.randint(-5,  5), sh+random.randint(-5, 5)))
                img = img.rotate(random.randint(-20, 20))

                n_sw, n_sh = img.size
                left = max(0, ((n_sw - sw) - sw) // 2)
                top = max(0, ((n_sh - sh) - sh) // 2)
                right = min(n_sw, (left + sw))
                bottom = min(n_sh, (top + sh))

                augmented_img = img.crop((top, left, right, bottom))
                if augmented_img.size != (sw, sh):
                    augmented_img = augmented_img.resize((sw, sh))
                augmented_img.save(f"{dir}/{utf}/augmented_{cnt}.png")
                cnt+=1
            continue


def get_rnd(dataset_dir, path: str, target: int):
    rel = f'{dataset_dir}/{path}'
    try:
        s = os.listdir(rel)
        if '.gitkeep' in s:
            s.remove('.gitkeep')
        if len(s) >= target:
            return random.sample(s, target)
        else:
            return random.choices(s, k=target)
    finally:
        open(f'{rel}/.gitkeep', 'a')


def load_img(img: str, source_width: int, source_height: int):
    image = tf.io.read_file(img)
    tensor = tf.image.decode_png(image, channels=1)
    tensor = tf.image.resize(tensor, [source_width, source_height])
    tensor = tf.cast(tensor, tf.float32) / 255.0
    return tensor


def create_dataset(imgs, labs, sw: int, sh: int):
    # pair = [[load_img(f'../dataset/Kanji_Images/{l}/{i}', sw, sh), idx] for idx, l in enumerate(labs) for i in imgs[idx]]
    pair = [[load_img(f'../dataset/Kanji_Images/{l}/{i}', sw, sh), idx] for idx, l in enumerate(labs) for i in imgs[idx]]

    # semen = (list(map(lambda x: x[0], pair)), list(map(lambda x: x[1], pair)))
    dataset = tf.data.Dataset.from_tensor_slices((list(map(lambda x: x[0], pair)), list(map(lambda x: x[1], pair))))

    # for e in dataset.as_numpy_iterator():
    #     semen = e[0].reshape(64, 64)
    #     plt.imshow(semen)
    #     plt.show()
    #     print(labs[e[1]])

    return dataset

normalization(100, 64, 64)