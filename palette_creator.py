import numpy as np
import json
from PIL import Image
from sklearn.cluster import KMeans


def paletter(image_path):
    image = Image.open(image_path).convert("RGB")
    image_data = np.array(image)
    pixels = image_data.reshape(-1, 3)

    # Cluster Colors
    kmeans = KMeans(n_clusters = 9, n_init = "auto")
    kmeans.fit(pixels)

    # Get dominant colors
    colors = np.round(kmeans.cluster_centers_).astype(int)
    labels, counts = np.unique(kmeans.labels_, return_counts = True)
    total = sum(counts)

    # Combine into colors list
    palette = [(tuple(color), count / total) for color, count in zip(colors, counts)]
    palette = [((int(c[0]), int(c[1]), int(c[2])), float(ratio)) for c, ratio in palette]
    return palette

def perceived_brightness(color):
    (r,g,b), _ = color
    brightness = (0.2126*r + 0.7152*g + 0.0722*b)
    return brightness

def brightness_sorter(palette):
    brightness_palette = []
    for color in palette:
        brightness = perceived_brightness(color)
        (r,g,b), freq = color
        new_color = (r,g,b), freq, brightness
        brightness_palette.append(new_color)

    # print(f"The unsorted palette looks like {brightness_palette}")
    brightness_palette = sorted(brightness_palette, key = lambda x: x[2], reverse = True)

    # print(f"The sorted palette looks like {brightness_palette}")

    return brightness_palette

def pngifier(palette, trim_id):
    file_path = f"Resource_Pack/assets/minecraft/textures/trims/color_palettes/{trim_id}.png"

    # Create image with a row and 8 columns
    image = Image.new("RGB", (8, 1))
    
    # Create pixel data from palette colors
    pixels = [color for color, _, _ in palette]
    
    # Fill the image pixel by pixel instead of using putdata
    for x in range(min(8, len(pixels))):
        if x < len(pixels):
            image.putpixel((x, 0), pixels[x])
    
    image.save(file_path)
    # print(f"Palette saved at {file_path}")

def palette_dumper(trim_id, palette):

    # print(f"Pre-filter palette looks like {palette} with length {len(palette)}")

    for color in palette[:]:
        (r,g,b), freq = color
        # print(f"The rgb values of {color} are {r}, {g}, and {b} with frequency of {freq}")
        if (r <= 5 and g <= 5 and b <= 5) or (r >= 250 and g >= 250 and b >= 250):
            palette.remove(color)

    # print(f"Post-filter palette looks like {palette} with length {len(palette)}")

    sorted_palette = brightness_sorter(palette)

    pngifier(sorted_palette, trim_id)