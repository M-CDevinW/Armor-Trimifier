import palette_creator
import resource_modifier
import datapack_modifier


def trimifier(trim_id, trim_ingredient):
    palette = palette_creator.paletter(f"images/{trim_id}.png")
    palette_creator.palette_dumper(trim_id = trim_id, palette = palette)
    resource_modifier.modify_atlases(trim_id = trim_id, atlases = ["armor_trims", "blocks"])
    datapack_modifier.generate_json(trim_id = trim_id, trim_ingredient = trim_ingredient, palette = palette)
    resource_modifier.add_translation_key(trim_id = trim_id)
    datapack_modifier.modify_tag(trim_ingredient = trim_ingredient)


trimifier(trim_id = "blaze_rod", trim_ingredient = f"minecraft:blaze_rod")