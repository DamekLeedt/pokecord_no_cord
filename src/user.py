import os, simpokemon, pypokedex, random

class User:
    def __init__(self):
        self.party = []
        self.money = 0

    def load(self, file):
        pass

    def save(self):
        if not self.party:
            print("No party.")
            return "No party."
        if not os.path.exists("./saves"):
            print("saves does not exist")
            os.makedirs("./saves")
        

    def add_pokemon(self, dex_num = 151, shiny = False, gender = "male"):
        pokemon = pypokedex.get(dex = dex_num)
        self.party.append(simpokemon.SimPokemon(dex_num, pokemon.name, random.randint(1, 100), self._generate_ivs(), list(pokemon.base_stats), None, shiny, gender))

    def show_party(self):
        if not self.party:
            print("Empty party.")
            return
        for pokemon in self.party:
            print(pokemon)

    def _generate_ivs(self):
        return [random.randint(0, 31) for _i in range(6)]