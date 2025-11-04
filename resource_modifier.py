import os
import json

def json_importer(atlas):
    with open(f"Resource_Pack/assets/minecraft/atlases/{atlas}.json", "r") as file:
        data = json.load(file)

    # print(type(data))
    return data

def add_permutation(data, trim_id):
    # print(data["sources"][-1]["permutations"])
    data["sources"][-1]["permutations"][f"{trim_id}"] = f"trims/color_palettes/{trim_id}"
    return data

def dump_json(data, atlas):
    with open(f"Resource_Pack/assets/minecraft/atlases/{atlas}.json", "w") as fp:
        json.dump(data, fp, indent = 4)
    # print(f"Dumped json to {atlas}")


def modify_atlas(trim_id, atlas):
    armor_trims = json_importer(atlas = "armor_trims")
    armor_trims = add_permutation(armor_trims, trim_id)
    dump_json(data = armor_trims, atlas = "armor_trims")

def modify_atlases(trim_id, atlases):
    for atlas in atlases:
        data = json_importer(atlas = atlas)
        data = add_permutation(data, trim_id)
        dump_json(data = data, atlas = atlas)

def add_translation_key(trim_id):
    with open(f"Resource_Pack/assets/more_trims/lang/en_us.json", "r") as file:
        data = json.load(file)

    translation_key = f"trim_material.minecraft.{trim_id}"
    capitilized_string = str.title(trim_id)
    finished_string = capitilized_string.replace("_", " ")
    data[translation_key] = finished_string

    with open(f"Resource_Pack/assets/more_trims/lang/en_us.json", "w") as fp:
        json.dump(data, fp, indent = 4)