import json
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def __repr__(self):
        odict = {
            "name": self.name,
            "score": self.score
        }
        return json.dumps(odict)

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.name < b.name:
            return -1
        elif a.name > b.name:
            return 1
        return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

############################################################################
"""
SAMPLE1:
        INPUT:
                5
                amy 100
                david 100
                heraldo 50
                aakansha 75
                aleksa 150
        OUTPUT:
                aleksa 150
                amy 100
                david 100
                aakansha 75
                heraldo 50
SAMPLE2:
        INPUT:
                3
                smith 20
                jones 15
                jones 20
        OUTPUT:
                jones 20
                smith 20
                jones 15
SAMPLE3:
        INPUT:
                4
                davis 15
                davis 20
                davis 10
                edgehill 15
        OUTPUT:
                davis 20
                davis 15
                edgehill 15
                davis 10
"""
