import re

def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()

def find_split_line(input:list[str]) -> int:
    for row in input:
        if row == "": return input.index(row)

def parse_instructions(raw:list[str]) -> list[list[str]]:
    instructions = []
    for row in raw:
        values = re.split("move|from|to", row)
        instructions.append([int(values[1]), int(values[2]), int(values[3])])
    return instructions

def plan_to_columns(plan:list[str]) -> list[list[str]]:
    columns = []
    for num in re.split("    | ", plan[0]):
        columns.append([])
    for row in reversed(plan):
        rowSplit = re.split("    | ", row)
        index = 0
        while index < len(rowSplit):
            if rowSplit[index] != "":
                columns[index].append(rowSplit[index])
            index += 1
    return columns

def execute_instructions(plan:list[list[str]], instructions:list[list[int]])->list[list[str]]:
    for instruction in instructions:
        for numberOfItems in range(instruction[0]):
            item = plan[instruction[1]-1].pop()
            plan[instruction[2]-1].append(item)
    return plan

def execute_instructions_2(plan:list[list[str]], instructions:list[list[int]])->list[list[str]]:
    for instruction in instructions:
        items = plan[instruction[1]-1][len(plan[instruction[1]-1]) - instruction[0]: len(plan[instruction[1]-1])]
        plan[instruction[1]-1] = plan[instruction[1]-1][0:len(plan[instruction[1]-1]) - instruction[0]]
        for item in items:
            plan[instruction[2]-1].append(item)
    return plan

def display_solution(plan:list[list[str]])->None:
    for column in plan:
        try:
            print(column[-1][1], end="")
        except:
            pass
    print()

def main():
    input = read_input_into_list("day5/input5.txt")
    splitRow = find_split_line(input)
    plan = plan_to_columns(input[0:splitRow-1])
    instructions = parse_instructions(input[splitRow+1:len(input)])
    # firstFinal = execute_instructions(firstPlan, instructions)
    secondFinal = execute_instructions_2(plan, instructions)
    # display_solution(firstFinal)
    display_solution(secondFinal)

main()