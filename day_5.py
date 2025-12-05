f = open('day_5.txt', 'r')

lines = f.read().splitlines()

ranges: list[list[int]] = []
available_id: list[int] = []

merge: list[list[int]] = []

def part1(blank_line_index: int = 0, count: int = 0) -> int:
    for i in range(len(lines)):
        if lines[i] == '':
            blank_line_index = i
            break

    for i in range(0, blank_line_index):
        start, end = map(int, lines[i].split('-'))
        ranges.append([start, end])

    for i in range(blank_line_index+1, len(lines)):
        available_id.append(int(lines[i]))

    for i in available_id:
        is_fresh = any(start <= i <= end for start, end in ranges)

        if is_fresh:
            count+=1

    return count


def part2(blank_line_index: int = 0, count: int = 0):
    for i in range(len(lines)):
        if lines[i] == '':
            blank_line_index = i
            break

    for i in range(0, blank_line_index):
        start, end = map(int, lines[i].split('-'))
        ranges.append([start, end])
    
    ranges.sort()

    for start, end in ranges:
        if not merge:
            merge.append([start, end])
        elif start <= merge[-1][1]:
            merge[-1][1] = max(merge[-1][1], end)
        else:
            merge.append([start, end])

    

    return sum(end - start + 1 for start, end in merge)

# print(part1())
# print(part2())