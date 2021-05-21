import hashlib
input = 'iwrupvqb'
def GetRequiredInt(i,zerosCount):
    match = '0' * zerosCount
    x = 0
    while True:
        entry = f'{i}{x}'
        hash = hashlib.md5(entry.encode()).hexdigest()
        if hash.startswith(match):
            return x
        x += 1
    

print(f'Part 1 result = {GetRequiredInt(input,5)}')
print(f'Part 1 result = {GetRequiredInt(input,6)}')
