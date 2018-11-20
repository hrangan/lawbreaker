import random


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

    @classmethod
    def get_traits(cls):
        return {"physique": random.choice(cls.physique).lower(),
                "face": random.choice(cls.face).lower(),
                "skin": random.choice(cls.skin).lower(),
                "hair": random.choice(cls.hair).lower(),
                "clothing": random.choice(cls.clothing).lower(),
                "virtue": random.choice(cls.virtues).lower(),
                "vice": random.choice(cls.vices).lower(),
                "speech": random.choice(cls.speech).lower(),
                "background": random.choice(cls.background).lower(),
                "misfortune": random.choice(cls.misfortunes).lower(),
                "alignment": random.choice(cls.alignment).lower()}

    @classmethod
    def format_traits(cls, name):
        choices = cls.get_traits()
        description_strings = ["  - Has a {physique} physique, a {face} face, {skin} skin and {hair} hair."
                               "\n  - Clothes are {clothing}, and speech {speech}."
                               "\n  - Is {virtue}, but {vice}."
                               "\n  - Has been a {background} in the past. Has been {misfortune} in the past."
                               "\n  - Favours {alignment}."]
        description = "".join(description_strings).format(name=name, **choices)
        return '\n'.join(['Description:', '-'*12, description])
