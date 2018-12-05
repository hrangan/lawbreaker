import random


class Traits(object):

    physique = ["athletic", "brawny", "corpulent", "delicate", "gaunt", "hulking", "lanky", "ripped",
                "rugged", "scrawny", "short", "sinewy", "slender", "flabby", "statuesque", "stout",
                "tiny", "towering", "willowy", "wiry"]
    face = ["bloated", "blunt", "bony", "chiseled", "delicate", "elongated", "patrician", "pinched",
            "hawkish", "broken", "impish", "narrow", "ratlike", "round", "sunken", "sharp", "soft",
            "square", "wide", "wolfish"]
    skin = ["battle scar", "birthmark", "burn scar", "dark", "makeup", "oily", "pale", "perfect",
            "pierced", "pockmarked", "reeking", "tattooed", "rosy", "rough", "sallow", "sunburned",
            "tanned", "war paint", "weathered", "whip scar"]
    hair = ["bald", "braided", "bristly", "cropped", "curly", "disheveled", "dreadlocks", "filthy",
            "frizzy", "greased", "limp", "long", "luxurious", "mohawk", "oily", "ponytail", "silky",
            "topknot", "wavy", "wispy"]
    clothing = ["antique", "bloody", "ceremonial", "decorated", "eccentric", "elegant", "fashionable",
                "filthy", "flamboyant", "stained", "foreign", "frayed", "frumpy", "livery", "oversized",
                "patched", "perfumed", "rancid", "torn", "undersized"]
    virtues = ["ambitious", "cautious", "courageous", "courteous", "curious", "disciplined", "focused",
               "generous", "gregarious", "honest", "honorable", "humble", "idealistic", "just", "loyal",
               "merciful", "righteous", "serene", "stoic", "tolerant"]
    vices = ["aggressive", "arrogant", "bitter", "cowardly", "cruel", "deceitful", "flippant", "gluttonous",
             "greedy", "irascible", "lazy", "nervous", "prejudiced", "reckless", "rude", "suspicious", "vain",
             "vengeful", "wasteful", "whiny"]
    speech = ["blunt", "booming", "breathy", "cryptic", "drawling", "droning", "flowery", "formal",
              "gravelly", "hoarse", "mumbling", "precise", "quaint", "rambling", "rapid-fire", "dialect",
              "slow", "squeaky", "stuttering", "whispery"]
    background = ["alchemist", "beggar", "butcher", "burglar", "charlatan", "cleric", "cook", "cultist",
                  "gambler", "herbalist", "magician", "mariner", "mercenary", "merchant", "outlaw",
                  "performer", "pickpocket", "smuggler", "student", "tracker"]
    misfortunes = ["abandoned", "addicted", "blackmailed", "condemned", "cursed", "defrauded", "demoted",
                   "discredited", "disowned", "exiled", "framed", "haunted", "kidnapped", "mutilated",
                   "poor", "pursued", "rejected", "replaced", "robbed", "suspected"]
    alignment = ["law", "law", "law", "law", "law",
                 "neutrality", "neutrality", "neutrality", "neutrality", "neutrality",
                 "neutrality", "neutrality", "neutrality", "neutrality", "neutrality",
                 "chaos", "chaos", "chaos", "chaos", "chaos"]

    def __init__(self):
        self.traits = {"physique": random.choice(Traits.physique),
                       "face": random.choice(Traits.face),
                       "skin": random.choice(Traits.skin),
                       "hair": random.choice(Traits.hair),
                       "clothing": random.choice(Traits.clothing),
                       "virtue": random.choice(Traits.virtues),
                       "vice": random.choice(Traits.vices),
                       "speech": random.choice(Traits.speech),
                       "background": random.choice(Traits.background),
                       "misfortune": random.choice(Traits.misfortunes),
                       "alignment": random.choice(Traits.alignment)}

    def __str__(self):
        description_string = ("Traits\n"
                              "--------------------------------------------------\n"
                              "A {background}. Wears {clothing} clothes, and has {speech} speech.\n"
                              "Has a {physique} physique, a {face} face, {skin} skin and {hair} hair.\n"
                              "Is {virtue}, but {vice}. Has been {misfortune} in the past.\n"
                              "Favours {alignment}.")
        return description_string.format(**self.traits)
