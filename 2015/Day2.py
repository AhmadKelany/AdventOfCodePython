with open('2015\day2input.txt') as f:
    lines = f.readlines()

def getBox(line):
    return list(map(int , line.split('x')))

def getArea(box):
    return 2 * box[0] * box[1] + 2 * box[1] * box[2] + 2 * box[2] * box[0]

def getSlack(box):
    return min(box[0]*box[1] , box[0] * box[2] , box[1] * box[2])

def getRibbonArea(box):
    box.sort()
    return 2 * box[0] + 2 * box[1] + box[0] * box[1] * box[2]

def Part1():
    sum = 0
    for line in lines:
        box = getBox(line)
        sum += getArea(box) + getSlack(box)
    return sum

def Part2():
    sum = 0
    for line in lines:
        box = getBox(line)
        sum += getRibbonArea(box) 
    return sum

print('Part 1 :' , Part1())
print('Part 2 :' , Part2())