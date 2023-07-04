#  СЛОВАРЬ СПИСОК МНОЖЕСТВА сначала пустые потом с помоью append
# Добавление элементо
# Вывод элемнтов Values

films = []
new_film = "человек паук: паутина вселенных", "человек земли", "барби"
films.append(new_film)
print(films)
serials = set()
new_serial = "one piece", "мир дружба жвачка", "пацаны"
serials.add(new_serial)
print(serials)
games = {}
gameskeys = {'minecraft': 2010, 'terraria': 2013, "dota 2": 2011}
games.update(gameskeys)
print(games)
print(games.values())