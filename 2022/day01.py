filename = '2022/input.txt'
puzzle_input = [r.strip() for r in open(filename).readlines()]

def top_three(input):
    a,b,c = 0,0,0
    curr_cals = 0

    for entry in input:
        if entry == '':
            if curr_cals > a:
                a,b,c = curr_cals,a,b
            elif curr_cals > b:
                b,c = curr_cals,b
            elif curr_cals > c:
                c = curr_cals
            curr_cals = 0
        else:
            curr_cals += int(entry)
    return a,b,c

#Part 1
print(max(top_three(puzzle_input)))

# Part 2
print(sum(top_three(puzzle_input)))