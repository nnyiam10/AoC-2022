filename= "input.txt"
puzzle_input = [r for r in open(filename).readlines()]

def arrange_creates(puzzle_input):
    row_length = len(puzzle_input[0])
    crates = {}
    for i in range(1, row_length//4 + 1):
        crates[i] = []
    
    for row in puzzle_input:
        if row[1] == "1":
            break
        for i in range(0, row_length, 4):
            if row[i] == "[":
                crates[i//4 + 1].append(row[i+1])
        puzzle_input = puzzle_input[1:]
    puzzle_input = puzzle_input[2:]         #to account for the rows with 1-9 and space
    return (puzzle_input, crates)

def instructions(puzzle_input, crates, part):
    for row in puzzle_input:
        new_row = row.strip().split()
        (num, start, end) = (int(new_row[1]), int(new_row[3]), int(new_row[5]))
        current_crates = crates[start][:num]
        if part == 1:
            current_crates.reverse()
        crates[start] = crates[start][num:]
        crates[end] = current_crates + crates[end]
    res = []
    for key in crates:
        res += crates[key][0]
    return "".join(res)

#Part 1 
def part1(puzzle_input):
    (updated_input, crates) = arrange_creates(puzzle_input)
    return instructions(updated_input, crates, 1)

#Part 2
def part2(puzzle_input):
    (updated_input, crates) = arrange_creates(puzzle_input)
    return instructions(updated_input, crates, 2)
    