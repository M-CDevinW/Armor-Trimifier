import palette_creator
import resource_modifier
import datapack_modifier
import folder_clearer
import os
import shutil


def trimifier(trim_id, trim_ingredient, image_filepath, model_index = 0.101, enderscape_enabled = False):
    palette = palette_creator.paletter(f"{image_filepath}/{trim_id}.png")

    # print(f"Here in trimifier palette looks like {palette}")

    palette_creator.palette_dumper(trim_id = trim_id, palette = palette)
    datapack_modifier.generate_json(trim_id = trim_id, trim_ingredient = trim_ingredient, palette = palette, model_index = model_index)
    datapack_modifier.modify_tag(trim_ingredient = trim_ingredient)
    resource_modifier.modify_atlases(trim_id = trim_id, atlases = ["armor_trims", "blocks"])
    resource_modifier.add_translation_key(trim_id = trim_id)
    resource_modifier.create_model_json(trim_id = trim_id, enderscape_enabled = enderscape_enabled)
    resource_modifier.edit_model_json(trim_id = trim_id, trim_index = model_index, enderscape_enabled = enderscape_enabled)

def trimify_all(resource_pack_path, datapack_path, resource_destination, data_destination, enderscape_enabled = False):
    folder_clearer.clear_folders(resource_pack_path = resource_pack_path, datapack_path = datapack_path)
    model_index = 0.101
    for image in os.listdir("mass_trim_images_2"):
        trimifier(trim_id = image[:-4], trim_ingredient = f"minecraft:{image[:-4]}", image_filepath = "mass_trim_images_2", model_index = model_index, enderscape_enabled = enderscape_enabled)
        model_index = round(model_index + 0.001, 4)
        print(f"Model index is at {model_index}")
    zip_contents(resource_destination = resource_destination, datapack_destination = data_destination, resource_folder = resource_pack_path, data_folder = datapack_path)

def zip_contents(resource_folder: str, resource_destination: str, data_folder: str, datapack_destination: str):

    if not os.path.isdir(resource_folder):
        raise FileNotFoundError(f"Source folder not found: {resource_folder}")

    if not os.path.isdir(data_folder):
        raise FileNotFoundError(f"Source folder not found: {data_folder}")
    
    os.makedirs(os.path.dirname(resource_destination), exist_ok = True)
    
    os.makedirs(os.path.dirname(datapack_destination), exist_ok = True)

    resource_archive_path = shutil.make_archive(
        base_name = resource_destination,
        format = "zip",
        root_dir = resource_folder)

    data_archive_path = shutil.make_archive(
        base_name = datapack_destination,
        format = "zip",
        root_dir = data_folder)
    
    # print(f"Archive paths look like {resource_archive_path} and {data_archive_path}")
    
    return resource_archive_path, data_archive_path

def trimify_single(trim_id, trim_ingredient, resource_pack_destination, datapack_destination, image_filepath = "images", resource_pack_source = "Resource_Pack", datapack_source = "Datapack"):
    folder_clearer.clear_folders(resource_pack_path = resource_pack_source, datapack_path = datapack_source)
    trimifier(trim_id = trim_id, trim_ingredient = trim_ingredient, image_filepath = image_filepath)
    zip_contents(
        resource_folder = resource_pack_source,
        resource_destination = resource_pack_destination,
        data_folder = datapack_source,
        datapack_destination = datapack_destination
    )



# trimify_single(
#     trim_id = "auric_bar",
#     trim_ingredient = "minecraft:honeycomb",
#     resource_pack_destination = r"C:\Users\devin\curseforge\minecraft\Instances\Moderately Modded Server\resourcepacks\More Trims",
#     datapack_destination = r"C:\Users\devin\curseforge\minecraft\Instances\Moderately Modded Server\saves\Test\datapacks\More Trims",
#     # These areguments can be used if the folder structure of the user is different than the base project
#     # image_filepath = "images",
#     # resource_pack_source = "Resource_Pack",
#     # datapack_source = "Datapack"
#     )

# trimify_all(
#     data_destination = r"C:\Users\devin\curseforge\minecraft\Instances\Moderately Modded Server\saves\Test\datapacks\More Trims",
#     resource_destination = r"C:\Users\devin\curseforge\minecraft\Instances\Moderately Modded Server\resourcepacks\More Trims",
#     resource_pack_path = "Resource_Pack",
#     datapack_path = "Datapack",
#     enderscape_enabled = True
#     )

folder_clearer.clear_folders(datapack_path = "Datapack", resource_pack_path = "Resource_Pack")