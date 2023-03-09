filename = '2022/input.txt'

puzzle_input = [r.strip() for r in open(filename).readlines()]
shape_score = {'X': 1, 'Y': 2, 'Z': 3}

def part1(puzzle_input):
    opponent_score = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 'B': {'X': 0, 'Y': 3, 'Z': 6}, 'C': {'X': 6, 'Y': 0, 'Z': 3}}
    total_score = 0
    for input in puzzle_input:
        opponent, you = input.split()
        total_score += shape_score[you] + opponent_score[opponent][you]
    return total_score

def part2(puzzle_input):
    total_score = 0
    opposite_shape_score = {'A': {'X': 3 , 'Y': 1 , 'Z': 2 }, 'B': {'X': 1 , 'Y': 2 , 'Z': 3 }, 'C': {'X': 2, 'Y': 3, 'Z': 1}}
    your_score = {'X': 0, 'Y': 3, 'Z': 6}
    for input in puzzle_input:
        opponent, you = input.split()
        total_score += opposite_shape_score[opponent][you] + your_score[you]
    return total_score

#Part 1
print(part1(puzzle_input))

#Part 2
print(part2(puzzle_input))
        