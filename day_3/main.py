
import re

with open("day_3/input.txt", "r") as file:
    data = file.read()


#### Part 1

pattern = r"mul\((\d+),(\d+)\)"
mul_matches = [(int(m.group(1)), int(m.group(2)), m.start()) for m in re.finditer(pattern, data)]

result_part1 = sum([int(match[0]) * int(match[1]) for match in mul_matches])

print(result_part1)


#### Part 2
def is_multiplication_enabled(position, control_matches):
    enabled = True
    relevant_controls = []

    for match in control_matches:
        if match[1] < position:
            relevant_controls.append(match)
    
    if relevant_controls:
        last_control = relevant_controls[-1]
        enabled = (last_control[0] == "do()")
    
    return enabled

control_pattern = r"(?:do|don't)\(\)"
control_matches = [(m.group(), m.start()) for m in re.finditer(control_pattern, data)]

result_part2 = 0
for value_1, value_2, position in mul_matches:
    if is_multiplication_enabled(position, control_matches):
        result_part2 += value_1 * value_2

print(result_part2)

