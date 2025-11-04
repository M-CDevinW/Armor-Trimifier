import json



def rgb_to_hex(r, g, b):
  return "#{:02x}{:02x}{:02x}".format(r, g, b)

def find_leading_color(palette):
    palette = sorted(palette, key = lambda x: x[1], reverse = True)

    # print(f"The palette sorted by frequency looks like {palette}")

    (r, g, b), freq = palette[0]

    hex_code = rgb_to_hex(r, g, b)

    # print(f"The hex code of {palette[0]} is {hex_code}")

    return hex_code

def generate_json(trim_id, trim_ingredient, palette):
    
    description_object = {}
    description_object["translate"] = f"trim_material.minecraft.{trim_id}"
    description_object["color"] = find_leading_color(palette)

    trim_json = {}
    trim_json["asset_name"] = trim_id
    trim_json["description"] = description_object
    trim_json["ingredient"] = trim_ingredient
    trim_json["item_model_index"] = 1

    with open(f"Datapack/data/more_trims/trim_material/{trim_id}.json", "w") as fp:
        json.dump(trim_json, fp, indent = 4)

    # print(trim_json)

def modify_tag(trim_ingredient):
    with open(f"Datapack/data/minecraft/tags/item/trim_materials.json", "r") as file:
        data = json.load(file)

    data["values"].append(f"{trim_ingredient}")

    with open(f"Datapack/data/minecraft/tags/item/trim_materials.json", "w") as fp:
        json.dump(data, fp, indent = 4)