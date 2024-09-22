import os, simpokemon, pypokedex, random

class User:
    def __init__(self):
        self.party = []
        self.money = 0

    def load(self):
        if not os.path.exists("../saves/save.txt"):
            print("No save file available.")
            print(os.path)
            return
        save = open("../saves/save.txt", "r").read().split("\n")
        print("Money available: " + save[0])
        for pokemon in save[1:]:
            if not pokemon:
                break
            print(pokemon)
            traits = pokemon.split("|")
            self.party.append(simpokemon.SimPokemon(traits[0], traits[1], int(traits[4]), self.list_of_str_to_int(traits[6].split(",")), self.list_of_str_to_int(traits[5].split(",")), traits[7], bool(traits[3]), traits[8], traits[2]))

    def list_of_str_to_int(self, list):
        return [int(num) for num in list]

    def save(self):
        if not self.party:
            print("No party.")
            return "No party."
        if not os.path.exists("../saves"):
            print("saves does not exist")
            os.makedirs("../saves")
        save = open("../saves/save.txt", "w")
        save.write(str(self.money) + "\n")
        for pokemon in self.party:
            save.write(str(pokemon) + "\n")
        save.close()
        
    def clear_party(self, are_you_sure = True):
        if not self.party:
            print("No party to clear.")
            return "No party to clear."
        if not are_you_sure:
            print("Canceling.")
            return "Canceled."
        self.party = []

    def add_pokemon(self, dex_num = 151, shiny = False, gender = "male"):
        pokemon = pypokedex.get(dex = dex_num)
        self.party.append(simpokemon.SimPokemon(dex_num, pokemon.name, random.randint(1, 100), self._generate_ivs(), list(pokemon.base_stats), None, shiny, gender))

    def show_party(self):
        if not self.party:
            print("Empty party.")
            return
        for pokemon in self.party:
            print(repr(pokemon))

    def _generate_ivs(self):
        return [random.randint(0, 31) for _i in range(6)]