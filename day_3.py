f = open('day_3.txt', 'r')
lines = f.read().splitlines()

# this approach solve both part 1 and part 2

def solve(k: int) -> int:
    ris = 0

    for line in lines:
        bank_joltages = [int(joltage) for joltage in line]
        n = len(bank_joltages)

        k_remaining = k
        start = 0

        enabled = ""

        while k_remaining > 0:
            search = bank_joltages[start:n-k_remaining+1]
            greatest = max(search)

            enabled += str(greatest)
            pos = bank_joltages.index(greatest, start)
            start = pos + 1
            k_remaining -= 1
        
        ris += int(enabled)

    return ris


# print(solve(2))
# print(solve(12))
