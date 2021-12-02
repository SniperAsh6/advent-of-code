with open("2021/input/day-1-example.txt", "r") as example_file:
    example_input = example_file.read().splitlines()

with open("2021/input/day-1-puzzle.txt", "r") as puzzle_file:
    puzzle_input = puzzle_file.read().splitlines()

def sonar_sweep(input):
    count = 0
    last = 999999999
    for x in input:
        x = int(x)
        if x > last:
            count += 1
        last = x
    return count

def group_values(input, group_size=3):
    values = [sum(map(int, input[i:i+group_size])) for i in range(len(input)-(group_size-1))]
    return values

print(sonar_sweep(example_input))
print(sonar_sweep(puzzle_input))

example_values = group_values(example_input)
print(sonar_sweep(example_values))
puzzle_values = group_values(puzzle_input)
print(sonar_sweep(puzzle_values))