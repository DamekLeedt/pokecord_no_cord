import pypokedex, random, user, time

def main():
    loop()

def loop():
    player = user.User()
    game_continue = True
    while game_continue:
        pokemon = get_pokemon(random.randint(1, 151))
        num = random.randint(1, 4096)
        shiny = num == 1
        gender = "male" if num % 2 == 0 else "female"
        chances = 3
        while chances > 0:
            show_pokemon(pokemon, shiny, gender)
            print("What is the name of this Pokemon?")
            choice = input().lower()

            if choice.lower() == "quit":
                game_continue = False
                break
            if choice.lower() == "party":
                player.show_party()
                continue
            if choice.lower() == "save":
                player.save()
                continue
            if choice.lower() == "load":
                player.load()
                continue

            if choice == pokemon.name.lower():
                break
            else:
                chances -= 1
                print(f"Wrong, you have {chances}/3 chances left.")
        if not game_continue:
            continue
        if chances == 0:
            print(f"{pokemon.name.capitalize()} got away...")
        else:
            print("You caught " + pokemon.name.capitalize() + "!")
            player.add_pokemon(pokemon.dex, shiny, gender)
    print("Goodbye!")

def get_pokemon(dex_num:int = 1):
    return pypokedex.get(dex=dex_num)

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