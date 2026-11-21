from __future__ import annotations
from typing import NamedTuple
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import AceCombat8World

class AceCombat8ItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


item_table: dict[str, AceCombat8ItemData] = {
    "M1: Jokers Wild, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M2: Nomad, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M3: Purple Magic Takes Flight, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M4: The Fall of the Numbered Fleets, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M5: Retaking of Theve, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M6: Attack on the Drinwich Airfield, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M7: A Lifeline in the Desert, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M8: Retaking of Theve II, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M9: The Land Battleship Blockade, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M10: Over the Rainband, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M11: Maximum Payload, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M12: An Island in Darkness, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M13: The People of the Lost Country, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M14: Two on the Run, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M15: Wings of Wax, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M16: Singer, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M17: Land Battleship No. 3, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M18: Moonlight and Shadows, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M19: Clearing the Lighthouse, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M20: Escort Orbiter, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M21: The Star-Bound Bird, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M22: Pursuing the HSCA, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M23: The Destruction of Expo City, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M24: The Battle of Rocky Island, Day 1, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M25: The Battle of Rocky Island, Day 2, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M26: Crossing Fleets, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M27: Fatsia, The Ocean Fortress, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M28: A Thousand Points of Light, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M29: Selene, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "M30: Song of Wings, Mission Ticket": AceCombat8ItemData(ItemClassification.progression, 1, 1, "Ticket"),
    "F/A-18C": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "A-6E": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Attacker"),
    "A-10C": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Attacker"),
    "EA-6B": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Electronic Warfare"),
    "EA-18G": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Electronic Warfare"),
    "F-2A": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Attacker"),
    "F-4E": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "F-14D": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "F-15C": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "F-15E": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Attacker"),
    "F-15J": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "F-16C": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "F-22A": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "F-35C": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "F/A-18E": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "F/A-18F": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "Gripen E": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "Mirage 2000-5": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "Rafale M": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "Typhoon": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "MiG-21bis": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "MiG-29A": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "MiG-31B": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "Su-25SM": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Attacker"),
    "Su-33": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "Su-34": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Attacker"),
    "Su-35S": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "Su-47": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Multirole"),
    "Su-57": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Fighter"),
    "Lightweight Blisk": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Airbrake Auxiliary Pressurization Device": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Next-Generation High-Pressure Components": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Bypass Ratio Optimization System": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "ECU Software Update": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Flap Auxiliary Pressurization Device": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Aileron Auxiliary Pressurization Device": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Rudder Auxiliary Pressurization Device": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Superior Maneuverability": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Fuel Tank Bulletproof Coating": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Multipurpose Stealth Coating": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Long-Range Enhanced Shells": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "High-Power Enhanced Shells": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Directional Proximity Fuze (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Air-to-Air Ballistic Correction Module (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Air-to-Ground Ballistic Correction Module (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Target ID Accelerator (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Guidance Optimization Software (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "New High-Energy Propellant (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Rocket Motor Combustion Optimization Unit (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Electronic Optical Hybrid Sight (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Takeoff Weight Augmentation (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Air-to-Air Ballistic Correction Module (SP. W)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Airborne Target ID Accelerator (SP. W)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Guidance Optimization Software (SP. W)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "New High-Energy Propellant (Air-to-Air MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Combustion Optimization Unit (Air-to-Air MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Air-to-Air Electronic Optical Hybrid Sight": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Multi-Target Air-to-Air Detection Accelerator": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Reinforced Mount (Air-to-Air MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Air-to-Ground Ballistic Correction Module (SP. W)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Surface Target ID Accelerator (SP. W)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Air-to-Ground Electronic Optical Hybrid Sight": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Multi-Target Air-to-Ground Detection Accelerator": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Long-Range Terrain Scan Accelerator": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Air-to-Ship Surveillance Scan Accelerator": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Reinforced Mount (Air-to-Ground MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "High-Spec Explosive Charge": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Additional Bomb Explosives": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "GPS Targeting Support System": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Extended Drop Rack": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "New Bomb Rack Safety Device": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Bomb Noise Filter": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Additional Rocket Explosives": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Additional Rocket Propellant": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "High-Speed Projectiles": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "High-Power Accumulator": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Additional Aerial Suppression Explosives": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Small Anti-Icing/De-Icing System": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Main Structural Frame": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Adaptive Armor Material": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Auto-Strafing Machine Gun Device": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Onboard Self-Defense Jammer": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Predictive Lock-On Algorithm (MSL)": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Anti-Stealth Microwave Radar": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Drop Tank": AceCombat8ItemData(ItemClassification.useful, 1, 1, "Part"),
    "Progressive F/A-18C: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-4E: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive A-6E: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive MiG-21bis: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive EA-6B: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-14D: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Su-25SM: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive MiG-29A: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive MiG-31B": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-2A: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Mirage 2000-5: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Su-33: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Su-47: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-16C: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive A-10C: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-15J: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-15C: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F/A-18E: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F/A-18F: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Gripen E: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Su-34: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-15E: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Su-35S: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive EA-18G: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Typhoon: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive Rafale M: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-22A: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive F-35C: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "FA-36": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Aircraft"),
    "EA-36": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Aircraft"),
    "X-40": AceCombat8ItemData(ItemClassification.useful, 4, 1, "Aircraft"),
    "Progressive FA-36: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive EA-36: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
    "Progressive X-40: SPW": AceCombat8ItemData(ItemClassification.useful, 3, 1, "Weaponry"),
}
# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.


# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class AceCombat8Item(Item):
    game = "AceCombat8"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: AceCombat8Item) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    #if world.random.randint(0, 99) < world.options.trap_chance:
    #    return "Math Trap"
    return "Nothing"


def create_item_with_correct_classification(world: AceCombat8World, name: str) -> AceCombat8Item:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    #if name == "Health Upgrade" and world.options.hard_mode:
    #    classification = ItemClassification.progression

    return AceCombat8Item(name, item_table[name].classification, item_table[name].item_id_offset, world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: AceCombat8World) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
        "M1: Jokers Wild, Mission Ticket",
        "M2: Nomad, Mission Ticket",
        "M3: Purple Magic Takes Flight, Mission Ticket",
        "M4: The Fall of the Numbered Fleets, Mission Ticket",
        "M5: Retaking of Theve, Mission Ticket",
        "M6: Attack on the Drinwich Airfield, Mission Ticket",
        "M7: A Lifeline in the Desert, Mission Ticket",
        "M8: Retaking of Theve II, Mission Ticket",
        "M9: The Land Battleship Blockade, Mission Ticket",
        "M10: Over the Rainband, Mission Ticket",
        "M11: Maximum Payload, Mission Ticket",
        "M12: An Island in Darkness, Mission Ticket",
        "M13: The People of the Lost Country, Mission Ticket",
        "M14: Two on the Run, Mission Ticket",
        "M15: Wings of Wax, Mission Ticket",
        "M16: Singer, Mission Ticket",
        "M17: Land Battleship No. 3, Mission Ticket",
        "M18: Moonlight and Shadows, Mission Ticket",
        "M19: Clearing the Lighthouse, Mission Ticket",
        "M20: Escort Orbiter, Mission Ticket",
        "M21: The Star-Bound Bird, Mission Ticket",
        "M22: Pursuing the HSCA, Mission Ticket",
        "M23: The Destruction of Expo City, Mission Ticket",
        "M24: The Battle of Rocky Island, Day 1, Mission Ticket",
        "M25: The Battle of Rocky Island, Day 2, Mission Ticket",
        "M26: Crossing Fleets, Mission Ticket",
        "M27: Fatsia, The Ocean Fortress, Mission Ticket",
        "M28: A Thousand Points of Light, Mission Ticket",
        "M29: Selene, Mission Ticket",
        "M30: Song of Wings, Mission Ticket",
        "F/A-18C",
        "F/A-18C",
        "F/A-18C",
        "F/A-18C",
        "A-6E",
        "A-6E",
        "A-6E",
        "A-6E",
        "A-10C",
        "A-10C",
        "A-10C",
        "A-10C",
        "EA-6B",
        "EA-6B",
        "EA-6B",
        "EA-6B",
        "EA-18G",
        "EA-18G",
        "EA-18G",
        "EA-18G",
        "F-2A",
        "F-2A",
        "F-2A",
        "F-2A",
        "F-4E",
        "F-4E",
        "F-4E",
        "F-4E",
        "F-14D",
        "F-14D",
        "F-14D",
        "F-14D",
        "F-15C",
        "F-15C",
        "F-15C",
        "F-15C",
        "F-15E",
        "F-15E",
        "F-15E",
        "F-15E",
        "F-15J",
        "F-15J",
        "F-15J",
        "F-15J",
        "F-16C",
        "F-16C",
        "F-16C",
        "F-16C",
        "F-22A",
        "F-22A",
        "F-22A",
        "F-22A",
        "F-35C",
        "F-35C",
        "F-35C",
        "F-35C",
        "F/A-18E",
        "F/A-18E",
        "F/A-18E",
        "F/A-18E",
        "F/A-18F",
        "F/A-18F",
        "F/A-18F",
        "F/A-18F",
        "Gripen E",
        "Gripen E",
        "Gripen E",
        "Gripen E",
        "Mirage 2000-5",
        "Mirage 2000-5",
        "Mirage 2000-5",
        "Mirage 2000-5",
        "Rafale M",
        "Rafale M",
        "Rafale M",
        "Rafale M",
        "Typhoon",
        "Typhoon",
        "Typhoon",
        "Typhoon",
        "MiG-21bis",
        "MiG-21bis",
        "MiG-21bis",
        "MiG-21bis",
        "MiG-29A",
        "MiG-29A",
        "MiG-29A",
        "MiG-29A",
        "MiG-31B",
        "MiG-31B",
        "MiG-31B",
        "MiG-31B",
        "Su-25SM",
        "Su-25SM",
        "Su-25SM",
        "Su-25SM",
        "Su-33",
        "Su-33",
        "Su-33",
        "Su-33",
        "Su-34",
        "Su-34",
        "Su-34",
        "Su-34",
        "Su-35S",
        "Su-35S",
        "Su-35S",
        "Su-35S",
        "Su-47",
        "Su-47",
        "Su-47",
        "Su-47",
        "Su-57",
        "Su-57",
        "Su-57",
        "Su-57",
        "Lightweight Blisk",
        "Airbrake Auxiliary Pressurization Device",
        "Next-Generation High-Pressure Components",
        "Bypass Ratio Optimization System",
        "ECU Software Update",
        "Flap Auxiliary Pressurization Device",
        "Aileron Auxiliary Pressurization Device",
        "Rudder Auxiliary Pressurization Device",
        "Superior Maneuverability",
        "Fuel Tank Bulletproof Coating",
        "Multipurpose Stealth Coating",
        "Long-Range Enhanced Shells",
        "High-Power Enhanced Shells",
        "Directional Proximity Fuze (MSL)",
        "Air-to-Air Ballistic Correction Module (MSL)",
        "Air-to-Ground Ballistic Correction Module (MSL)",
        "Target ID Accelerator (MSL)",
        "Guidance Optimization Software (MSL)",
        "New High-Energy Propellant (MSL)",
        "Rocket Motor Combustion Optimization Unit (MSL)",
        "Electronic Optical Hybrid Sight (MSL)",
        "Takeoff Weight Augmentation (MSL)",
        "Air-to-Air Ballistic Correction Module (SP. W)",
        "Airborne Target ID Accelerator (SP. W)",
        "Guidance Optimization Software (SP. W)",
        "New High-Energy Propellant (Air-to-Air MSL)",
        "Combustion Optimization Unit (Air-to-Air MSL)",
        "Air-to-Air Electronic Optical Hybrid Sight",
        "Multi-Target Air-to-Air Detection Accelerator",
        "Reinforced Mount (Air-to-Air MSL)",
        "Air-to-Ground Ballistic Correction Module (SP. W)",
        "Surface Target ID Accelerator (SP. W)",
        "Air-to-Ground Electronic Optical Hybrid Sight",
        "Multi-Target Air-to-Ground Detection Accelerator",
        "Long-Range Terrain Scan Accelerator",
        "Air-to-Ship Surveillance Scan Accelerator",
        "Reinforced Mount (Air-to-Ground MSL)",
        "High-Spec Explosive Charge",
        "Additional Bomb Explosives",
        "GPS Targeting Support System",
        "Extended Drop Rack",
        "New Bomb Rack Safety Device",
        "Bomb Noise Filter",
        "Additional Rocket Explosives",
        "Additional Rocket Propellant",
        "High-Speed Projectiles",
        "High-Power Accumulator",
        "Additional Aerial Suppression Explosives",
        "Small Anti-Icing/De-Icing System",
        "Main Structural Frame",
        "Adaptive Armor Material",
        "Auto-Strafing Machine Gun Device",
        "Onboard Self-Defense Jammer",
        "Predictive Lock-On Algorithm (MSL)",
        "Anti-Stealth Microwave Radar",
        "Drop Tank",
        "Progressive F/A-18C: SPW",
        "Progressive F/A-18C: SPW",
        "Progressive F/A-18C: SPW",
        "Progressive F-4E: SPW",
        "Progressive F-4E: SPW",
        "Progressive F-4E: SPW",
        "Progressive A-6E: SPW",
        "Progressive A-6E: SPW",
        "Progressive A-6E: SPW",
        "Progressive MiG-21bis: SPW",
        "Progressive MiG-21bis: SPW",
        "Progressive MiG-21bis: SPW",
        "Progressive EA-6B: SPW",
        "Progressive EA-6B: SPW",
        "Progressive EA-6B: SPW",
        "Progressive F-14D: SPW",
        "Progressive F-14D: SPW",
        "Progressive F-14D: SPW",
        "Progressive Su-25SM: SPW",
        "Progressive Su-25SM: SPW",
        "Progressive Su-25SM: SPW",
        "Progressive MiG-29A: SPW",
        "Progressive MiG-29A: SPW",
        "Progressive MiG-29A: SPW",
        "Progressive MiG-31B",
        "Progressive MiG-31B",
        "Progressive MiG-31B",
        "Progressive F-2A: SPW",
        "Progressive F-2A: SPW",
        "Progressive F-2A: SPW",
        "Progressive Mirage 2000-5: SPW",
        "Progressive Mirage 2000-5: SPW",
        "Progressive Mirage 2000-5: SPW",
        "Progressive Su-33: SPW",
        "Progressive Su-33: SPW",
        "Progressive Su-33: SPW",
        "Progressive Su-47: SPW",
        "Progressive Su-47: SPW",
        "Progressive Su-47: SPW",
        "Progressive F-16C: SPW",
        "Progressive F-16C: SPW",
        "Progressive F-16C: SPW",
        "Progressive A-10C: SPW",
        "Progressive A-10C: SPW",
        "Progressive A-10C: SPW",
        "Progressive F-15J: SPW",
        "Progressive F-15J: SPW",
        "Progressive F-15J: SPW",
        "Progressive F-15C: SPW",
        "Progressive F-15C: SPW",
        "Progressive F-15C: SPW",
        "Progressive F/A-18E: SPW",
        "Progressive F/A-18E: SPW",
        "Progressive F/A-18E: SPW",
        "Progressive F/A-18F: SPW",
        "Progressive F/A-18F: SPW",
        "Progressive F/A-18F: SPW",
        "Progressive Gripen E: SPW",
        "Progressive Gripen E: SPW",
        "Progressive Gripen E: SPW",
        "Progressive Su-34: SPW",
        "Progressive Su-34: SPW",
        "Progressive Su-34: SPW",
        "Progressive F-15E: SPW",
        "Progressive F-15E: SPW",
        "Progressive F-15E: SPW",
        "Progressive Su-35S: SPW",
        "Progressive Su-35S: SPW",
        "Progressive Su-35S: SPW",
        "Progressive EA-18G: SPW",
        "Progressive EA-18G: SPW",
        "Progressive EA-18G: SPW",
        "Progressive Typhoon: SPW",
        "Progressive Typhoon: SPW",
        "Progressive Typhoon: SPW",
        "Progressive Rafale M: SPW",
        "Progressive Rafale M: SPW",
        "Progressive Rafale M: SPW",
        "Progressive F-22A: SPW",
        "Progressive F-22A: SPW",
        "Progressive F-22A: SPW",
        "Progressive F-35C: SPW",
        "Progressive F-35C: SPW",
        "Progressive F-35C: SPW",
        "FA-36",
        "FA-36",
        "FA-36",
        "FA-36",
        "EA-36",
        "EA-36",
        "EA-36",
        "EA-36",
        "X-40",
        "X-40",
        "X-40",
        "X-40",
        "Progressive FA-36: SPW",
        "Progressive FA-36: SPW",
        "Progressive FA-36: SPW",
        "Progressive EA-36: SPW",
        "Progressive EA-36: SPW",
        "Progressive EA-36: SPW",
        "Progressive X-40: SPW",
        "Progressive X-40: SPW",
        "Progressive X-40: SPW",
    ]
    # Some items may only exist if the player enables certain options.
    # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # Otherwise, we add a filler Confetti Cannon.
    #if world.options.hammer:
        # Once again, it is important to stress that even though the Hammer doesn't always exist,
        # it must be present in the worlds item_name_to_id.
        # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
        #itempool.append(world.create_item("Hammer"))

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().
    #if world.options.start_with_one_confetti_cannon:
        # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
        #starting_confetti_cannon = world.create_item("Confetti Cannon")
        #world.push_precollected(starting_confetti_cannon)
