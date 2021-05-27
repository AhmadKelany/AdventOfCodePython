from typing import NamedTuple


with open('2015\day5input.txt') as f:
    lines = f.readlines()

Instruction = NamedTuple('Instruction' , 'Command x1 y1 x2 y2')
def Part1Rule(command,num):
    match command:
        case 'on':
            num = 1
        case 'off':
            num = 0
        case 'toggle':
            num = 0 if num == 1 else 1
    return num

def Part2Rule(command,num):
    match command:
        case 'on':
            num += 1
        case 'off':
            num = 0 if num == 0 else num - 1
        case 'toggle':
            num += 2
    return num   

def GetInstruction(s):
    return Instruction('on' , 0 , 1 , 0 , 1)

a = GetInstruction('')
print(a.command)
print(a.x1)