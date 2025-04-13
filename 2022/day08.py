from collections import defaultdict
import math

def part1(puzzle_input):
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    visible = set()

    for i in range(rows):
        max_height = -1
        for j in range(cols):
            if puzzle_input[i][j] > max_height:
                visible.add((i, j))
                max_height = puzzle_input[i][j]

    for i in range(rows):
        max_height = -1
        for j in reversed(range(cols)):
            if puzzle_input[i][j] > max_height:
                visible.add((i, j))
                max_height = puzzle_input[i][j]

    for j in range(cols):
        max_height = -1
        for i in range(rows):
            if puzzle_input[i][j] > max_height:
                visible.add((i, j))
                max_height = puzzle_input[i][j]

    for j in range(cols):
        max_height = -1
        for i in reversed(range(rows)):
            if puzzle_input[i][j] > max_height:
                visible.add((i, j))
                max_height = puzzle_input[i][j]

    return len(visible)

def part2(puzzle_input):
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    max_scenic_score = -1
    
    for i in range(rows):
        for j in range(cols):
            height = puzzle_input[i][j]
            scenic_score = 1

            above = [puzzle_input[k][j] for k in range(i)][::-1]
            below = [puzzle_input[k][j] for k in range(i+1, rows)]
            left = [puzzle_input[i][k] for k in range(j)][::-1]
            right = [puzzle_input[i][k] for k in range(j+1, rows)]

            for direction in above, below, left, right:
                curr_visible = 0
                for tree in direction:
                    if tree <= height:
                        curr_visible += 1
                    if tree >= height:
                        break
                scenic_score *= curr_visible
            max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score






            
def main():
    filename = "2022/input.txt"
    with open(filename) as f:
        puzzle_input = [[int(char) for char in line.strip()] for line in f]
    
    print(part1(puzzle_input))
    print(part2(puzzle_input))



if __name__ == "__main__":
    main()
