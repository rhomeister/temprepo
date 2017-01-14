import fileinput

numbers = []
for line in fileinput.input():
    numbers.append(int(line.strip()))

print numbers[0] + numbers[1]
