filename = "2022/input.txt"
puzzle_input = [r.strip() for r in open(filename).readlines()]


def part1(puzzle_input):
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    opponent_score = {
        'A': {'X': 3, 'Y': 6, 'Z': 0}, 
        'B': {'X': 0, 'Y': 3, 'Z': 6}, 
        'C': {'X': 6, 'Y': 0, 'Z': 3}
    }
    return sum(shape_score[you] + opponent_score[opponent][you] for opponent, you in map(str.split, puzzle_input))

def part2(puzzle_input):
    opposite_shape_score = {
        'A': {'X': 3, 'Y': 1, 'Z': 2},
        'B': {'X': 1, 'Y': 2, 'Z': 3},
        'C': {'X': 2, 'Y': 3, 'Z': 1}
    }
    your_score = {'X': 0, 'Y': 3, 'Z': 6}
    return sum(opposite_shape_score[opponent][you] + your_score[you] for opponent, you in map(str.split, puzzle_input))

def main():
    filename = "2022/input.txt"
    with open(filename) as f:
        puzzle_input = [line.strip() for line in f]

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()