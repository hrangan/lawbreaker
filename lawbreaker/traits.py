import random
from collections import OrderedDict


class Traits(object):

    physique = ["Athletic", "Brawny", "Corpulent", "Delicate", "Gaunt", "Hulking", "Lanky", "Ripped",
                "Rugged", "Scrawny", "Short", "Sinewy", "Slender", "Flabby", "Statuesque", "Stout",
                "Tiny", "Towering", "Willowy", "Wiry"]
    face = ["Bloated", "Blunt", "Bony", "Chiseled", "Delicate", "Elongated", "Patrician", "Pinched",
            "Hawkish", "Broken", "Impish", "Narrow", "Ratlike", "Round", "Sunken", "Sharp", "Soft",
            "Square", "Wide", "Wolfish"]
    skin = ["Battle Scar", "Birthmark", "Burn Scar", "Dark", "Makeup", "Oily", "Pale", "Perfect",
            "Pierced", "Pockmarked", "Reeking", "Tattooed", "Rosy", "Rough", "Sallow", "Sunburned",
            "Tanned", "War Paint", "Weathered", "Whip Scar"]
    hair = ["Bald", "Braided", "Bristly", "Cropped", "Curly", "Disheveled", "Dreadlocks", "Filthy",
            "Frizzy", "Greased", "Limp", "Long", "Luxurious", "Mohawk", "Oily", "Ponytail", "Silky",
            "Topknot", "Wavy", "Wispy"]
    clothing = ["Antique", "Bloody", "Ceremonial", "Decorated", "Eccentric", "Elegant", "Fashionable",
                "Filthy", "Flamboyant", "Stained", "Foreign", "Frayed", "Frumpy", "Livery", "Oversized",
                "Patched", "Perfumed", "Rancid", "Torn", "Undersized"]
    virtues = ["Ambitious", "Cautious", "Courageous", "Courteous", "Curious", "Disciplined", "Focused",
               "Generous", "Gregarious", "Honest", "Honorable", "Humble", "Idealistic", "Just", "Loyal",
               "Merciful", "Righteous", "Serene", "Stoic", "Tolerant"]
    vices = ["Aggressive", "Arrogant", "Bitter", "Cowardly", "Cruel", "Deceitful", "Flippant", "Gluttonous",
             "Greedy", "Irascible", "Lazy", "Nervous", "Prejudiced", "Reckless", "Rude", "Suspicious", "Vain",
             "Vengeful", "Wasteful", "Whiny"]
    speech = ["Blunt", "Booming", "Breathy", "Cryptic", "Drawling", "Droning", "Flowery", "Formal",
              "Gravelly", "Hoarse", "Mumbling", "Precise", "Quaint", "Rambling", "Rapid-fire", "Dialect",
              "Slow", "Squeaky", "Stuttering", "Whispery"]
    background = ["Alchemist", "Beggar", "Butcher", "Burglar", "Charlatan", "Cleric", "Cook", "Cultist",
                  "Gambler", "Herbalist", "Magician", "Mariner", "Mercenary", "Merchant", "Outlaw",
                  "Performer", "Pickpocket", "Smuggler", "Student", "Tracker"]
    misfortunes = ["Abandoned", "Addicted", "Blackmailed", "Condemned", "Cursed", "Defrauded", "Demoted",
                   "Discredited", "Disowned", "Exiled", "Framed", "Haunted", "Kidnapped", "Mutilated",
                   "Poor", "Pursued", "Rejected", "Replaced", "Robbed", "Suspected"]
    alignment = ["Law", "Law", "Law", "Law", "Law",
                 "Neutrality", "Neutrality", "Neutrality", "Neutrality", "Neutrality",
                 "Neutrality", "Neutrality", "Neutrality", "Neutrality", "Neutrality",
                 "Chaos", "Chaos", "Chaos", "Chaos", "Chaos"]

    def __init__(self):
        self.traits = OrderedDict([("physique", random.choice(Traits.physique).lower()),
                                   ("face", random.choice(Traits.face).lower()),
                                   ("skin", random.choice(Traits.skin).lower()),
                                   ("hair", random.choice(Traits.hair).lower()),
                                   ("clothing", random.choice(Traits.clothing).lower()),
                                   ("virtue", random.choice(Traits.virtues).lower()),
                                   ("vice", random.choice(Traits.vices).lower()),
                                   ("speech", random.choice(Traits.speech).lower()),
                                   ("background", random.choice(Traits.background)),
                                   ("misfortune", random.choice(Traits.misfortunes).lower()),
                                   ("alignment", random.choice(Traits.alignment).lower())
                                   ]
                                  )

    def __str__(self):

        description_string = ("Traits\n"
                              "--------------------------------------------------\n"
                              "{background}.  Wears {clothing} clothes, and has {speech} speech.\n"
                              "Has a {physique} physique, a {face} face, {skin} skin and {hair} hair.\n"
                              "Is {virtue}, but {vice}. Has been {misfortune} in the past.\n"
                              "Favours {alignment}.")
        return description_string.format(**self.traits)
