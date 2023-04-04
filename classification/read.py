import matplotlib.pyplot as plt
from PIL import Image

# Load the image
img = Image.open('/content/saturn-bone-tru-stone-16x16-ceramic.jpg')

width, height = img.size
tile_size = 600

#calculate the size of the tile, for each dimension
num_tiles_x = (width + tile_size -1) // tile_size
num_tiles_y = (height + tile_size -1) // tile_size

#calculate the number of tiles
num_tiles  = num_tiles_x*num_tiles_y
print("Number of tiles: ", num_tiles)
# Display the image
plt.imshow(img)
plt.show()