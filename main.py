from input import out, inp
from collections import defaultdict
from random import randint, shuffle
# print(inp("01-the-cloud-abyss.txt"))
path = [
    "inputs/00-example.txt",
    "inputs/01-the-cloud-abyss.txt",
    
    "inputs/02-iot-island-of-terror.txt",
    "inputs/03-etheryum.txt",
    "inputs/04-the-desert-of-autonomous-machines.txt",
    "inputs/05-androids-armageddon.txt"

]
def solve(path):
    stamina, max_stamina, turns, demons = inp(path)

    seen = set()
    killed = []
    gain_stamina = defaultdict(int)
    for turn in range(turns):
        stamina += gain_stamina[turn]
        p = [i for i in range(0, len(demons) - 1)]
        for i in p:
            demon = demons[i]
            if i not in seen and stamina >= demon.consume_stamina:
                gain_stamina[turn + demon.recover_turns] += demon.recover_stamina
                stamina -= demon.consume_stamina
                killed.append(i)
                seen.add(i)
            if stamina >= max_stamina:
                break
    
    return killed[::-1]
    
    
for _ in range(len(path)):
    
    faced_demon_id= solve(path[_])
    out(_,faced_demon_id)