import sublime, sublime_plugin, sys, os
PYTHON_VERSION = sys.version_info
if PYTHON_VERSION[0] == 2:
    import imp
    mainPackage = os.path.join(os.path.split(os.getcwd())[0], "SublimePapyrus", "SublimePapyrus.py")
    imp.load_source("SublimePapyrus", mainPackage)
    del mainPackage
    import SublimePapyrus
if PYTHON_VERSION[0] == 3:
    from SublimePapyrus import SublimePapyrus

class PapyrusSkseMenuSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
    def get_items(self, **args):
        items = {
        "Barter": "BarterMenu",
        "Book": "Book Menu",
        "Console native UI": "Console Native UI Menu",
        "Console": "Console",
        "Container": "ContainerMenu",
        "Crafting": "Crafting Menu",
        "Credits": "Credits Menu",
        "Cursor": "Cursor Menu",
        "Custom": "CustomMenu",
        "Debug text": "Debug Text Menu",
        "Dialogue": "Dialogue Menu",
        "Fader": "Fader Menu",
        "Favorites": "FavoritesMenu",
        "Gift": "GiftMenu",
        "HUD": "HUD Menu",
        "Inventory": "InventoryMenu",
        "Journal": "Journal Menu",
        "Kinect": "Kinect Menu",
        "Level up": "LevelUp Menu",
        "Loading": "Loading Menu",
        "Lockpicking": "Lockpicking Menu",
        "Magic": "MagicMenu",
        "Main menu": "Main Menu",
        "Map": "MapMenu",
        "Message box": "MessageBoxMenu",
        "Mist": "Mist Menu",
        "Overlay interaction": "Overlay Interaction Menu",
        "Overlay": "Overlay Menu",
        "Quantity": "Quantity Menu",
        "Race (character creation)": "RaceSex Menu",
        "Sleep/wait": "Sleep/Wait Menu",
        "Stats": "StatsMenu",
        "Title sequence": "TitleSequence Menu",
        "Top": "Top Menu",
        "Training": "Training Menu",
        "Tutorial": "Tutorial Menu",
        "Tween": "TweenMenu"
        }
        return items

class PapyrusSkseKeycodeSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
    def get_items(self, **args):
        items = {
        "0": 11,
        "1": 2,
        "2": 3,
        "3": 4,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 8,
        "8": 9,
        "9": 10,
        "A (Gamepad)": 276,
        "A": 30,
        "Apostrophe": 40,
        "B (Gamepad)": 277,
        "B": 48,
        "Back (Gamepad)": 271,
        "Back Slash": 43,
        "Backspace": 14,
        "C": 46,
        "Caps Lock": 58,
        "Comma": 51,
        "D": 32,
        "D-pad Down (Gamepad)": 267,
        "D-pad Left (Gamepad)": 268,
        "D-pad Right (Gamepad)": 269,
        "D-pad Up (Gamepad)": 266,
        "Delete": 211,
        "Down Arrow": 208,
        "E": 18,
        "End": 207,
        "Enter": 28,
        "Equals": 13,
        "Escape": 1,
        "F": 33,
        "F1": 59,
        "F10": 68,
        "F11": 87,
        "F12": 88,
        "F2": 60,
        "F3": 61,
        "F4": 62,
        "F5": 63,
        "F6": 64,
        "F7": 65,
        "F8": 66,
        "F9": 67,
        "Forward Slash": 53,
        "G": 34,
        "H": 35,
        "Home": 199,
        "I": 23,
        "Insert": 210,
        "J": 36,
        "K": 37,
        "L": 38,
        "Left Alt": 56,
        "Left Arrow": 203,
        "Left Bracket": 26,
        "Left Control": 29,
        "Left Mouse Button": 256,
        "Left Shift": 42,
        "Left shoulder (Gamepad)": 274,
        "Left thumbstick (Gamepad)": 272,
        "Left trigger (Gamepad)": 280,
        "M": 50,
        "Middle/Wheel Mouse Button": 258,
        "Minus": 12,
        "Mouse Button 3": 259,
        "Mouse Button 4": 260,
        "Mouse Button 5": 261,
        "Mouse Button 6": 262,
        "Mouse Button 7": 263,
        "Mouse Wheel Down": 265,
        "Mouse Wheel Up": 264,
        "N": 49,
        "NUM Enter": 156,
        "Num Lock": 69,
        "NUM*": 55,
        "NUM+": 78,
        "NUM-": 74,
        "NUM.": 83,
        "NUM/": 181,
        "NUM0": 82,
        "NUM1": 79,
        "NUM2": 80,
        "NUM3": 81,
        "NUM4": 75,
        "NUM5": 76,
        "NUM6": 77,
        "NUM7": 71,
        "NUM8": 72,
        "NUM9": 73,
        "O": 24,
        "P": 25,
        "Page Down": 209,
        "Page Up": 201,
        "Period": 52,
        "Q": 16,
        "R": 19,
        "Right Alt": 184,
        "Right Arrow": 205,
        "Right Bracket": 27,
        "Right Control": 157,
        "Right Mouse Button": 257,
        "Right Shift": 54,
        "Right shoulder (Gamepad)": 275,
        "Right thumbstick (Gamepad)": 273,
        "S": 31,
        "Scroll Lock": 70,
        "Semicolon": 39,
        "Spacebar": 57,
        "Start (Gamepad)": 270,
        "T": 20,
        "Tab": 15,
        "Tilde": 41,
        "U": 22,
        "Up Arrow": 200,
        "V": 47,
        "W": 17,
        "X (Gamepad)": 278,
        "X": 45,
        "Y (Gamepad)": 279,
        "Y": 21,
        "Z": 44,
        "Right trigger (Gamepad)": 281
        }
        return items

class PapyrusSkseControlSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
    def get_items(self, **args):
        items = {
        "Activate": "Activate",
        "Auto-move": "Auto-Move",
        "Back": "Back",
        "Camera Path": "CameraPath",
        "Console": "Console",
        "Favorites": "Favorites",
        "Forward": "Forward",
        "Hotkey 1": "Hotkey1",
        "Hotkey 2": "Hotkey2",
        "Hotkey 3": "Hotkey3",
        "Hotkey 4": "Hotkey4",
        "Hotkey 5": "Hotkey5",
        "Hotkey 6": "Hotkey6",
        "Hotkey 7": "Hotkey7",
        "Hotkey 8": "Hotkey8",
        "Journal": "Journal",
        "Jump": "Jump",
        "Left Attack/Block": "Left Attack/Block",
        "Look": "Look",
        "Move": "Move",
        "Multi-screenshot": "Multi-Screenshot",
        "Pause": "Pause",
        "Quick Inventory": "Quick Inventory",
        "Quick Load": "Quickload",
        "Quick Magic": "Quick Magic",
        "Quick Map": "Quick Map",
        "Quick Save": "Quicksave",
        "Quick Stats": "Quick Stats",
        "Ready Weapon": "Ready Weapon",
        "Right Attack/Block": "Right Attack/Block",
        "Run": "Run",
        "Screenshot": "Screenshot",
        "Shout": "Shout",
        "Sneak": "Sneak",
        "Sprint": "Sprint",
        "Strafe Left": "Strafe Left",
        "Strafe Right": "Strafe Right",
        "Toggle Always Run": "Toggle Always Run",
        "Toggle POV": "Toggle POV",
        "Tween Menu": "Tween Menu",
        "Wait": "Wait",
        "Zoom In": "Zoom In",
        "Zoom Out": "Zoom Out"
        }
        return items

class PapyrusSkseDefaultObjectSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
    def get_items(self, **args):
        items = {
        "Action Activate": "AAAC",
        "Action Bleedout Start": "AAB1",
        "Action Bleedout Stop": "AAB2",
        "Action Block Anticipate": "AABA",
        "Action Block Hit": "AABH",
        "Action Bumped Into": "AABI",
        "Action Death Wait": "AADW",
        "Action Death": "AADE",
        "Action Draw": "AADR",
        "Action Dual Power Attack": "ADPA",
        "Action DualAttack": "AADA",
        "Action DualRelease": "AADL",
        "Action Fall": "AAFA",
        "Action Fly Start": "AAF1",
        "Action Fly Stop": "AAF2",
        "Action Force Equip": "AAFQ",
        "Action Get Up": "AAGU",
        "Action Hover Start": "AAH1",
        "Action Hover Stop": "AAH2",
        "Action Idle Stop Instant": "ASID",
        "Action Idle Stop": "AAIS",
        "Action Idle Warn": "AIDW",
        "Action Idle": "AAID",
        "Action Jump": "AAJP",
        "Action Knockdown": "AKDN",
        "Action Land": "AALN",
        "Action Large Movement Delta": "AALM",
        "Action Large Recoil": "AAR2",
        "Action Left Power Attack": "ALPA",
        "Action LeftAttack": "AALA",
        "Action LeftInterrupt": "AALI",
        "Action LeftReady": "AALD",
        "Action LeftRelease": "AALR",
        "Action Listen Idle": "ALTI",
        "Action Look": "AALK",
        "Action Move Backward": "AMBK",
        "Action Move Forward": "AMFD",
        "Action Move Left": "AMLT",
        "Action Move Right": "AMRT",
        "Action Move Start": "AMST",
        "Action Move Stop": "AMSP",
        "Action Path End": "AAPE",
        "Action Path Start": "AAPS",
        "Action Ragdoll Instant": "ARGI",
        "Action Recoil": "AARC",
        "Action Reload": "AREL",
        "Action Reset Animation Graph": "ARAG",
        "Action Right Power Attack": "AAPA",
        "Action RightAttack": "AARA",
        "Action RightInterrupt": "AARI",
        "Action RightReady": "AARD",
        "Action RightRelease": "AARR",
        "Action Sheath": "AASH",
        "Action Shield Change": "AASC",
        "Action Sneak": "AASN",
        "Action Sprint Start": "AAST",
        "Action Sprint Stop": "AASP",
        "Action Stagger Start": "AAS1",
        "Action Summoned Start": "AASS",
        "Action Swim State Change": "AASW",
        "Action Talking Idle": "ATKI",
        "Action Turn Left": "ATLE",
        "Action Turn Right": "ATRI",
        "Action Turn Stop": "ATSP",
        "Action Voice": "AAVC",
        "Action VoiceInterrupt": "AAVI",
        "Action VoiceReady": "AAVD",
        "Action VoiceRelease": "AAVR",
        "Action Ward Hit": "AAWH",
        "Action Waterwalk Start": "AWWS",
        "Allow Player Shout": "APSH",
        "Armor Material List": "ARTL",
        "Art Object - Absorb Effect": "ABSE",
        "Ash LOD Material (HD)": "ALHD",
        "Ash LOD Material": "ALDM",
        "Base Armor Enchantment": "BENA",
        "Base Poison": "BAPS",
        "Base Potion": "BAPO",
        "Base Weapon Enchantment": "BENW",
        "Battle Music": "BTMS",
        "Bunny Faction": "AWWW",
        "Combat Style": "CSTY",
        "Commanded Actor Ability": "CACA",
        "Complex Scene Object": "CMPX",
        "Dark Brotherhood Faction": "DBHF",
        "Death Music": "DTMS",
        "Default MovementType: Fly": "DMFL",
        "Default MovementType: Run": "DMRN",
        "Default MovementType: Sneak": "DMSN",
        "Default MovementType: Sprint": "DMSP",
        "Default MovementType: Swim": "DMSW",
        "Default MovementType: Walk": "DMWL",
        "Default Music": "DFMS",
        "Default Pack List": "PLST",
        "Dialogue Output Model (2D)": "DOP3",
        "Dialogue Output Model (3D)": "DOP2",
        "Dialogue Voice Category": "DDSC",
        "DialogueFollower Quest": "DGFL",
        "Dragon Crash Zone Marker": "DCZM",
        "Dragon Land Zone Marker": "DLZM",
        "Dragon Mount No Land List": "DMXL",
        "Drug Wears Off Image Space": "DEIS",
        "Dungeon Cleared Music": "DCMS",
        "Eat Package Default Food": "EPDF",
        "EitherHand Equip": "EHEQ",
        "Every Actor Ability": "EACA",
        "Favor Cost Large": "FPCL",
        "Favor Cost Medium": "FPCM",
        "Favor Cost Small": "FPCS",
        "Favor Gifts Per Day": "FGPD",
        "Favor travel marker location": "FTML",
        "Female Face Texture Set: Eyes": "FTRF",
        "Female Face Texture Set: Head": "FTHF",
        "Female Face Texture Set: Mouth": "FTMF",
        "Fighters' Guild Faction": "FTGF",
        "Flying Mount - Allowed Spells": "FMYS",
        "Flying Mount - Disallowed Spells": "FMNS",
        "Flying Mount - Fly Fast Worldspaces": "FMFF",
        "Footstep Set": "DFTS",
        "FormList - Hair Color List": "HCLL",
        "Furniture Test NPC": "FTNP",
        "Gold": "GOLD",
        "Guard Faction": "GFAC",
        "Harvest Failed Sound": "HVFS",
        "Harvest Sound": "HVSS",
        "Heartbeat Sound Fast": "HFSD",
        "Heartbeat Sound Slow": "HSSD",
        "Help - Attack Target": "HBAT",
        "Help - Barter": "HBBR",
        "Help - Basic Alchemy": "HBAL",
        "Help - Basic Cooking": "HBCO",
        "Help - Basic Enchanting": "HBEC",
        "Help - Basic Forging": "HBFG",
        "Help - Basic Lockpicking (Console)": "HBLX",
        "Help - Basic Lockpicking (PC)": "HBLK",
        "Help - Basic Object Creation": "HBOC",
        "Help - Basic Smelting": "HBML",
        "Help - Basic Smithing Armor": "HBSA",
        "Help - Basic Smithing Weapon": "HBSM",
        "Help - Basic Tanning": "HBTA",
        "Help - Favorites": "HBFS",
        "Help - Flying Mount": "HBFM",
        "Help - Jail": "HBHJ",
        "Help - Journal": "HBJL",
        "Help - Leveling up": "HBLU",
        "Help - Low Health": "HBLH",
        "Help - Low Magicka": "HBLM",
        "Help - Low Stamina": "HBLS",
        "Help - Map Menu": "HBMM",
        "Help - Skills Menu": "HBSK",
        "Help - Target Lock": "HBTL",
        "Help - Teamate Favor": "HBFT",
        "Help - Weapon Charge": "HBWC",
        "Help Manual PC": "HMPC",
        "Help Manual XBox": "HMXB",
        "Imagespace - Load screen": "LSIS",
        "Imagespace - Low Health": "IMLH",
        "ImageSpaceModifier for inventory menu.": "IMID",
        "Interface Output Model": "IOPM",
        "Inventory Player": "INVP",
        "Jarl Faction": "JRLF",
        "Keyword - Activator Furniture No Player": "AFNP",
        "Keyword - Animal": "ANML",
        "Keyword - Armor Material Daedric": "AODA",
        "Keyword - Armor Material Dragonbone": "AODB",
        "Keyword - Armor Material Dragonplate": "AODP",
        "Keyword - Armor Material Dragonscale": "AODS",
        "Keyword - Armor Material Dwarven": "AODW",
        "Keyword - Armor Material Ebony": "AOEB",
        "Keyword - Armor Material Elven": "AOEL",
        "Keyword - Armor Material ElvenSplinted": "AOES",
        "Keyword - Armor Material FullLeather": "AOFL",
        "Keyword - Armor Material Glass": "AOGL",
        "Keyword - Armor Material Heavy Bonemold": "AHBM",
        "Keyword - Armor Material Heavy Chitin": "AHCH",
        "Keyword - Armor Material Heavy Nordic": "AHNC",
        "Keyword - Armor Material Heavy Stalhrim": "AHSM",
        "Keyword - Armor Material Hide": "AOHI",
        "Keyword - Armor Material Imperial": "AOIM",
        "Keyword - Armor Material ImperialHeavy": "AOIH",
        "Keyword - Armor Material ImperialReinforced": "AOIR",
        "Keyword - Armor Material Iron": "AOFE",
        "Keyword - Armor Material IronBanded": "AOIB",
        "Keyword - Armor Material Light Bonemold": "ALBM",
        "Keyword - Armor Material Light Chitin": "ALCH",
        "Keyword - Armor Material Light Nordic": "ALNC",
        "Keyword - Armor Material Light Stalhrim": "ALSM",
        "Keyword - Armor Material Orcish": "AOOR",
        "Keyword - Armor Material Scaled": "AOSC",
        "Keyword - Armor Material Steel": "AOST",
        "Keyword - Armor Material SteelPlate": "AOSP",
        "Keyword - Armor Material Stormcloak": "AOSK",
        "Keyword - Armor Material Studded": "AOSD",
        "Keyword - BeastRace": "KWBR",
        "Keyword - Civil War Neutral": "CWNE",
        "Keyword - Civil War Owner": "CWOK",
        "Keyword - ClearableLocation": "KWDO",
        "Keyword - Conditional Explosion": "COEX",
        "Keyword - Cooking Pot": "COOK",
        "Keyword - Cuirass": "KWCU",
        "Keyword - Daedra": "DAED",
        "Keyword - Disallow Enchanting": "DIEN",
        "Keyword - Dragon": "DRAK",
        "Keyword - DummyObject": "KWDM",
        "Keyword - Forge": "FORG",
        "Keyword - Furniture Forces 1st Person": "FFFP",
        "Keyword - Furniture Forces 3rd Person": "FFTP",
        "Keyword - Generic Craftable Keyword 01": "GCK1",
        "Keyword - Generic Craftable Keyword 02": "GCK2",
        "Keyword - Generic Craftable Keyword 03": "GCK3",
        "Keyword - Generic Craftable Keyword 04": "GCK4",
        "Keyword - Generic Craftable Keyword 05": "GCK5",
        "Keyword - Generic Craftable Keyword 06": "GCK6",
        "Keyword - Generic Craftable Keyword 07": "GCK7",
        "Keyword - Generic Craftable Keyword 08": "GCK8",
        "Keyword - Generic Craftable Keyword 09": "GCK9",
        "Keyword - Generic Craftable Keyword 10": "GCKX",
        "Keyword - Hold Location": "LKHO",
        "Keyword - Horse": "HRSK",
        "Keyword - Jewelry": "JWLR",
        "Keyword - Mount": "MNT2",
        "Keyword - Movable": "MVBL",
        "Keyword - MustStop": "KWMS",
        "Keyword - Nirnroot": "NRNT",
        "Keyword - NPC": "NPCK",
        "Keyword - Reusable SoulGem": "RUSG",
        "Keyword - Robot": "BEEP",
        "Keyword - Scale Actor To 1.0": "SAT1",
        "Keyword - Skip Outfit Items": "KWOT",
        "Keyword - Smelter": "SMLT",
        "Keyword - Special Furniture": "SPFK",
        "Keyword - Tanning Rack": "TANN",
        "Keyword - Type Ammo": "TKAM",
        "Keyword - Type Armor": "TKAR",
        "Keyword - Type Book": "TKBK",
        "Keyword - Type Ingredient": "TKIG",
        "Keyword - Type Key": "TKKY",
        "Keyword - Type Misc": "TKMS",
        "Keyword - Type Potion": "TKPT",
        "Keyword - Type SoulGem": "TKSG",
        "Keyword - Type Weapon": "TKWP",
        "Keyword - Undead": "UNDK",
        "Keyword - UpdateDuringArchery": "KWUA",
        "Keyword - UseGeometryEmitter": "KWGE",
        "Keyword - Vampire": "VAMP",
        "Keyword - Weapon Material Daedric": "WMDA",
        "Keyword - Weapon Material Draugr": "WMDR",
        "Keyword - Weapon Material DraugrHoned": "WMDH",
        "Keyword - Weapon Material Dwarven": "WMDW",
        "Keyword - Weapon Material Ebony": "WMEB",
        "Keyword - Weapon Material Elven": "WMEL",
        "Keyword - Weapon Material Falmer": "WMFA",
        "Keyword - Weapon Material FalmerHoned": "WMFH",
        "Keyword - Weapon Material Glass": "WMGL",
        "Keyword - Weapon Material Imperial": "WMIM",
        "Keyword - Weapon Material Iron": "WMIR",
        "Keyword - Weapon Material Nordic": "WPNC",
        "Keyword - Weapon Material Orcish": "WMOR",
        "Keyword - Weapon Material Stalhrim": "WPSM",
        "Keyword - Weapon Material Steel": "WMST",
        "Keyword - Weapon Material Wood": "WMWO",
        "Keyword - WeaponTypeBoundArrow": "WTBA",
        "Kinect Help FormList": "KHFL",
        "Landscape Material": "DLMT",
        "LeftHand Equip": "LHEQ",
        "Level Up Music": "LUMS",
        "Local Map Hide Plane": "LMHP",
        "Lockpick": "LKPK",
        "LocRefType - Civil War Soldier": "LRSO",
        "LocRefType - Resource Destructible": "LRRD",
        "LocRefType Boss": "LRTB",
        "Mages' Guild Faction": "MGGF",
        "Magic Fail Sound": "MFSN",
        "Main Menu Cell": "MMCL",
        "Male Face Texture Set: Eyes": "FTEL",
        "Male Face Texture Set: Head": "FTHD",
        "Male Face Texture Set: Mouth": "FTMO",
        "Map Menu Looping Sound": "MMSD",
        "Master Sound Category": "MTSC",
        "Music Sound Category": "MDSC",
        "No-Activation Sound": "NASD",
        "Non-Dialogue Voice Category": "NDSC",
        "Package template": "PTEM",
        "Pathing Test NPC": "PTNP",
        "Pause During Loading Menu Category": "PDLC",
        "Pause During Menu Category (Fade)": "PDMC",
        "Pause During Menu Category (Immediate)": "PIMC",
        "PersistAll Location": "PLOC",
        "Pickup Sound Armor": "PUSA",
        "Pickup Sound Book": "PUSB",
        "Pickup Sound Generic": "PUSG",
        "Pickup Sound Ingredient": "PUSI",
        "Pickup Sound Weapon": "PUSW",
        "Player Can Mount Dragon Here List": "PCMD",
        "Player Faction": "PFAC",
        "Player Is Vampire Variable": "PIVV",
        "Player Is Werewolf Variable": "PIWV",
        "Player Voice (Female Child)": "PVFC",
        "Player Voice (Female)": "PVFA",
        "Player Voice (Male Child)": "PVMC",
        "Player Voice (Male)": "PVMA",
        "Player's Output Model (1st Person)": "POPM",
        "Player's Output Model (3rd Person)": "P3OM",
        "PotentialFollower Faction": "PTFR",
        "Potion Equip": "POEQ",
        "Putdown Sound Armor": "PDSA",
        "Putdown Sound Book": "PDSB",
        "Putdown Sound Generic": "PDSG",
        "Putdown Sound Ingredient": "PDSI",
        "Putdown Sound Weapon": "PDSW",
        "Reverb Type": "RVBT",
        "RightHand Equip": "RHEQ",
        "Road Marker": "NMRD",
        "SFX To Fade In Dialogue Category": "SFDC",
        "Shout Fail Sound": "SFSN",
        "Sitting Angle Limit": "SALT",
        "SkeletonKey": "SKLK",
        "Skyrim - Worldspace": "KWSP",
        "Snow LOD Material (HD)": "SLHD",
        "Snow LOD Material": "SLDM",
        "Soul Captured Sound": "SCSD",
        "Stats Music": "SSSC",
        "Stats Mute Category": "SMSC",
        "Success Music": "SCMS",
        "Telekinesis Grab Sound": "TKGS",
        "Telekinesis Throw Sound": "TKTS",
        "Thieves' Guild Faction": "TVGF",
        "Time Sensitive Sound Category": "TSSC",
        "Underwater Loop Sound": "UWLS",
        "Underwater Reverb Type": "URVT",
        "Vampire Available Perks": "AVVP",
        "Vampire Feed No Crime Faction": "VFNC",
        "Vampire Race": "RIVR",
        "Vampire Spells": "RIVS",
        "Verlet Cape": "AIVC",
        "Virtual Location": "VLOC",
        "Voice Equip": "VOEQ",
        "Wait-For-Dialogue Package": "PWFD",
        "Ward Absorb Sound": "WASN",
        "Ward Break Sound": "WBSN",
        "Ward Deflect Sound": "WDSN",
        "Weapon Material List": "WEML",
        "Werewolf Available Perks": "AVWP",
        "Werewolf Race": "RIWR",
        "Werewolf Spell": "WWSP",
        "World Map Weather": "WMWE",
        }
        return items

class PapyrusSkseActorValueInfoNameSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
    def get_items(self, **args):
        items = {
        "Absorb chance": "AbsorbChance",
        "Aggression": "Aggression",
        "Alchemy modifier": "AlchemyMod",
        "Alchemy power modifier": "AlchemyPowerMod",
        "Alchemy skill advance": "AlchemySkillAdvance",
        "Alchemy": "Alchemy",
        "Alteration modifier": "AlterationMod",
        "Alteration power modifier": "AlterationPowerMod",
        "Alteration skill advance": "AlterationSkillAdvance",
        "Alteration": "Alteration",
        "Armor perks": "ArmorPerks",
        "Assistance": "Assistance",
        "Attack damage multiplier": "AttackDamageMult",
        "Blindness": "Blindness",
        "Block modifier": "BlockMod",
        "Block power modifier": "BlockPowerMod",
        "Block skill advance": "BlockSkillAdvance",
        "Block": "Block",
        "Bow speed bonus": "BowSpeedBonus",
        "Bow stagger bonus": "BowStaggerBonus",
        "Brain condition": "BrainCondition",
        "Bypass vendor keyword check": "BypassVendorKeywordCheck",
        "Bypass vendor stolen check": "BypassVendorStolenCheck",
        "Carry weight": "CarryWeight",
        "Combat health regeneration multiplier modifier": "CombatHealthRegenMultMod",
        "Combat health regeneration multiplier power modifier": "CombatHealthRegenMultPowerMod",
        "Combat health regeneration multiplier": "CombatHealthRegenMult",
        "Confidence": "Confidence",
        "Conjuration modifier": "ConjurationMod",
        "Conjuration power modifier": "ConjurationPowerMod",
        "Conjuration skill advance": "ConjurationSkillAdvance",
        "Conjuration": "Conjuration",
        "Critical chance": "CritChance",
        "Damage resistance": "DamageResist",
        "Destruction modifier": "DestructionMod",
        "Destruction power modifier": "DestructionPowerMod",
        "Destruction skill advance": "DestructionSkillAdvance",
        "Destruction": "Destruction",
        "Detect life range": "DetectLifeRange",
        "Dragon Rend": "DragonRend",
        "Dragon souls": "DragonSouls",
        "Enchanting modifier": "EnchantingMod",
        "Enchanting power modifier": "EnchantingPowerMod",
        "Enchanting skill advance": "EnchantingSkillAdvance",
        "Enchanting": "Enchanting",
        "Endurance condition": "EnduranceCondition",
        "Energy": "Energy",
        "Equipped item charge": "EquippedItemCharge",
        "Equipped staff charge": "EquippedStaffCharge",
        "Fame": "Fame",
        "Favor active": "FavorActive",
        "Favor points bonus": "FavorPointsBonus",
        "Favors per day timer": "FavorsPerDayTimer",
        "Favors per day": "FavorsPerDay",
        "Fire resistance": "FireResist",
        "Frost resistance": "FrostResist",
        "Grab actor offset": "GrabActorOffset",
        "Grabbed": "Grabbed",
        "Heal rate power modifier": "HealRatePowerMod",
        "Heal rate": "HealRate",
        "Health": "Health",
        "Heavy armor modifier": "HeavyArmorMod",
        "Heavy armor power modifier": "HeavyArmorPowerMod",
        "Heavy armor skill advance": "HeavyArmorSkillAdvance",
        "Heavy armor": "HeavyArmor",
        "Ignore crippled limbs": "IgnoreCrippleLimbs",
        "Illusion modifier": "IllusionMod",
        "Illusion power modifier": "IllusionPowerMod",
        "Illusion skill advance": "IllusionSkillAdvance",
        "Infamy": "Infamy",
        "Inventory weight": "InventoryWeight",
        "Invisibility": "Invisibility",
        "Jumping bonus": "JumpingBonus",
        "Last bribed or intimidated": "LastBribedIntimidated",
        "Last flattered": "LastFlattered",
        "Left attack condition": "LeftAttackCondition",
        "Left mobility condition": "LeftMobilityCondition",
        "Left weapon speed multiplier": "LeftWeaponSpeedMult",
        "Light armor modifier": "LightArmorMod",
        "Light armor power modifier": "LightArmorPowerMod",
        "Light armor skill advance": "LightArmorSkillAdvance",
        "Light armor": "LightArmor",
        "Lockpicking modifier": "LockPickingMod",
        "Lockpicking power modifier": "LockPickingPowerMod",
        "Lockpicking skill advance": "LockPickingSkillAdvance",
        "Lockpicking": "LockPicking",
        "Magic resistance": "MagicResist",
        "Magicka rate modifier": "MagickaRateMod",
        "Magicka rate": "MagickaRate",
        "Magicka": "Magicka",
        "Marksman modifier": "MarksmanMod",
        "Marksman power modifier": "MarksmanPowerMod",
        "Marksman skill advance": "MarksmanSkillAdvance",
        "Marksman": "Marksman",
        "Mass": "Mass",
        "Melee damage": "MeleeDamage",
        "Mood": "Mood",
        "Morality": "Morality",
        "Muffled": "Muffled",
        "Mysticism": "Mysticism",
        "Night eye": "NightEye",
        "Normal weapon resistance": "NormalWeaponsResist",
        "One-handed modifier": "OneHandedMod",
        "One-handed power modifier": "OneHandedPowerMod",
        "One-handed skill advance": "OneHandedSkillAdvance",
        "One-handed": "OneHanded",
        "Paralysis": "Paralysis",
        "Perception condition": "PerceptionCondition",
        "Pickpocket modifier": "PickPocketMod",
        "Pickpocket power modifier": "PickPocketPowerMod",
        "Pickpocket skill advance": "PickPocketSkillAdvance",
        "Pickpocket": "Pickpocket",
        "Poison resistance": "PoisonResist",
        "Restoration modifier": "RestorationMod",
        "Restoration power modifier": "RestorationPowerMod",
        "Restoration skill advance": "RestorationSkillAdvance",
        "Restoration": "Restoration",
        "Right attack condition": "RightAttackCondition",
        "Right mobility condition": "RightMobilityCondition",
        "Shield perks": "ShieldPerks",
        "Shock resistance": "ElectricResist",
        "Shout recovery multiplier": "ShoutRecoveryMult",
        "Smithing modifier": "SmithingMod",
        "Smithing power modifier": "SmithingPowerMod",
        "Smithing skill advance": "SmithingSkillAdvance",
        "Smithing": "Smithing",
        "Sneak modifier": "SneakMod",
        "Sneak power modifier": "SneakPowerMod",
        "Sneak skill advance": "SneakSkillAdvance",
        "Sneak": "Sneak",
        "Speech modifier": "SpeechcraftMod",
        "Speech power modifier": "SpeechcraftPowerMod",
        "Speech skill advance": "SpeechcraftSkillAdvance",
        "Speech": "SpeechCraft",
        "Speed multiplier": "SpeedMult",
        "Stamina rate multiplier": "StaminaRateMult",
        "Stamina rate": "StaminaRate",
        "Stamina": "Stamina",
        "Telekinesis": "Telekinesis",
        "Two-handed modifier": "TwoHandedMod",
        "Two-handed power modifier": "TwoHandedPowerMod",
        "Two-handed skill advance": "TwoHandedSkillAdvance",
        "Two-handed": "TwoHanded",
        "Unarmed damage": "UnarmedDamage",
        "Variable 01": "Variable01",
        "Variable 02": "Variable02",
        "Variable 03": "Variable03",
        "Variable 04": "Variable04",
        "Variable 05": "Variable05",
        "Variable 06": "Variable06",
        "Variable 07": "Variable07",
        "Variable 08": "Variable08",
        "Variable 09": "Variable09",
        "Variable 10": "Variable10",
        "Voice points": "VoicePoints",
        "Voice rate": "VoiceRate",
        "Waiting for player": "WaitingForPlayer",
        "Ward deflection": "WardDeflection",
        "Ward power": "WardPower",
        "Water breathing": "WaterBreathing",
        "Water walking": "WaterWalking",
        "Weapon speed multiplier": "WeaponSpeedMult",
        "Reflect damage": "ReflectDamage"
        }
        return items

class PapyrusSkseActorValueInfoIdSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
    def get_items(self, **args):
        items = {
        "Absorb chance": 83,
        "Aggression": 0,
        "Alchemy modifier": 106,
        "Alchemy power modifier": 145,
        "Alchemy skill advance": 124,
        "Alchemy": 16,
        "Alteration modifier": 108,
        "Alteration power modifier": 147,
        "Alteration skill advance": 126,
        "Alteration": 18,
        "Armor perks": 65,
        "Assistance": 5,
        "Attack damage multiplier": 154,
        "Blindness": 84,
        "Block modifier": 99,
        "Block power modifier": 138,
        "Block skill advance": 117,
        "Block": 9,
        "Bow speed bonus": 78,
        "Bow stagger bonus": 87,
        "Brain condition": 52,
        "Bypass vendor keyword check": 94,
        "Bypass vendor stolen check": 93,
        "Carry weight": 32,
        "Combat health regeneration multiplier modifier": 155,
        "Combat health regeneration multiplier power modifier": 156,
        "Combat health regeneration multiplier": 134,
        "Confidence": 1,
        "Conjuration modifier": 109,
        "Conjuration power modifier": 148,
        "Conjuration skill advance": 127,
        "Conjuration": 19,
        "Critical chance": 33,
        "Damage resistance": 39,
        "Destruction modifier": 110,
        "Destruction power modifier": 149,
        "Destruction skill advance": 128,
        "Destruction": 20,
        "Detect life range": 56,
        "Dragon Rend": 153,
        "Dragon souls": 133,
        "Enchanting modifier": 113,
        "Enchanting power modifier": 152,
        "Enchanting skill advance": 131,
        "Enchanting": 23,
        "Endurance condition": 47,
        "Energy": 2,
        "Equipped item charge": 64,
        "Equipped staff charge": 82,
        "Fame": 60,
        "Favor active": 79,
        "Favor points bonus": 89,
        "Favors per day timer": 81,
        "Favors per day": 80,
        "Fire resistance": 41,
        "Frost resistance": 43,
        "Grab actor offset": 160,
        "Grabbed": 161,
        "Heal rate power modifier": 158,
        "Heal rate": 27,
        "Health": 24,
        "Heavy armor modifier": 101,
        "Heavy armor power modifier": 140,
        "Heavy armor skill advance": 119,
        "Heavy armor": 11,
        "Ignore crippled limbs": 59,
        "Illusion modifier": 111,
        "Illusion power modifier": 150,
        "Illusion skill advance": 129,
        "Infamy": 61,
        "Inventory weight": 31,
        "Invisibility": 54,
        "Jumping bonus": 62,
        "Last bribed or intimidated": 90,
        "Last flattered": 91,
        "Left attack condition": 48,
        "Left mobility condition": 50,
        "Left weapon speed multiplier": 132,
        "Light armor modifier": 102,
        "Light armor power modifier": 141,
        "Light armor skill advance": 120,
        "Light armor": 12,
        "Lockpicking modifier": 104,
        "Lockpicking power modifier": 143,
        "Lockpicking skill advance": 122,
        "Lockpicking": 14,
        "Magic resistance": 44,
        "Magicka rate modifier": 159,
        "Magicka rate": 28,
        "Magicka": 25,
        "Marksman modifier": 98,
        "Marksman power modifier": 137,
        "Marksman skill advance": 116,
        "Marksman": 8,
        "Mass": 36,
        "Melee damage": 34,
        "Mood": 4,
        "Morality": 3,
        "Muffled": 92,
        "Mysticism": 21,
        "Night eye": 55,
        "Normal weapon resistance": 45,
        "One-handed modifier": 96,
        "One-handed power modifier": 135,
        "One-handed skill advance": 114,
        "One-handed": 6,
        "Paralysis": 53,
        "Perception condition": 46,
        "Pickpocket modifier": 103,
        "Pickpocket power modifier": 142,
        "Pickpocket skill advance": 121,
        "Pickpocket": 13,
        "Poison resistance": 40,
        "Reflect damage": 163,
        "Restoration modifier": 112,
        "Restoration power modifier": 151,
        "Restoration skill advance": 130,
        "Restoration": 22,
        "Right attack condition": 49,
        "Right mobility condition": 51,
        "Shield perks": 66,
        "Shock resistance": 42,
        "Shout recovery multiplier": 86,
        "Smithing modifier": 100,
        "Smithing power modifier": 139,
        "Smithing skill advance": 118,
        "Smithing": 10,
        "Sneak modifier": 105,
        "Sneak power modifier": 144,
        "Sneak skill advance": 123,
        "Sneak": 15,
        "Speech modifier": 107,
        "Speech power modifier": 146,
        "Speech skill advance": 125,
        "Speech": 17,
        "Speed multiplier": 30,
        "Stamina rate multiplier": 157,
        "Stamina rate": 29,
        "Stamina": 26,
        "Telekinesis": 88,
        "Two-handed modifier": 97,
        "Two-handed power modifier": 136,
        "Two-handed skill advance": 115,
        "Two-handed": 7,
        "Unarmed damage": 35,
        "Variable 01": 68,
        "Variable 02": 69,
        "Variable 03": 70,
        "Variable 04": 71,
        "Variable 05": 72,
        "Variable 06": 73,
        "Variable 07": 74,
        "Variable 08": 75,
        "Variable 09": 76,
        "Variable 10": 77,
        "Voice points": 37,
        "Voice rate": 38,
        "Waiting for player": 95,
        "Ward deflection": 67,
        "Ward power": 63,
        "Water breathing": 57,
        "Water walking": 58,
        "Weapon speed multiplier": 85
        #162: "Cannot find the name of this AVI",
        }
        return items