import pypokedex, random

def main():
    result = generate_ivs()
    print(result)

def get_pokemon(dex_num:int = 1):
    return pypokedex.get(dex=dex_num)

def generate_ivs():
    return [random.randint(0, 31) for _i in range(6)]

def generate_pokemon(pokemon):
    raise NotImplementedError()

main()