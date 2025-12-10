from collections import deque

f = open('day_7.txt', 'r')

lines = f.read().splitlines()

def part1() -> int:
    row = -1
    col = -1

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == 'S':
                row = r
                col = c
                break

    queue = deque([(row, col)])
    visited = set()
    activated_splitters = set()

    while queue:
        row, col = queue.popleft()

        if f"{row},{col}" in visited:
            continue

        visited.add(f"{row},{col}")

        for r in range(row+1, len(lines)):
            if lines[r][col] == '^':
                if f"{r},{col}" not in activated_splitters:
                    activated_splitters.add(f"{r},{col}")

                if col - 1 >= 0:
                    queue.append((r, col-1))
                
                if col + 1 < len(lines[r]):
                    queue.append((r, col+1))

                break

    return len(activated_splitters)

# print(part1())