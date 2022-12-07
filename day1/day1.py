def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()

def group_calories(allLines:list[str]) -> list[int]:
    groups = []
    currentTotal = 0
    for string in allLines:
        if string != "":
            currentTotal+= int(string)
        else:
            groups.append(currentTotal)
            currentTotal = 0
    return groups

def main():
    inputLines = read_input_into_list('input1.txt')
    caloriesPerElf = group_calories(inputLines)
    # print(max(caloriesPerElf))
    caloriesPerElf.sort(reverse=True)
    print(caloriesPerElf[0] + caloriesPerElf[1] + caloriesPerElf[2])

main()
