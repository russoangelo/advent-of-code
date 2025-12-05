f = open('day_4.txt', 'r')

lines = f.read().strip()
array = [list(row) for row in lines.splitlines()]
directions = [
    (-1, -1),
    (-1, 0),
    (0, 1),
    (1, -1),
    (0, -1),
    (1, 0),
    (-1, 1),
    (1, 1)
]

def part1() -> int:
    ris = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            adjacency = 0
            if array[i][j] == '@':
                for dx, dy in directions:
                    if  0 <= i+dx < len(array) and 0 <= j+dy < len(array[i]) and array[i+dx][j+dy] == '@':
                        adjacency += 1
                
                if adjacency < 4:
                    ris += 1
    
    return ris

def part2() -> int:
    ris = 0
    while True:
        count = 0
        to_remove: list[tuple[int, int]] = []
        for i in range(len(array)):
            for j in range(len(array[i])):
                adjacency = 0
                if array[i][j] == '@':
                    for dx, dy in directions:
                        if  0 <= i+dx < len(array) and 0 <= j+dy < len(array[i]) and array[i+dx][j+dy] == '@':
                            adjacency += 1
                    
                    if adjacency < 4:
                        to_remove.append((i, j))
                        count += 1
                        ris += 1

        for i, j in to_remove:
            array[i][j] = '.'

        if count == 0:
            break
    
    return ris

# print(part1())
# print(part2())