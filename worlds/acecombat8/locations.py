from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import AceCombat8World

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "Jokers Wild Clear Mission": 1,
    "Jokers Wild Clear Mission (Veteran)": 2,
    "Jokers Wild Clear Mission (Elite)": 3,
    "Jokers Wild Clear Mission (Ace)": 4,
    "Jokers Wild Clear Mission S-Rank": 5,
    "Jokers Wild Clear Mission S-Rank (Veteran)": 6,
    "Jokers Wild Clear Mission S-Rank (Elite)": 7,
    "Jokers Wild Clear Mission S-Rank (Ace)": 8,
    "Nomad Clear Mission": 9,
    "Nomad Clear Mission (Veteran)": 10,
    "Nomad Clear Mission (Elite)": 11,
    "Nomad Clear Mission (Ace)": 12,
    "Nomad Clear Mission S-Rank": 13,
    "Nomad Clear Mission S-Rank (Veteran)": 14,
    "Nomad Clear Mission S-Rank (Elite)": 15,
    "Nomad Clear Mission S-Rank (Ace)": 16,
    "Purple Magic Takes Flight Clear Mission": 17,
    "Purple Magic Takes Flight Clear Mission (Veteran)": 18,
    "Purple Magic Takes Flight Clear Mission (Elite)": 19,
    "Purple Magic Takes Flight Clear Mission (Ace)": 20,
    "Purple Magic Takes Flight Clear Mission S-Rank": 21,
    "Purple Magic Takes Flight Clear Mission S-Rank (Veteran)": 22,
    "Purple Magic Takes Flight Clear Mission S-Rank (Elite)": 23,
    "Purple Magic Takes Flight Clear Mission S-Rank (Ace)": 24,
    "The Fall of the Numbered Fleets Clear Mission": 25,
    "The Fall of the Numbered Fleets Clear Mission (Veteran)": 26,
    "The Fall of the Numbered Fleets Clear Mission (Elite)": 27,
    "The Fall of the Numbered Fleets Clear Mission (Ace)": 28,
    "The Fall of the Numbered Fleets Clear Mission S-Rank": 29,
    "The Fall of the Numbered Fleets Clear Mission S-Rank (Veteran)": 30,
    "The Fall of the Numbered Fleets Clear Mission S-Rank (Elite)": 31,
    "The Fall of the Numbered Fleets Clear Mission S-Rank (Ace)": 32,
    "Retaking of Theve Clear Mission": 33,
    "Retaking of Theve Clear Mission (Veteran)": 34,
    "Retaking of Theve Clear Mission (Elite)": 35,
    "Retaking of Theve Clear Mission (Ace)": 36,
    "Retaking of Theve Clear Mission S-Rank": 37,
    "Retaking of Theve Clear Mission S-Rank (Veteran)": 38,
    "Retaking of Theve Clear Mission S-Rank (Elite)": 39,
    "Retaking of Theve Clear Mission S-Rank (Ace)": 40,
    "Attack on the Drinwich Airfield Clear Mission": 41,
    "Attack on the Drinwich Airfield Clear Mission (Veteran)": 42,
    "Attack on the Drinwich Airfield Clear Mission (Elite)": 43,
    "Attack on the Drinwich Airfield Clear Mission (Ace)": 44,
    "Attack on the Drinwich Airfield Clear Mission S-Rank": 45,
    "Attack on the Drinwich Airfield Clear Mission S-Rank (Veteran)": 46,
    "Attack on the Drinwich Airfield Clear Mission S-Rank (Elite)": 47,
    "Attack on the Drinwich Airfield Clear Mission S-Rank (Ace)": 48,
    "A Lifeline in the Desert Clear Mission": 49,
    "A Lifeline in the Desert Clear Mission (Veteran)": 50,
    "A Lifeline in the Desert Clear Mission (Elite)": 51,
    "A Lifeline in the Desert Clear Mission (Ace)": 52,
    "A Lifeline in the Desert Clear Mission S-Rank": 53,
    "A Lifeline in the Desert Clear Mission S-Rank (Veteran)": 54,
    "A Lifeline in the Desert Clear Mission S-Rank (Elite)": 55,
    "A Lifeline in the Desert Clear Mission S-Rank (Ace)": 56,
    "Retaking of Theve II Clear Mission": 57,
    "Retaking of Theve II Clear Mission (Veteran)": 58,
    "Retaking of Theve II Clear Mission (Elite)": 59,
    "Retaking of Theve II Clear Mission (Ace)": 60,
    "Retaking of Theve II Clear Mission S-Rank": 61,
    "Retaking of Theve II Clear Mission S-Rank (Veteran)": 62,
    "Retaking of Theve II Clear Mission S-Rank (Elite)": 63,
    "Retaking of Theve II Clear Mission S-Rank (Ace)": 64,
    "The Land Battleship Blockade Clear Mission": 65,
    "The Land Battleship Blockade Clear Mission (Veteran)": 66,
    "The Land Battleship Blockade Clear Mission (Elite)": 67,
    "The Land Battleship Blockade Clear Mission (Ace)": 68,
    "The Land Battleship Blockade Clear Mission S-Rank": 69,
    "The Land Battleship Blockade Clear Mission S-Rank (Veteran)": 70,
    "The Land Battleship Blockade Clear Mission S-Rank (Elite)": 71,
    "The Land Battleship Blockade Clear Mission S-Rank (Ace)": 72,
    "Over the Rainband Clear Mission": 73,
    "Over the Rainband Clear Mission (Veteran)": 74,
    "Over the Rainband Clear Mission (Elite)": 75,
    "Over the Rainband Clear Mission (Ace)": 76,
    "Over the Rainband Clear Mission S-Rank": 77,
    "Over the Rainband Clear Mission S-Rank (Veteran)": 78,
    "Over the Rainband Clear Mission S-Rank (Elite)": 79,
    "Over the Rainband Clear Mission S-Rank (Ace)": 80,
    "Maximum Payload Clear Mission": 81,
    "Maximum Payload Clear Mission (Veteran)": 82,
    "Maximum Payload Clear Mission (Elite)": 83,
    "Maximum Payload Clear Mission (Ace)": 84,
    "Maximum Payload Clear Mission S-Rank": 85,
    "Maximum Payload Clear Mission S-Rank (Veteran)": 86,
    "Maximum Payload Clear Mission S-Rank (Elite)": 87,
    "Maximum Payload Clear Mission S-Rank (Ace)": 88,
    "An Island in Darkness Clear Mission": 89,
    "An Island in Darkness Clear Mission (Veteran)": 90,
    "An Island in Darkness Clear Mission (Elite)": 91,
    "An Island in Darkness Clear Mission (Ace)": 92,
    "An Island in Darkness Clear Mission S-Rank": 93,
    "An Island in Darkness Clear Mission S-Rank (Veteran)": 94,
    "An Island in Darkness Clear Mission S-Rank (Elite)": 95,
    "An Island in Darkness Clear Mission S-Rank (Ace)": 96,
    "The People of the Lost Country Clear Mission": 97,
    "The People of the Lost Country Clear Mission (Veteran)": 98,
    "The People of the Lost Country Clear Mission (Elite)": 99,
    "The People of the Lost Country Clear Mission (Ace)": 100,
    "The People of the Lost Country Clear Mission S-Rank": 101,
    "The People of the Lost Country Clear Mission S-Rank (Veteran)": 102,
    "The People of the Lost Country Clear Mission S-Rank (Elite)": 103,
    "The People of the Lost Country Clear Mission S-Rank (Ace)": 104,
    "Two on the Run Clear Mission": 105,
    "Two on the Run Clear Mission (Veteran)": 106,
    "Two on the Run Clear Mission (Elite)": 107,
    "Two on the Run Clear Mission (Ace)": 108,
    "Two on the Run Clear Mission S-Rank": 109,
    "Two on the Run Clear Mission S-Rank (Veteran)": 110,
    "Two on the Run Clear Mission S-Rank (Elite)": 111,
    "Two on the Run Clear Mission S-Rank (Ace)": 112,
    "Wings of Wax Clear Mission": 113,
    "Wings of Wax Clear Mission (Veteran)": 114,
    "Wings of Wax Clear Mission (Elite)": 115,
    "Wings of Wax Clear Mission (Ace)": 116,
    "Wings of Wax Clear Mission S-Rank": 117,
    "Wings of Wax Clear Mission S-Rank (Veteran)": 118,
    "Wings of Wax Clear Mission S-Rank (Elite)": 119,
    "Wings of Wax Clear Mission S-Rank (Ace)": 120,
    "Singer Clear Mission": 121,
    "Singer Clear Mission (Veteran)": 122,
    "Singer Clear Mission (Elite)": 123,
    "Singer Clear Mission (Ace)": 124,
    "Singer Clear Mission S-Rank": 125,
    "Singer Clear Mission S-Rank (Veteran)": 126,
    "Singer Clear Mission S-Rank (Elite)": 127,
    "Singer Clear Mission S-Rank (Ace)": 128,
    "Land Battleship No.3 Clear Mission": 129,
    "Land Battleship No.3 Clear Mission (Veteran)": 130,
    "Land Battleship No.3 Clear Mission (Elite)": 131,
    "Land Battleship No.3 Clear Mission (Ace)": 132,
    "Land Battleship No.3 Clear Mission S-Rank": 133,
    "Land Battleship No.3 Clear Mission S-Rank (Veteran)": 134,
    "Land Battleship No.3 Clear Mission S-Rank (Elite)": 135,
    "Land Battleship No.3 Clear Mission S-Rank (Ace)": 136,
    "Moonlight and Shadows Clear Mission": 137,
    "Moonlight and Shadows Clear Mission (Veteran)": 138,
    "Moonlight and Shadows Clear Mission (Elite)": 139,
    "Moonlight and Shadows Clear Mission (Ace)": 140,
    "Moonlight and Shadows Clear Mission S-Rank": 141,
    "Moonlight and Shadows Clear Mission S-Rank (Veteran)": 142,
    "Moonlight and Shadows Clear Mission S-Rank (Elite)": 143,
    "Moonlight and Shadows Clear Mission S-Rank (Ace)": 144,
    "Clearing the Lighthouse Clear Mission": 145,
    "Clearing the Lighthouse Clear Mission (Veteran)": 146,
    "Clearing the Lighthouse Clear Mission (Elite)": 147,
    "Clearing the Lighthouse Clear Mission (Ace)": 148,
    "Clearing the Lighthouse Clear Mission S-Rank": 149,
    "Clearing the Lighthouse Clear Mission S-Rank (Veteran)": 150,
    "Clearing the Lighthouse Clear Mission S-Rank (Elite)": 151,
    "Clearing the Lighthouse Clear Mission S-Rank (Ace)": 152,
    "Escort Orbiter Clear Mission": 153,
    "Escort Orbiter Clear Mission (Veteran)": 154,
    "Escort Orbiter Clear Mission (Elite)": 155,
    "Escort Orbiter Clear Mission (Ace)": 156,
    "Escort Orbiter Clear Mission S-Rank": 157,
    "Escort Orbiter Clear Mission S-Rank (Veteran)": 158,
    "Escort Orbiter Clear Mission S-Rank (Elite)": 159,
    "Escort Orbiter Clear Mission S-Rank (Ace)": 160,
    "The Star-Bound Bird Clear Mission": 161,
    "The Star-Bound Bird Clear Mission (Veteran)": 162,
    "The Star-Bound Bird Clear Mission (Elite)": 163,
    "The Star-Bound Bird Clear Mission (Ace)": 164,
    "The Star-Bound Bird Clear Mission S-Rank": 165,
    "The Star-Bound Bird Clear Mission S-Rank (Veteran)": 166,
    "The Star-Bound Bird Clear Mission S-Rank (Elite)": 167,
    "The Star-Bound Bird Clear Mission S-Rank (Ace)": 168,
    "Pursuing the HSCA Clear Mission": 169,
    "Pursuing the HSCA Clear Mission (Veteran)": 170,
    "Pursuing the HSCA Clear Mission (Elite)": 171,
    "Pursuing the HSCA Clear Mission (Ace)": 172,
    "Pursuing the HSCA Clear Mission S-Rank": 173,
    "Pursuing the HSCA Clear Mission S-Rank (Veteran)": 174,
    "Pursuing the HSCA Clear Mission S-Rank (Elite)": 175,
    "Pursuing the HSCA Clear Mission S-Rank (Ace)": 176,
    "The Destruction of Expo City Clear Mission": 177,
    "The Destruction of Expo City Clear Mission (Veteran)": 178,
    "The Destruction of Expo City Clear Mission (Elite)": 179,
    "The Destruction of Expo City Clear Mission (Ace)": 180,
    "The Destruction of Expo City Clear Mission S-Rank": 181,
    "The Destruction of Expo City Clear Mission S-Rank (Veteran)": 182,
    "The Destruction of Expo City Clear Mission S-Rank (Elite)": 183,
    "The Destruction of Expo City Clear Mission S-Rank (Ace)": 184,
    "The Battle of Rocky Island, Day 1 Clear Mission": 185,
    "The Battle of Rocky Island, Day 1 Clear Mission (Veteran)": 186,
    "The Battle of Rocky Island, Day 1 Clear Mission (Elite)": 187,
    "The Battle of Rocky Island, Day 1 Clear Mission (Ace)": 188,
    "The Battle of Rocky Island, Day 1 Clear Mission S-Rank": 189,
    "The Battle of Rocky Island, Day 1 Clear Mission S-Rank (Veteran)": 190,
    "The Battle of Rocky Island, Day 1 Clear Mission S-Rank (Elite)": 191,
    "The Battle of Rocky Island, Day 1 Clear Mission S-Rank (Ace)": 192,
    "The Battle of Rocky Island, Day 2 Clear Mission": 193,
    "The Battle of Rocky Island, Day 2 Clear Mission (Veteran)": 194,
    "The Battle of Rocky Island, Day 2 Clear Mission (Elite)": 195,
    "The Battle of Rocky Island, Day 2 Clear Mission (Ace)": 196,
    "The Battle of Rocky Island, Day 2 Clear Mission S-Rank": 197,
    "The Battle of Rocky Island, Day 2 Clear Mission S-Rank (Veteran)": 198,
    "The Battle of Rocky Island, Day 2 Clear Mission S-Rank (Elite)": 199,
    "The Battle of Rocky Island, Day 2 Clear Mission S-Rank (Ace)": 200,
    "Crossing Fleets Clear Mission": 201,
    "Crossing Fleets Clear Mission (Veteran)": 202,
    "Crossing Fleets Clear Mission (Elite)": 203,
    "Crossing Fleets Clear Mission (Ace)": 204,
    "Crossing Fleets Clear Mission S-Rank": 205,
    "Crossing Fleets Clear Mission S-Rank (Veteran)": 206,
    "Crossing Fleets Clear Mission S-Rank (Elite)": 207,
    "Crossing Fleets Clear Mission S-Rank (Ace)": 208,
    "Fatsia, The Ocean Fortress Clear Mission": 209,
    "Fatsia, The Ocean Fortress Clear Mission (Veteran)": 210,
    "Fatsia, The Ocean Fortress Clear Mission (Elite)": 211,
    "Fatsia, The Ocean Fortress Clear Mission (Ace)": 212,
    "Fatsia, The Ocean Fortress Clear Mission S-Rank": 213,
    "Fatsia, The Ocean Fortress Clear Mission S-Rank (Veteran)": 214,
    "Fatsia, The Ocean Fortress Clear Mission S-Rank (Elite)": 215,
    "Fatsia, The Ocean Fortress Clear Mission S-Rank (Ace)": 216,
    "A Thousand Points of Light Clear Mission": 217,
    "A Thousand Points of Light Clear Mission (Veteran)": 218,
    "A Thousand Points of Light Clear Mission (Elite)": 219,
    "A Thousand Points of Light Clear Mission (Ace)": 220,
    "A Thousand Points of Light Clear Mission S-Rank": 221,
    "A Thousand Points of Light Clear Mission S-Rank (Veteran)": 222,
    "A Thousand Points of Light Clear Mission S-Rank (Elite)": 223,
    "A Thousand Points of Light Clear Mission S-Rank (Ace)": 224,
    "Selene Clear Mission": 225,
    "Selene Clear Mission (Veteran)": 226,
    "Selene Clear Mission (Elite)": 227,
    "Selene Clear Mission (Ace)": 228,
    "Selene Clear Mission S-Rank": 229,
    "Selene Clear Mission S-Rank (Veteran)": 230,
    "Selene Clear Mission S-Rank (Elite)": 231,
    "Selene Clear Mission S-Rank (Ace)": 232,
    "Song of Wings Clear Mission": 233,
    "Song of Wings Clear Mission (Veteran)": 234,
    "Song of Wings Clear Mission (Elite)": 235,
    "Song of Wings Clear Mission (Ace)": 236,
    "Song of Wings Clear Mission S-Rank": 237,
    "Song of Wings Clear Mission S-Rank (Veteran)": 238,
    "Song of Wings Clear Mission S-Rank (Elite)": 239,
    "Song of Wings Clear Mission S-Rank (Ace)": 240,
    "11th Tactical Squadron 160th Unit \"Lux Lunae\" - Gladiator": 241,
    "11th Tactical Squadron 160th Unit \"Lux Lunae\" - Captor": 242,
    "11th Tactical Squadron 160th Unit \"Lux Lunae\" - Domitor": 243,
    "11th Tactical Squadron 160th Unit \"Lux Lunae\" - Praedo": 244,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Aranea": 245,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Luscinia": 246,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Vespa": 247,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Cerambyx": 248,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Lucanus": 249,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Locusta": 250,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Libellula": 251,
    "11th Tactical Squadron 150th Unit \"Lux Lunae\" - Gallus": 252,
    "11th Tactical Squadron 77th Unit \"Lux Lunae\" - Novacula": 253,
    "11th Tactical Squadron 77th Unit \"Lux Lunae\" - Talus": 254,
    "11th Tactical Squadron 180th Unit \"Lux Lunae\" - Patriota": 255,
    "11th Tactical Squadron 180th Unit \"Lux Lunae\" - Tormentum": 256,
    "11th Tactical Squadron 55th Unit \"Lux Lunae\" - Lacerta": 257,
    "11th Tactical Squadron 55th Unit \"Lux Lunae\" - Aspis": 258,
    "11th Tactical Squadron 55th Unit \"Lux Lunae\" - Vipera": 259,
    "11th Tactical Squadron 55th Unit \"Lux Lunae\" - Salamandra": 260,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Sagitta": 261,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Arcus": 262,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Corvus": 263,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Ulula": 264,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Picus": 265,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Cygnus": 266,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Hirundo": 267,
    "11th Tactical Squadron 140th Unit \"Lux Lunae\" - Grus": 268,
    "11th Tactical Squadron 99th Unit \"Lux Lunae\" - Tigris": 269,
    "11th Tactical Squadron 99th Unit \"Lux Lunae\" - Lynx": 270,
    "11th Tactical Squadron 99th Unit \"Lux Lunae\" - Panthera": 271,
    "11th Tactical Squadron 99th Unit \"Lux Lunae\" - Vulpes": 272,
    "8th Pastoral Air Wing, 1st Fighter Squadron - Niveus": 273,
    "8th Pastoral Air Wing, 1st Fighter Squadron - Pruina": 274,
    "11th Tactical Squadron 33rd Unit \"Lux Lunae\" - Monoceros": 275,
    "11th Tactical Squadron 33rd Unit \"Lux Lunae\" - Siren": 276,
    "11th Tactical Squadron 33rd Unit \"Lux Lunae\" - Larva": 277,
    "11th Tactical Squadron 33rd Unit \"Lux Lunae\" - Mors": 278,
    "11th Tactical Squadron 44th Unit \"Lux Lunae\" - Poeta": 279,
    "11th Tactical Squadron 44th Unit \"Lux Lunae\" - Tempestas": 280,
    "11th Tactical Squadron 44th Unit \"Lux Lunae\" - Vorticosus": 281,
    "11th Tactical Squadron 44th Unit \"Lux Lunae\" - Malacia": 282,
    "11th Tactical Squadron 120th Unit \"Lux Lunae\" - Athleta": 283,
    "11th Tactical Squadron 120th Unit \"Lux Lunae\" - Gladius": 284,
    "11th Tactical Squadron 120th Unit \"Lux Lunae\" - Flagrum": 285,
    "11th Tactical Squadron 120th Unit \"Lux Lunae\" - Lancea": 286,
    "11th Tactical Squadron 22nd Unit \"Lux Lunae\" - Doctus": 287,
    "11th Tactical Squadron 22nd Unit \"Lux Lunae\" - Saltatrix": 288,
    "11th Tactical Squadron 22nd Unit \"Lux Lunae\" - Acrobates": 289,
    "11th Tactical Squadron 22nd Unit \"Lux Lunae\" - Anteros": 290,
    "11th Tactical Squadron 22nd Unit \"Lux Lunae\" - Ares": 291,
    "Sotoa Air Force 1st Special Operations Wing Major General - Selene": 292,
    "Sotoa Air Force 132nd Foothill Air Wing 150th Tactical Squadron - Gigas": 293,
    "Sotoa Air Force 303rd Coastal Air Wing 194th Attack Squadron - Crematio": 294,
    "Sotoa Air Force 107th Rapid Response Air Wing 82nd Fighter Attack Squadron - Raia": 295,
    "Newfield Island Garrison 1st Fighter Squadron - Auster": 296,
    "Sotoa Air Force 132nd Foothill Air Wing 17th Attack Squadron - Custos": 297,
    "Sotoa Air Force 109th Apline Air Wing 146th Fighter Squardon - Flamma": 298,
    "Sotoa Air Force 418th Special Operations Wing 302nd Electronic Warfare Squadron - Orcus": 299,
    "Sotoa Air Force 303rd Coastal Air Wing 101st Fighter Squadron  - Tessera": 300,
    "Sotoa Air Force 132nd Foothill Air Wing 110th Landing Ship Support Unit - Judex": 301,
    "Sotoa Air Force 109th Alpine Air Wing 115th Fighter Squadron  - Vorago": 302,
    "Sotoa Navy 51st Fighter Squadron - Larus": 303,
    "Sotoa Air Force 106th Woodlands Air Wing 40th Fighter Attack Squadron  - Imber": 304,
    "Republic of Southern Waiapolo Air Force 1st Squadron - Sicarius": 305,
    "Sotoa Navy 18th Fighter Squadron - Lupus": 306,
    "Sotoa Air Force 1st Air Wing 201st Tactical Squadron - Currus": 307,
    "Sotoa Air Force 472nd Reserve Air Wing 101st Fighter Squadron - Avus": 308,
    "Sotoa Air Force 106th Woodlands Air Wing 300th Fighter Squadron - Curis": 309,
    "Sotoa Air Force 101st Air Wing 102nd Landing Ship Support Unit - Aleator": 310,
    "Sotoa Air Force 142nd Air Wing 109th Fighter Squadron - Periodus": 311,
    "Sotoa Navy 470th Tactical Support Squadron - Alienus": 312,
    "Sotoa Air Force 107th Rapid Response Air Wing 147th Tactical Squadron - Caligo": 313,
    "Sotoa Air Force 166th Combined Air Wing 36th Attack Squadron - Milvus/FULMEN": 314,
    "Sotoa Air Force Air Armaments Center 408th Test and Evaluation Squadron - Cantrix": 315,
    "Sotoa Air Force 166th Combined Air Wing 52nd Fighter Attack Squadron - Sabulum": 316,
    "Sotoa Air Force 166th Combined Air Wing 34th Fighter Attack Squadron - Cinis": 317,
    "Sotoa Air Force Air Armaments Center 408th Test and Evaluation Squadron - Simulacrum": 318,
    "Sotoa Air Force 107th Rapid Response Air Wing 158th Tactical Squadron - Lucidus": 319,
    "Sotoa Air Force 107th Rapid Response Air Wing 122nd Tactical Squadron - Stiria": 320,
    "Sotoa Navy 57th Fighter Attack Squadron - Harmonius": 321,
    "Sotoa Air Force 132nd Foothill Air Wing 101st Tactical Squadron - Prudens": 322,
    "Sotoa Air Force 24th Assault Wing 303rd Squadron - Tegimen": 323,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class AceCombat8Location(Location):
    game = "acecombat8"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: AceCombat8Location) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: AceCombat8Location) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    overworld = world.get_region("Overworld")
    top_left_room = world.get_region("Top Left Room")
    bottom_right_room = world.get_region("Bottom Right Room")
    right_room = world.get_region("Right Room")

    # One way to create locations is by just creating them directly via their constructor.
    bottom_left_chest = AceCombat8Location(
        world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    )

    # You can then add them to the region.
    overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    bottom_right_room_locations = get_location_names_with_ids(
        ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    )
    bottom_right_room.add_locations(bottom_right_room_locations, AceCombat8Location)

    top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    top_left_room.add_locations(top_left_room_locations, AceCombat8Location)

    right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    right_room.add_locations(right_room_locations, AceCombat8Location)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, AceCombat8Location)
    else:
        overworld.add_locations(top_middle_room_locations, AceCombat8Location)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        overworld.add_locations(bottom_left_extra_chest, AceCombat8Location)


def create_events(world: AceCombat8World) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = AceCombat8Location(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.AceCombat8Item("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
