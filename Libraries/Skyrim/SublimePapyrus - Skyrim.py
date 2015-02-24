import sublime, sublime_plugin, sys
PYTHON_VERSION = sys.version_info
if PYTHON_VERSION[0] == 3:
    from SublimePapyrus import SublimePapyrus

    class PapyrusSkyrimActorValueSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
        def get_items(self, **args):
            items = {
            "Health": "Health",
			"Magicka": "Magicka",
			"Stamina": "Stamina",
			"OneHanded": "One-handed",
			"TwoHanded": "Two-handed",
			"Marksman": "Marksman",
			"Block": "Block",
			"Smithing": "Smithing",
			"HeavyArmor": "Heavy armor",
			"LightArmor": "Light armor",
			"Pickpocket": "Pickpocket",
			"Lockpicking": "Lockpicking",
			"Sneak": "Sneak",
			"Alchemy": "Alchemy",
			"Speechcraft": "Speech",
			"Alteration": "Alteration",
			"Conjuration": "Conjuration",
			"Destruction": "Destruction",
			"Illusion": "Illusion",
			"Restoration": "Restoration",
			"Enchanting": "Enchanting",
			"Aggression": "Aggression",
			"Confidence": "Confidence",
			"Energy": "Energy",
			"Morality": "Morality",
			"Mood": "Mood",
			"Assistance": "Assistance",
			"WaitingForPlayer": "Waiting for player",
			"HealRate": "Heal rate",
			"MagickaRate": "Magicka rate",
			"StaminaRate": "Stamina rate",
			"AttackDamageMult": "Attack damage multiplier",
			"SpeedMult": "Speed multiplier",
			"ShoutRecoveryMult": "Shout recovery multiplier",
			"WeaponSpeedMult": "Weapon speed multiplier",
			"DestructionMod": "Destruction modifier",
			"DestructionPowerMod": "Destruction power modifier",
			"AlterationMod": "Alteration modifier",
			"AlterationPowerMod": "Alteration power modifier",
			"IllusionMod": "Illusion modifier",
			"IllusionPowerMod": "Illusion power modifier",
			"RestorationMod": "Restoration modifier",
			"RestorationPowerMod": "Restoration power modifier",
			"ConjurationMod": "Conjuration modifier",
			"ConjurationPowerMod": "Conjuration power modifier",
			"InventoryWeight": "Inventory weight",
			"CarryWeight": "Carry weight",
			"CritChance": "Critical chance",
			"MeleeDamage": "Melee damage",
			"UnarmedDamage": "Unarmed damage",
			"Mass": "Mass",
			"VoicePoints": "Voice points",
			"VoiceRate": "Voice rate",
			"DamageResist": "Damage resistance",
			"DiseaseResist": "Disease resistance",
			"PoisonResist": "Poison resistance",
			"FireResist": "Fire resistance",
			"ElectricResist": "Shock resistance",
			"FrostResist": "Frost resistance",
			"MagicResist": "Magic resistance",
			"Paralysis": "Paralysis",
			"Invisibility": "Invisibility",
			"NightEye": "Night eye",
			"DetectLifeRange": "Detect life range",
			"WaterBreathing": "Water breating",
			"WaterWalking": "Water walking",
			"JumpingBonus": "Jumping bonus",
			"WardPower": "Ward power",
			"WardDeflection": "Ward deflection",
			"EquippedItemCharge": "Equipped item charge",
			"EquippedStaffCharge": "Equipped staff charge",
			"ArmorPerks": "Armor perks",
			"ShieldPerks": "Shield perks",
			"BowSpeedBonus": "Bow speed bonus",
			"DragonSouls": "Dragon souls",
			"Variable01": "Variable 01",
			"Variable02": "Variable 02",
			"Variable03": "Variable 03",
			"Variable04": "Variable 04",
			"Variable05": "Variable 05",
			"Variable06": "Variable 06",
			"Variable07": "Variable 07",
			"Variable08": "Variable 08",
			"Variable09": "Variable 09",
			"Variable10": "Variable 10",
			"CombatHealthRegenMultMod": "Combat health regeneration multiplier modifier",
			"CombatHealthRegenMultPowerMod": "Combat health regeneration multiplier power modifier",
			"PerceptionCondition": "Perception condition",
			"EnduranceCondition": "Endurance condition",
			"LeftAttackCondition": "Left attack condition",
			"RightAttackCondition": "Right attack condition",
			"LeftMobilityCondition": "Left mobility condition",
			"RightMobilityCondition": "Right mobility condition",
			"BrainCondition": "Brain condition",
			"IgnoreCrippledLimbs": "Ignore crippled limbs",
			"Fame": "Fame",
			"Infamy": "Infamy",
			"FavorActive": "Favor active",
			"FavorPointsBonus": "Favor points bonus",
			"FavorsPerDay": "Favors per day",
			"FavorsPerDayTimer": "Favors per day timer",
			"BypassVendorStolenCheck": "Bypass vendor stolen check",
			"BypassVendorKeywordCheck": "Bypass vendor keyword check",
			"LastBribedIntimidated": "Last bribed or intimidated",
			"LastFlattered": "Last flattered"
            }
            return items

    class PapyrusSkyrimFormTypeSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
        def get_items(self, **args):
        	items = {
        	83: "Animated Object (ANIO)",
			102: "Armor Addon (ARMA)",
			16: "Acoustic Space (ASPC)",
			6: "Action (AACT)",
			24: "Activator (ACTI)",
			95: "ActorValueInfo (AVIF)",
			94: "Addon Node (ADDN)",
			42: "Ammo (AMMO)",
			33: "Apparatus (APPA)",
			26: "Armor (ARMO)",
			64: "Arrow Projectile (PARW)",
			125: "Art Object (ARTO)",
			123: "Association Type (ASTP)",
			69: "Barrier Projectile (PBAR)",
			66: "Beam Projectile (PBEA)",
			93: "Body Part Data (BPTD)",
			27: "Book (BOOK)",
			97: "Camera Path (CPTH)",
			96: "Camera Shot (CAMS)",
			60: "Cell (CELL)",
			62: "Character",
			10: "Class (CLAS)",
			55: "Climate (CLMT)",
			132: "Collision Layer (COLL)",
			133: "Color Form (CLFM)",
			80: "Combat Style (CSTY)",
			68: "Cone/Voice Projectile (PCON)",
			49: "Constructible Object (COBJ)",
			28: "Container (CONT)",
			117: "Dialog View (DLVW)",
			88: "Debris (DEBR)",
			107: "Default Object Manager (DOBJ)",
			115: "Dialogue Branch (DLBR)",
			29: "Door (DOOR)",
			129: "Dual Cast Data (DUAL)",
			18: "Effect Setting",
			85: "Effect Shader (EFSH)",
			21: "Enchantment (ENCH)",
			103: "Encounter Zone (ECZN)",
			120: "Equip Slot (EQUP)",
			87: "Explosion (EXPL)",
			13: "Eyes (EYES)",
			11: "Faction (FACT)",
			67: "Flame Projectile (PLFA)",
			39: "Flora (FLOR)",
			110: "Footstep (FSTP)",
			111: "Footstep Set (FSTS)",
			40: "Furniture (FURN)",
			3: "Game Setting (GMST)",
			9: "Global Variable (GLOB)",
			37: "Grass (GRAS)",
			65: "Grenade Projectile (PGRE)",
			2: "Group (GRUP)",
			51: "Hazard (HAZD)",
			12: "Head Part (HDPT)",
			78: "Idle (IDLE)",
			47: "Idle Marker (IDLM)",
			89: "Image Space (IMGS)",
			90: "Image Space Modifier (IMAD)",
			100: "Impact Data (IPCT)",
			101: "Impact Data Set (IPDS)",
			30: "Ingredient (INGR)",
			45: "Key (KEYM)",
			4: "Keyword (KYWD)",
			72: "Landscape (LAND)",
			20: "Land Texture (LTEX)",
			44: "Leveled Actor (LVLN)",
			53: "Leveled Item (LVLI)",
			82: "Leveled Spell (LVLS)",
			31: "Light (LIGH)",
			108: "Lighting Template (LGTM)",
			91: "FormID List (FLST)",
			81: "Load Screen (LSCR)",
			104: "Location (LCTN)",
			5: "Location Reference Type (LCRT)",
			126: "Material Object (MATO)",
			99: "Material Type (MATT)",
			8: "Menu Icon",
			105: "Message (MESG)",
			32: "Miscellaneous Object (MISC)",
			63: "Missile Projectile (PMIS)",
			36: "Movable Static (MSTT)",
			127: "Movement Type (MOVT)",
			116: "Music Track (MUST)",
			109: "Music Type (MUSC)",
			59: "Navigation (NAVI)",
			43: "Actor (NPC_)",
			73: "Navigation Mesh (NAVM)",
			0: "None",
			48: "Note",
			124: "Outfit (OTFT)",
			70: "Placed Hazard (PHZD)",
			79: "AI Package (PACK)",
			92: "Perk (PERK)",
			46: "Potion (ALCH)",
			50: "Projectile (PROJ)",
			77: "Quest (QUST)",
			14: "Race (RACE)",
			106: "Ragdoll (RGDL)",
			61: "Object Reference (REFR)",
			57: "Visual/Reference Effect (RFCT)",
			58: "Region (REGN)",
			121: "Relationship (RELA)",
			134: "Reverb Parameter (REVB)",
			122: "Scene (SCEN)",
			19: "Script (SCPT)",
			23: "Scroll Item (SCRL)",
			56: "Shader Particle Geometry Data (SPGD)",
			119: "Shout (SHOU)",
			17: "Skill",
			52: "Soul Gem (SLGM)",
			15: "Sound (SOUN)",
			130: "Sound Category (SNCT)",
			128: "Sound Descriptor (SNDR)",
			131: "Sound Output (SOPM)",
			22: "Spell (SPEL)",
			34: "Static (STAT)",
			35: "Static Collection",
			112: "Story Manager Branch Node (SMBN)",
			114: "Story Manager Event Node (SMEN)",
			113: "Story Manager Quest Node (SMQN)",
			1: "Main File Header (TES4)",
			74: " (TLOD)",
			86: " (TOFT)",
			25: "Talking Activator (TACT)",
			7: "Texture Set (TXST)",
			75: "Topic (DIAL)",
			76: "Topic Info (INFO)",
			38: "Tree (TREE)",
			98: "Voice Type (VTYP)",
			84: "Water (WATR)",
			41: "Weapon (WEAP)",
			54: "Weather (WTHR)",
			118: "Word of Power (WOOP)",
			71: "Worldspace (WRLD)"
        	}
        	return items