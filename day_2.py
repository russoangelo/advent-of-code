f = open('day_2.txt', 'r')
ranges = f.read().strip().split(',')

def part1(sum: int) -> int:
    for prod in ranges:
        prod_id = prod.split('-')
        start, end = int(prod_id[0]), int(prod_id[1])


        for i in range(start, end + 1):
            prod_id_str = str(i)
            if len(prod_id_str) % 2 != 0:
                continue
            else:
                id_len = len(prod_id_str) // 2
                if prod_id_str[:id_len] == prod_id_str[id_len:]:
                    sum+=i
    return sum


'''
if i have 111111
i can check every
for example if i have 12341234

i have a flag to check
i take the 1, then 2 == 1 no, so 12 is equal to 34 no 123 is equal to 412 no, 1234 is equal 1234 yes, but the str is ended? if yes is invalid else continue

i
'''

# print(part1(sum = 0))