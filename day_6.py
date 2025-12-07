from collections import defaultdict

f = open('day_6.txt', 'r')
lines = f.read().strip().split('\n')
numbers: list[list[str]] = []
operations: dict[int, dict] = defaultdict(lambda: {'numbers': [], 'operator': None})

def part1(ris: int = 0) -> int:
    for line in lines:
        i = line.strip().split()
        numbers.append(i)

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if i == len(numbers) - 1:
                operations[j]['operator'] = numbers[i][j]
            else:
                operations[j]['numbers'].append(int(numbers[i][j]))

    for _, problem in operations.items():
        num = problem['numbers']
        op = problem['operator']

        if op == '+':
            result = 0
            for n in num:
                result += n

        elif op == '*':
            result = 1
            for n in num:
                result *= n
        
        ris+=result
    
    return ris

def part2():
    indexes = []
    operators = []
    ris = 0

    for i in range(len(lines[-1])):
        if lines[-1][i] != ' ':
            operators.append(lines[-1][i])
            indexes.append(i)

    indexes.append(len(lines[0]))

    
    for block in range(len(operators)):
        start = indexes[block]
        end = indexes[block + 1]
        op = operators[block]

        num = []

        for col in range(start, end):
            n_str = ""

            for row in range(len(lines[:-1])):
                n_str += lines[row][col]

            n_str = n_str.strip()

            if n_str:
                num.append(int(n_str))

        
        if op == '+':
            result = 0
            result = sum(num)
        elif op == '*':
            result = 1
            for n in num:
                result *= n
        ris += result

    return ris


# print(part1())
# print(part2())