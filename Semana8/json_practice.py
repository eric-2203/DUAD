import json

print("Enter new Pokemon information")
pokemons_information = [
  {
    "name": {
      "english": "Pikachu"
    },
    "type": [
      "Electric"
    ],
    "base": {
      "HP": 35,
      "Attack": 55,
      "Defense": 40,
      "Sp. Attack": 50,
      "Sp. Defense": 50,
      "Speed": 90
    }
  },
  {
    "name": {
      "english": "Charmander"
    },
    "type": [
      "Fire"
    ],
    "base": {
      "HP": 39,
      "Attack": 52,
      "Defense": 43,
      "Sp. Attack": 60,
      "Sp. Defense": 50,
      "Speed": 65
    }
  },
  {
    "name": {
      "english": "Squirtle"
    },
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
  },
    {
    "name": {
      "english": input("Pokemon name: ")
    },
    "type": [
      input("Type: ")
    ],
    "base": {
      "HP": input("HP: "),
      "Attack": input("Attack: "),
      "Defense": input("Defense: "),
      "Sp. Attack": input("Sp. Attack: "),
      "Sp. Defense": input("Sp. Defense: "),
      "Speed": input("Speed: "),
    }
  }
]

print("Thank you for the information")
with open('file_path.json' , 'w') as file:
    json_file = json.dump(pokemons_information, file, indent=4)


