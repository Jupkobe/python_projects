import random as r

file = open("kadro.txt", "r")

roster = {}

stats = {"gurdal": 6.5,
         "fmu": 7,
         "tekinel": 8,
         "yunus": 7,
         "koyun": 4.5,
         "yigit": 5.5,
         "eck": 4,
         "hako": 3.5,
         "gazi": 4,
         "apo": 8,
         "kerem": 7,
         "emirk": 8,
         "eyup": 4,
         "mert": 4,
         "cengiz": 3,
         "muti": 5.5,
         "adin": 7}
#ensar = 2
#mete = 5

for i in file:
    i = i.strip().lower()
    roster[i] = stats[i]

roster = dict(sorted(roster.items(), key=lambda x: x[1], reverse=True))
players = list(roster.keys())

# team_size = input("Takım boyutu: ")

def takimlar():
    r.shuffle(players)
    team_a = []
    team_b = []
    stat_a = 0
    stat_b = 0
    for pl in players:
        if pl in team_a or pl in team_b:
            continue
        if len(team_b) == len(team_a) and stat_a == stat_b:
            team_a.append(pl)
            stat_a += stats[pl]
        elif stat_a > stat_b and len(team_b) == len(team_a):
            team_b.append(pl)
            stat_b += stats[pl]
        elif stat_a < stat_b and len(team_b) == len(team_a):
            team_a.append(pl)
            stat_a += stats[pl]
        elif len(team_b) < len(team_a):
            team_b.append(pl)
            stat_b += stats[pl]
        elif len(team_b) > len(team_a):
            team_a.append(pl)
            stat_a += stats[pl]
    return team_a, stat_a, team_b, stat_b


for i in range(5):
    print(takimlar())
