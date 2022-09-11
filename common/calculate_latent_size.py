# Used to calculate compatible values for creating latent space tiles

image_w = 60 # latent image width
image_h = 60 # latent image height
max_img_resolution = 2500 # max resolution per tile
latent_size = 36000 # desired latent size

columns = int(max_img_resolution / image_h)
imgs_per_tile = columns * columns
parts = int(latent_size / imgs_per_tile)
compatible_latent_size = parts * imgs_per_tile

print(
    f"Columns per tile {columns},",
    f"Tile Parts {parts},",
    f"Latent size {compatible_latent_size}"
)
