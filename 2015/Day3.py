with open('2015\day2input.txt') as f:
    input = f.read()

def GetSeenCount(directions, moversCount):
    currentLocations = {}
    seen = set()
    for m in range(0,moversCount):
        currentLocations[m] = '0,0'

    seen.add((0,0))
    moverIndex = 0
    for c in directions:
        newlocation = currentLocations[moverIndex].split(',')
        
