import os
import glob

latent_size = 35301
parts = 21
columns = 41

os.makedirs(f'./tiles/', exist_ok=True)

for part in range(0, parts):
    if os.path.exists('./images_to_montage.txt'):
        os.remove('./images_to_montage.txt')
    for img in sorted(glob.glob(f'./images_{part}/*'))[:latent_size]:
        with open('./images_to_montage.txt', 'a') as f:
            f.write(img + '\n')

    #!montage `cat images_to_montage.txt` -geometry +0+0 -background none -tile 31x images_0.jpg
    os.system(f'montage `cat images_to_montage.txt` -geometry +0+0 -background none -tile {columns}x ./tiles/images_{part}.jpg')
