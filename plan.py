"""
Parts of a custom trim definition:
1. The color palette png (8 pixel gradient/palette)
2. Additions to the armor_trims and blocks atlases
3. New trim material json
4. Add a translation key to the lang file
5. Addition to the trim_materials tag

Substeps:
0. Select a trim id. This id can be anything the user wants, but works best as the item name

1a. Find a texture and put it into the correct location
1b. Turn that image into a palette of all colors used in the image
1c. Find the 8 most used colors of the image and sort them into a line, lightest to darkest
1d. If there are fewer than 8 colors, create new colors between the largest gaps of the present colors
1e. If there are fewer than 4 colors, deny the image completely
1f. Save the color palette in the color_palettes folder under the trim id

2a. Import the armor_trims.json atlas
2b. Save all the current data in the atlas as reusable variabkes
2c. Add the color palette filepath to the permutations object
2d. Recompile the armor_trims.json atlas
2e. Dump the json back to it's correct folder
2f. Do steps 2a-2e again for the blocks.json atlas

3a. Ask the user for the trim ingredient
3b. Find the most representative color (most common one) and get its hex code
3c. Assemble the json object based on the provided information
3d. Dump the json to the trim_material datapack folder once assembled

4a. Format the trim id into a clean string (instead of "x_y", do "X Y")
4b. Create a translation key based on the trim id
4c. Import the current lang json as a dictionary
4d. Append the translation key to the dictionary and dump it to a json

5a. Import the current trim_materials json
5b. Add the trim ingredient id to the values list
5c. Recompile and dump the json to the tags folder
"""

"""
All of the above has been finished. Below is the list of updates to do:
1. Add a way for a user to define any number of trim ids and trim ingredients instead of all or singular generation options
"""

"""
Version 1.1 Changelog:
1. trim_id can now be anything, not just an item namespace
2. Fixed program failing if the image is too large
3. Fixed translation keys to have "Material" at the end
4. Added a WIP function that trimifies an entire folder of images
5. The trim materials tag no longer lists duplicate entires
6. Added a new function to main.py that packages the Resource and Datapacks into their respective folders when provided a proper filepath
7. Added functions to clear the resource pack folder, datapack folder, or both, reverting them to their base state
8. Made a new master function that can trimify an individual image, ending with zipped resource and datapacks in your game files
9. Verified modded namespaces generate properly
"""