character = {"name": "Babarian", "health": 60,
             "powre": 30, "mana": 10, "armor": 15}
# print(character["name"])
# print(character.items())
# print(character.keys())
# print(character.values())

for i in character:
    print(i)

for i in character.values():
    print(i)

for i in character, character.values():
    print(i)
