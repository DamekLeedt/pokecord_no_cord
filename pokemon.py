import random

# HP, Attack, Defense, SPATK, SPDEF, Speed
NATURES = {
    "adamant": (1, 3),
    "bashful": (3, 3),
    "bold": (2, 1),
    "brave": (1, 5),
    "calm": (4, 1),
    "careful": (4, 3),
    "docile": (2, 2),
    "gentle": (4, 2),
    "hardy": (1, 1),
    "hasty": (5, 2),
    "impish": (2, 3),
    "jolly": (5, 3),
    "lax": (2, 4),
    "lonely": (1, 2),
    "mild": (3, 2),
    "modest": (3, 1),
    "naive": (5, 4),
    "naughty": (1, 4),
    "quiet": (3, 5),
    "quirky": (4, 4),
    "rash": (3, 4),
    "relaxed": (2, 5),
    "sassy": (4, 5),
    "serious": (5, 5),
    "timid": (5, 1)
}

class SimPokemon:
    
    """
    HP = ((2*Base + IV + 100) * Level) / 100 + 10
    Stat = (((2*Base + IV) * Level) / 100 + 5) * NATURE
    """
    
    def __init__(self, dex_num = 151, name = "Mew", level=100, ivs=[0,0,0,0,0,0], base_stats=[100,100,100,100,100,100], nature = None, shiny = False, gender = "male", nickname = None):
        self.level = level
        self.name = name
        self.shiny = shiny
        self.gender = gender
        self.nickname = nickname
        self.dex_num = dex_num
        self._ivs = ivs
        self._base_stats:list[int] = base_stats
        self.nature = nature if nature else random.choice(list(NATURES.keys()))
        self.stats = self.calculate_stats()

    def calculate_stats(self):
        stats = self._base_stats.copy()
        nature = NATURES[self.nature]
        stats[0] = int(((2 * self._base_stats[0] + self._ivs[0] + 100) * self.level) / 100 + 10)
        for i in range(1, 6):
            stats[i] = int((((2 * self._base_stats[i] + self._ivs[i]) * self.level) / 100 + 5))
        if nature[0] != nature[1]:
            stats[nature[0]] = int(stats[nature[0]] * 1.1)
            stats[nature[1]] = int(stats[nature[1]] * 0.9)
        return stats

    def change_nick(self, nickname=None):
        if not nickname:
            self.nickname = None
            return
        if not isinstance(nickname, str):
            raise TypeError("Input is not a string.")
        self.nickname = nickname
    
    def __str__(self):
        return (f"SimPokemon(dex_num={self.dex_num}, name={self.name}, nickname={self.nickname}, shiny={self.shiny}, " +
                f"stats={self.stats}, ivs={self._ivs}, nature={self.nature})")
