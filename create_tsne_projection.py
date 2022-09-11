from sklearn.manifold import TSNE
import numpy as np
import glob
import json
import os

# create datastores
image_vectors = []
chart_data = []
latent_size = 35301

# build a list of image vectors
vector_files = sorted(glob.glob('./image_vectors/*.npz')
                      )[:latent_size]  # [:maximum_imgs]
for c, i in enumerate(vector_files):
    image_vectors.append(np.loadtxt(i))
    print(' * loaded', c+1, 'of', len(vector_files), 'image vectors')

# build the tsne model on the image vectors
model = TSNE(n_components=2, random_state=9)
np.set_printoptions(suppress=True)
fit_model = model.fit_transform(np.array(image_vectors))

# store the coordinates of each image in the chart data
for c, i in enumerate(fit_model):
    chart_data.append({
        'x': float(i[0]),
        'y': float(i[1]),
        'idx': c
    })

with open('image_tsne_projections.json', 'w') as out:
    json.dump(chart_data, out)
