
from collections import namedtuple
with open('2015\day6input.txt') as f:
    lines = f.readlines()


Instruction = namedtuple('Instruction' , 'command x1 y1 x2 y2')

def Part1Rule(command,num):
    match command:
        case 'on':
            num = 1
        case 'off':
            num = 0
        case 'toggle':
            num = 1 - num
    return num

def Part2Rule(command,num):
    match command:
        case 'on':
            num = num + 1
        case 'off':
            num = 0 if num == 0 else num - 1
        case 'toggle':
            num = num + 2
    return num   

def GetInstruction(s):
    d = s.split(' ')
    index = 2 if s.startswith('turn') else 1
    p1 = list(map(int , d[index].split(',')))
    p2 = list(map(int , d[index+2].split(',')))
    c = d[index-1]
    return Instruction(c , p1[0] , p1[1] , p2[0] , p2[1])

def GetAllInstructions():
    instructions = []
    for l in lines:
        instructions.append(GetInstruction(l))
    return instructions

def ApplyInstructions(instructions,rule):
    
    matrix =  [[0 for x in range(1000)] for i in range(1000)]
    
    for i in instructions:
        for x in range(i.x1,i.x2+1):
            for y in range(i.y1,i.y2+1):
                matrix[x][y] = rule(i.command, matrix[x][y])
    return matrix

def GetSum(matrix):
    sum = 0
    for x in range(0,1000):
        for y in range(0,1000):
            sum += matrix[x][y] 
    return sum
    
def Part1():
    return GetSum(ApplyInstructions(GetAllInstructions() , Part1Rule))

def Part2():
    return GetSum(ApplyInstructions(GetAllInstructions() , Part2Rule))



print(f'Part 1 = {Part1()}')
print(f'Part 2 = {Part2()}')

