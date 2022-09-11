import os
import glob

latent_size = 35301 # calculate_latent_size.py
parts = 21 # calculate_latent_size.py
columns = 41 # calculate_latent_size.py

os.makedirs(f'./atlas/', exist_ok=True)

for part in range(0, parts):
    if os.path.exists('./images_to_montage.txt'):
        os.remove('./images_to_montage.txt')
    for img in sorted(glob.glob(f'./images_{part}/*'))[:latent_size]:
        with open('./images_to_montage.txt', 'a') as f:
            f.write(img + '\n')

    #!montage `cat images_to_montage.txt` -geometry +0+0 -background none -tile 31x images_0.jpg
    os.system(f'montage `cat images_to_montage.txt` -geometry +0+0 -background none -tile {columns}x ./atlas/images_{part}.jpg')
