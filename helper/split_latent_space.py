import os
import shutil
import glob

parts = 21 # calculate_latent_size.py
latent_size = 35301 # calculate_latent_size.py

def split(a, n):
    k, m = divmod(len(a), n)
    
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

latent_images = list(split(sorted(glob.glob('./latent_images/*'))[:latent_size], parts))
for ind, images in enumerate(latent_images):
    os.makedirs(f'./images_{ind}/', exist_ok=True)
    for img in images:
        shutil.copyfile(img, f'./images_{ind}/{os.path.basename(img)}')
