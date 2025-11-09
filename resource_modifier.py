import os
import json

def json_importer(atlas):
    with open(f"Resource_Pack/assets/minecraft/atlases/{atlas}.json", "r") as file:
        data = json.load(file)

    # print(type(data))
    return data

def add_permutation(data, trim_id):
    # print(data["sources"][-1]["permutations"])
    data["sources"][-1]["permutations"][f"{trim_id}"] = f"more_trims:trims/color_palettes/{trim_id}"
    return data

def dump_json(data, atlas):
    with open(f"Resource_Pack/assets/minecraft/atlases/{atlas}.json", "w") as fp:
        json.dump(data, fp, indent = 4)
    # print(f"Dumped json to {atlas}")

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
    spaced_string = capitilized_string.replace("_", " ")
    finished_string = spaced_string + " Material"
    data[translation_key] = finished_string

    with open(f"Resource_Pack/assets/more_trims/lang/en_us.json", "w") as fp:
        json.dump(data, fp, indent = 4)

def create_model_json(trim_id, materials: list = ["diamond", "netherite", "iron", "gold", "leather", "chainmail"], enderscape_enabled = False):
    materials_list = materials
    slots = ["helmet", "chestplate", "leggings", 'boots']

    # Add code to account for turtle shell in particular

    model_json = {}
    model_json["parent"] = "minecraft:item/generated"
    textures = {}
    textures["layer0"] = f"minecraft:item/turtle_helmet"
    textures["layer1"] = f"minecraft:trims/items/helmet_trim_{trim_id}"
    model_json["textures"] = textures

    with open(f"Resource_Pack/assets/more_trims/models/item/turtle_helmet_{trim_id}_trim.json", "w") as fp:
        json.dump(model_json, fp, indent = 4)

    if enderscape_enabled:
        model_json = {}
        model_json["parent"] = "minecraft:item/generated"
        textures = {}
        textures["layer0"] = f"enderscape:item/drift_leggings"
        textures["layer1"] = f"minecraft:trims/items/leggings_trim_{trim_id}"
        model_json["textures"] = textures

        with open(f"Resource_Pack/assets/more_trims/models/item/drift_leggings_{trim_id}_trim.json", "w") as fp:
            json.dump(model_json, fp, indent = 4)

    for material in materials_list:
        for slot in slots:
            model_json = {}
            model_json["parent"] = "minecraft:item/generated"
            textures = {}
            textures["layer0"] = f"minecraft:item/{material}_{slot}"
            textures["layer1"] = f"minecraft:trims/items/{slot}_trim_{trim_id}"
            model_json["textures"] = textures

            with open(f"Resource_Pack/assets/more_trims/models/item/{material}_{slot}_{trim_id}_trim.json", "w") as fp:
                json.dump(model_json, fp, indent = 4)

def edit_model_json(trim_id, trim_index, materials: list = ["diamond", "netherite", "iron", "golden", "leather", "chainmail"], enderscape_enabled = False):
    materials_list = materials
    slots = ["helmet", "chestplate", "leggings", "boots"]

    # Add code to account for turtle shell later

    with open(f"Resource_Pack/assets/minecraft/models/item/turtle_helmet.json", "r") as file:
        data = json.load(file)

    overrides = data["overrides"]
    model_object = {}
    model_object["model"] = f"more_trims:item/turtle_helmet_{trim_id}_trim"
    model_object["predicate"] = {"trim_type": trim_index}
    overrides.append(model_object)
    data["overrides"] = overrides

    with open(f"Resource_Pack/assets/minecraft/models/item/turtle_helmet.json", "w") as fp:
        json.dump(data, fp, indent = 4)

    if enderscape_enabled:
        with open(f"Resource_Pack/assets/enderscape/models/item/drift_leggings.json", "r") as file:
            data = json.load(file)

        overrides = data["overrides"]
        model_object = {}
        model_object["model"] = f"more_trims:item/drift_leggings_{trim_id}_trim"
        model_object["predicate"] = {"trim_type": trim_index}
        overrides.append(model_object)
        data["overrides"] = overrides

        with open(f"Resource_Pack/assets/enderscape/models/item/drift_leggings.json", "w") as fp:
            json.dump(data, fp, indent = 4)

    for material in materials_list:
        for slot in slots:
            # Open json
            with open(f"Resource_Pack/assets/minecraft/models/item/{material}_{slot}.json", "r") as file:
                data = json.load(file)

            overrides = data["overrides"]
            model_object = {}
            model_object["model"] = f"more_trims:item/{material}_{slot}_{trim_id}_trim"
            model_object["predicate"] = {"trim_type": trim_index}
            overrides.append(model_object)
            data["overrides"] = overrides

            # print(f"Overrides looks like {overrides}")

            # print(f"Data looks like {data}")

            with open(f"Resource_Pack/assets/minecraft/models/item/{material}_{slot}.json", "w") as fp:
                json.dump(data, fp, indent = 4)