with open("2021/input/day-2-example.txt", "r") as example_file:
    example_input = example_file.read().splitlines()

with open("2021/input/day-2-puzzle.txt", "r") as puzzle_file:
    puzzle_input = puzzle_file.read().splitlines()

def dive(input):
    pos = 0
    depth = 0
    for x in input:
        command, unit = x.split(" ")
        if command == "forward":
            pos += int(unit)
        elif command == "down":
            depth += int(unit)
        elif command == "up":
            depth -= int(unit)
    return pos * depth

def dive2(input):
    aim = 0
    pos = 0
    depth = 0
    for x in input:
        command, unit = x.split(" ")
        if command == "forward":
            pos += int(unit)
            depth += aim * int(unit)
        elif command == "down":
            aim += int(unit)
        elif command == "up":
            aim -= int(unit)
    return depth * pos


print(dive(example_input))
print(dive(puzzle_input))

print(dive2(example_input))
print(dive2(puzzle_input))