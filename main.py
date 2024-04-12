import pypokedex, random, pokemon

import pypokedex.pokemon

def main():
    result = generate_ivs()
    print(result)
    print(get_pokemon().base_stats)

def get_pokemon(dex_num:int = 1):
    return pypokedex.get(dex=dex_num)

def generate_ivs():
    return [random.randint(0, 31) for _i in range(6)]

def generate_pokemon(dex_num:int = 1):
    pokemon:pypokedex.pokemon = pypokedex.get(dex=dex_num)

main()