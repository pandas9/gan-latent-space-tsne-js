# Used to calculate compatible values for creating latent space atlas

image_w = 60 # latent image width
image_h = 60 # latent image height
max_img_resolution = 2500 # max resolution per atlas
latent_size = 36000 # desired latent size

columns = int(max_img_resolution / image_h)
imgs_per_atlas = columns * columns
parts = int(latent_size / imgs_per_atlas)
compatible_latent_size = parts * imgs_per_atlas

print(
    f"Columns per atlas {columns},",
    f"Atlas Parts {parts},",
    f"Latent size {compatible_latent_size}"
)
