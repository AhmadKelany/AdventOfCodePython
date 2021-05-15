with open('2015\day3input.txt') as f:
    input = f.read()

def GetSeenCount(directions, moversCount):
    currentLocations = {}
    seen = set()
    for m in range(0,moversCount):
        currentLocations[m] = '0,0'

    seen.add('0,0')
    moverIndex = 0
    for c in directions:
        newlocation = list(map(int , currentLocations[moverIndex].split(','))) 
        match c:
            case '^':
                newlocation[1] -= 1
            case 'v':
                newlocation[1] += 1
            case '>':
                newlocation[0] += 1
            case '<':
                newlocation[0] -= 1
        newlocationString = f'{newlocation[0]},{newlocation[1]}'
        seen.add(newlocationString)
        currentLocations[moverIndex] = newlocationString
        moverIndex = 0 if moverIndex == moversCount -1 else moverIndex + 1
    return len(seen)

def part1():
    return GetSeenCount(input,1)

def part2():
    return GetSeenCount(input , 2)

print(f'part 1 result = {part1()}')
print(f'part 2 result = {part2()}')