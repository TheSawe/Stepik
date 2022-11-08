players = {'Carlsen': 2842,
           'Caruana': 2822,
           'Mamedyarov': 2801,
           'Ding': 2797,
           'Giri': 2780}
top_players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801, Ding=2797, Giri=2780)
print(top_players)
print(players)

top1 = players['Carlsen']
top_1 = players.get('Carlsen')
print(f'Top chess player\'s rating is {top1}')
print(top_1)

players['So'] = 2780
print(players)
players['So'] = 2781
print(players)

del players['So']
print(players)

keys = players.keys()
print(type(keys))
print(keys)

l = list(players.keys())
print(type(l))
print(l)

print(sorted(players.keys()))

print('Carlsen' in players)
print('Kramnik' not in players)

vals = players.values()
print(type(vals))
print(vals)
vals = list(vals)
print(type(vals))
print(vals)
