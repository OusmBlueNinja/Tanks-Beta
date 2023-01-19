import json
import os
path = os.path.dirname(os.path.realpath(__file__))


def load():
    print("loading GameData")
    saveDir = f"{path}/data/save.json"
    f = open(f'{saveDir}')
    data = json.load(f)
    x = data['saveData']['playerX']
    y = data['saveData']['playerY']
    seed = data['saveData']['seed']
    f.close()
    print("Loaded GameData")
    return x, y, seed
    pass


def save(x, y):
    print("saveing GameData")
    saveDir = f"{path}/data/save.json"
    f = open(f'{saveDir}')
    data = json.load(f)
    data['saveData']['playerX'] = x
    data['saveData']['playerY'] = y
    f.close()
    with open(saveDir, 'w') as f:
        data2 = json.dumps(data)
        f.write(str(data2))
    print("saved GameData")
