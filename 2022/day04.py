def part1(puzzle_input):
    contained = 0
    for pair in puzzle_input:
        (a,b), (c,d) = [map(int, r.split("-")) for r in pair.split(",")]

        if (a <= c and d <= b) or (c <= a and b <= d):
            contained += 1
    return contained

def part2(puzzle_input):
    overlap = 0
    for pair in puzzle_input:
        (a,b), (c,d) = [map(int, r.split("-")) for r in pair.split(",")]
        if b >= c and a <= d:
            overlap += 1
    return overlap

        
def main():
    filename = "2022/input.txt"
    with open(filename) as f:
        puzzle_input = [line.strip() for line in f]

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()