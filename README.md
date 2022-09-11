<h1 align="center">GAN Latent Space Web Explorer w/ t-SNE Visualization</h1>

[![gan-latent-space-web-explorer](examples/index.png?raw=true)](https://www.google.com)

Robust way to explore GAN model latent space on web using t-SNE statistical method <br />
[View GAN Explorer](https://pages.github.com/) <br />

This is example on how you can create latent space web explorer for any GAN model using js and python <br />
Example is based on three.js library, t-SNE statistical method and vanilla js <br />

t-SNE allows us to position images near other similar-looking images in the 2D coordinate space and three.js library to build a WebGL-powered visualization that can display tens of thousands of images in an interactive 3D environment

# Run Locally
1. clone github project <br />
2. `npm install` <br />
command inside project root folder <br />
3. `node app.js` <br />
serve app using node <br />

# Custom Gan Explorer
1. Using your GAN model generate images and save them i.e
`# create a plot of generated images
def generate_images(examples, n):
	# plot images
	for i in range(n):
		pyplot.imsave(f'./faces/generated_face_{i}.png', examples[i, :, :])

# load model
model = load_model('latest_celeba_gan.h5')
# generate points in latent space
n = 35301
latent_points = generate_latent_points(100, n)
# save points
savez_compressed('latent_points.npz', latent_points)
# generate images
X  = model.predict(latent_points)
# scale from [-1,1] to [0,1]
X = (X + 1) / 2.0
# save plot
generate_images(X, n)` 

# Requirements
python3 <br />
node.js <br />
imagemagick <br />


# To do
- Port to React.js <br />
- Convert classify_images.py to tf2 and have script only create vectorized representations of each image <br />
- Add 3D visualization <br />
- Allow objects to be interactive for interpolation / zoom / vector arithmetic ... etc <br />
- Dynamic atlas/tile size <br />
- Indication of load progress <br />
- Guide through the visualization <br />

# Acknowledgements
[machinelearningmastery.com/how-to-interpolate-and-perform-vector-arithmetic-with-faces-using-a-generative-adversarial-network/](https://machinelearningmastery.com/how-to-interpolate-and-perform-vector-arithmetic-with-faces-using-a-generative-adversarial-network/) <br />
[medium.com/mlearning-ai/latent-space-representation-a-hands-on-tutorial-on-autoencoders-in-tensorflow](https://medium.com/mlearning-ai/latent-space-representation-a-hands-on-tutorial-on-autoencoders-in-tensorflow-57735a1c0f3f) <br />
[douglasduhaime.com/posts/visualizing-tsne-maps-with-three-js](https://douglasduhaime.com/posts/visualizing-tsne-maps-with-three-js.html) <br />
[github.com/YaleDHLab/pix-plot](https://github.com/YaleDHLab/pix-plot) <br />
[artsexperiments.withgoogle.com/tsnemap](https://artsexperiments.withgoogle.com/tsnemap/) <br />
