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

def part2(sum: int) -> int:
    for prod in ranges:
        prod_id = prod.split('-')
        start, end = int(prod_id[0]), int(prod_id[1])

        for i in range(start, end + 1):
            string = ""
            ris = 0
            prod_id_str = str(i)
            for k in range(1, len(prod_id_str)):
                string = prod_id_str[:k]
                if len(prod_id_str) % len(string) != 0:
                    continue
                ris = len(prod_id_str) // len(string)
                if ris >= 2:
                    verify = string * ris
                    if prod_id_str == verify:
                        sum+=int(verify)
                        break
    return sum

# print(part2(sum=0))
# print(part1(sum = 0))