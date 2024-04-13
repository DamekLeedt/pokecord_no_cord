import pypokedex, random, pokemon, time

def main():
    result = get_pokemon(151)
    print(result)
    show_pokemon(result, True)

def get_pokemon(dex_num:int = 1):
    return pypokedex.get(dex=dex_num)

def generate_ivs():
    return [random.randint(0, 31) for _i in range(6)]

def show_pokemon(pokemon:pypokedex.Pokemon, shiny=False, gender="male"):
    result = pokemon.sprites.front
    if gender != "male" and result["female"]:
        if shiny:
            which_sprite = "shiny_female"
        else:
            which_sprite = "female"
    else:
        if shiny:
            which_sprite = "shiny"
        else:
            which_sprite = "default"
    print(result[which_sprite])


main()