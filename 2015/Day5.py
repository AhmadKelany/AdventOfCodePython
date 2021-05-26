
import re

with open('2015\day2input.txt') as f:
    lines = f.readlines()

def HasAtLeast3Vowels(s):
    return sum(1 for c in s if 'aeiou'.__contains__(c)) >= 3

def HasAtLeast1Duplicate(s):
    return re.match('(\w)\1+' , s)

print(HasAtLeast1Duplicate('jhiioufree'))
print(HasAtLeast1Duplicate('jhioufre'))