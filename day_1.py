f = open('day_1.txt', 'r')
code = 50
count = 0

ind = 1

def part1(code: int, count: int) -> int:
    for line in f:
        direction = line[0]
        new_line = int(line.replace(direction, '').strip())
        for _ in range(new_line):
            if direction == 'L':
                code-=ind
                if code < 0:
                    code = 99
            elif direction == 'R':
                code+=ind
                if code > 99:
                    code = 0
        if code == 0:
            count += 1

    return count

def part2(code: int, count: int) -> int:
    for line in f:
        direction = line[0]
        new_line = int(line.replace(direction, '').strip())
        for _ in range(new_line):
            if direction == 'L':
                code -= ind
                if code < 0:
                    code = 99
                if code == 0:
                    count += 1
            elif direction == 'R':
                code+=ind
                if code > 99:
                    code = 0
                if code == 0:
                    count += 1

    return count
                
# print(part1(code, count))
# print(part2(code, count))