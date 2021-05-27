
with open('2015\day5input.txt') as f:
    lines = f.readlines()

def HasAtLeast3Vowels(s):
    return sum(1 for c in s if 'aeiou'.__contains__(c)) >= 3

def HasDuplicate(s):
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
def HasDuplicateApart(s):
    for i in range(0,len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def NotContainingNaughtyString(s):
    naughty = ['ab' , 'cd' , 'pq' , 'xy']
    return all(not s.__contains__(n) for n in naughty)

def HasTwoLetterDuplicate(s):
    for i in range(0,len(s) - 3):
        if s[i+2:].__contains__(s[i:i+2]):
            return True
    return False

def RulesCheckCount(list,rules):
    return sum(1 for s in list if all(r(s) for r in rules))

part1rules = [HasDuplicate , NotContainingNaughtyString , HasAtLeast3Vowels]
part2rules = [HasTwoLetterDuplicate , HasDuplicateApart]

print(f'Part 1 count = {RulesCheckCount(lines,part1rules)}')
print(f'Part 2 count = {RulesCheckCount(lines,part2rules)}')
