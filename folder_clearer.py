import os
import shutil

def clear_resources(filepath):

    # print(os.getcwd())
    # print(f"Filepath provided is {filepath}")
    # print(f"The directories in the provided filepath are {os.listdir(filepath)}")
    # color_palettes_folder = os.listdir(rf"{filepath}\assets\minecraft\textures\trims\color_palettes")
    # print(f"The directories in the color palettes folder are {color_palettes_folder}")

    # Remove color palette textures
    for file in os.listdir(rf"{filepath}\assets\more_trims\textures\trims\color_palettes"):
        full_path = rf"{filepath}\assets\more_trims\textures\trims\color_palettes"
        # print(f"File is {file}")
        os.remove(path = rf"{full_path}\{file}")

    # Remove model json definitions
    for file in os.listdir(rf"{filepath}\assets\more_trims\models\item"):
        full_path = rf"{filepath}\assets\more_trims\models\item"
        os.remove(path = rf"{full_path}\{file}")
    
    # Revert atlases to originals
    for file in os.listdir(rf"{filepath}\assets\minecraft\atlases"):
        # print(f"File looks like {file}")
        shutil.copyfile(src = rf"Skeleton_Resource_Pack\assets\minecraft\atlases\{file}", dst = rf"{filepath}\assets\minecraft\atlases\{file}")

    # Revert model jsons to originals
    for file in os.listdir(rf"{filepath}\assets\minecraft\models\item"):
        shutil.copyfile(src = rf"Skeleton_Resource_Pack\assets\minecraft\models\item\{file}", dst = rf"{filepath}\assets\minecraft\models\item\{file}")

    # Revert drift leggings json
    shutil.copyfile(src = rf"Skeleton_Resource_Pack\assets\enderscape\models\item\drift_leggings.json", dst = rf"{filepath}\assets\enderscape\models\item\drift_leggings.json")

    # Reverts lang file to original state
    shutil.copyfile(src = rf"Skeleton_Resource_Pack\assets\more_trims\lang\en_us.json", dst = rf"{filepath}\assets\more_trims\lang\en_us.json")

def clear_data(filepath):

    # Remove all json definitions
    for file in os.listdir(rf"{filepath}\data\more_trims\trim_material"):
        full_path = rf"{filepath}\data\more_trims\trim_material"
        os.remove(path = rf"{full_path}\{file}")

    # Reset tag
    shutil.copyfile(src = rf"Skeleton_Datapack\data\minecraft\tags\item\trim_materials.json", dst = rf"{filepath}\data\minecraft\tags\item\trim_materials.json")

def clear_folders(datapack_path, resource_pack_path):
    clear_resources(resource_pack_path)
    clear_data(datapack_path)