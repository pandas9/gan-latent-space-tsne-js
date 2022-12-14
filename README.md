<h1 align="center">GAN Latent Space Web Explorer w/ t-SNE Visualization</h1>

[![gan-latent-space-web-explorer](examples/index.png?raw=true)](https://pandas9.github.io/gan-latent-space-tsne-js/)

Robust way to explore GAN model latent space on web using t-SNE statistical method <br />
[GAN explorer example](https://pandas9.github.io/gan-latent-space-tsne-js/) <br />

This is example on how you can create latent space web explorer for any GAN model using js and python <br />
Example is based on three.js library, t-SNE statistical method and vanilla js <br />

t-SNE allows us to position images near other similar-looking images in the 2D coordinate space and three.js library to build a WebGL-powered visualization that can display tens of thousands of images in an interactive 3D environment <br />

Inside examples folder there is `celeba_gan_e30.h5` that has been trained on celeba dataset in case someone wants to try and build custom GAN explorer but doesn't have machines to train model <br />

# Run Locally
1. clone github project and set `githubPages` to `false` inside `main.js` <br />
2. `npm install` <br />
command inside project root folder <br />
3. `node app.js` <br />
serve app using node <br />

# Build Gan Explorer For Your Model
1. Clone the project and run calculate_latent_size.py and set variables inside file that will fit your model this is important for atlases and how your latent space is visualized with three.js <br />
`python calculate_latent_size.py`<br />

2. Using your GAN model generate latent points and save each as image i.e <br />
<pre>
# example.py

def generate_images(examples, n):
	for i in range(n):
		pyplot.imsave(f'./faces/generated_face_{i}.png', examples[i, :, :])

model = load_model('celeba_gan_e30.h5')
n = 35301
latent_points = generate_latent_points(100, n)
X  = model.predict(latent_points)
X = (X + 1) / 2.0
generate_images(X, n)
</pre>

3. Use classify_images.py to create vectorized representation of each image <br />
`python classify_images.py 'faces/*'` <br />

4. Run create_tsne_projection.py to get t-SNE coordinates <br />
`python create_tsne_projection.py`<br />
inside file make sure to change latent_size and other variables same goes for other files below <br />

5. Split latent space images into equal parts for atlas <br />
`python split_latent_space.py` <br />

6. Generate atlases and serve the app <br />
`python create_atlases.py` <br /> <br />
by now you should have `image_tsne_projections.json` and `images_..jpg` those are your atlases next is to create new folder inside `/src/assets/` and copy generated files inside, create new config `config.js` inside `/src/` folder that will fit your model and add inside `main.js` - `index.html` option to have your config selectable inside web page <br /> <br />
serve app using node `node app.js` and visit `localhost:3000` to explore your GAN latent space <br />

# Requirements
python3 <br />
node.js <br />
imagemagick <br />


# To do
- Port to React.js <br />
- Convert classify_images.py to tf2 and have script only create vectorized representations of each image <br />
- Add 3D visualization <br />
- Allow objects to be interactive for interpolation / zoom / vector arithmetic ... etc <br />
- Dynamic atlas size <br />
- Indication of load progress <br />
- Guide through the visualization <br />

# Acknowledgements
[machinelearningmastery.com/how-to-interpolate-and-perform-vector-arithmetic-with-faces-using-a-generative-adversarial-network/](https://machinelearningmastery.com/how-to-interpolate-and-perform-vector-arithmetic-with-faces-using-a-generative-adversarial-network/) <br />
[medium.com/mlearning-ai/latent-space-representation-a-hands-on-tutorial-on-autoencoders-in-tensorflow](https://medium.com/mlearning-ai/latent-space-representation-a-hands-on-tutorial-on-autoencoders-in-tensorflow-57735a1c0f3f) <br />
[douglasduhaime.com/posts/visualizing-tsne-maps-with-three-js](https://douglasduhaime.com/posts/visualizing-tsne-maps-with-three-js.html) <br />
[github.com/YaleDHLab/pix-plot](https://github.com/YaleDHLab/pix-plot) <br />
[artsexperiments.withgoogle.com/tsnemap](https://artsexperiments.withgoogle.com/tsnemap/) <br />
[towardsdatascience.com/understanding-latent-space-in-machine-learning-de5a7c687d8d](https://towardsdatascience.com/understanding-latent-space-in-machine-learning-de5a7c687d8d) <br />
