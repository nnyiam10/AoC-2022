filename= '2022/input.txt'
puzzle_input = [r.strip() for r in open(filename).readlines()]

def priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def part1(puzzle_input):
    total_priority = 0
    
    for line in puzzle_input:
        first = line[:len(line)//2]
        second = line[len(line)//2:]

        s = set(first)
        for letter in second:
            if letter in s:
                total_priority += priority(letter)
                break
    return total_priority

def part2(puzzle_input):
    total_priority = 0
    
    for i in range(0, len(puzzle_input), 3):
        first = puzzle_input[i]
        second = puzzle_input[i+1]
        third = puzzle_input[i+2]

        s = set(first)
        s2 = set(second)
        s3 = set(third)

        res = s.intersection(s2, s3)
        total_priority += priority(res.pop())
    return total_priority

print(part2(puzzle_input))