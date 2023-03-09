filename= "2022/input.txt"
puzzle_input = [r.strip() for r in open(filename).readlines()]

def part_1(puzzle_input):
    contained = 0
    for pair in puzzle_input:
        range1, range2 = pair.split(",")
        a,b = range1.split("-")
        c,d = range2.split("-")     

        if int (a) <= int(c) <= int(d) <= int(b):
            contained += 1
        elif int(c) <= int(a) <= int(b) <= int(d):
            contained += 1
    return contained

def part_2(puzzle_input):
    overlap = 0
    for pair in puzzle_input:
        range1, range2 = pair.split(",")
        a,b = range1.split("-")
        c,d = range2.split("-")

        if int(a) <= int(c) <= int(b):
            overlap += 1 
        elif int(c) <= int(a) <= int(d):
            overlap += 1 
    
    return overlap

print(part_2(puzzle_input))
        
