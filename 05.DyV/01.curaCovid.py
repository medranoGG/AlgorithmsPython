g = []
bestItem = -1
shortest = float('inf')

chains = int(input())
for _ in range(chains):
    g.append([])
for c in range(chains):
    cad = input()
    for i in range(len(cad)):
        g[c].append(cad[i])

    if len(cad) < shortest:
        shortest = len(cad)
        bestItem = c

letter = 0
isSol = False
sol = list()
while letter < len(g[bestItem]) and not isSol:
    for i in range(chains):
        if g[i][letter] != g[bestItem][letter]:
            isSol = True
    if not isSol:
        sol.append(g[bestItem][letter])

    letter += 1

for s in sol:
    print(s, end="")