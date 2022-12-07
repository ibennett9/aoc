def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()

def halve_lines(input:list[str]) -> list[list[str]]:
    splits = []
    for line in input:
        length = len(line)
        splits.append([line[0:length // 2],line[length // 2: length]])
    return splits

def group_lines(input:list[str]) ->list[list[str]]:
    groups = []
    group =[]
    for pack in input:
        if len(group) == 3:
            groups.append(group)
            group = []
        group.append(pack)
    groups.append(group)
    return groups

def find_common(groups:list[list[str]]) -> chr:
    commonItems = []
    for item in groups[0]:
        if item in groups[1]:
            commonItems.append(item)
    if len(groups) != 3:
        return commonItems[0]
    for item in commonItems:
        if item in groups[2]:
            return item

def rel_value_of_item(item:chr) -> int:
    asciiVal = ord(item)
    if asciiVal < 91:
        return asciiVal - 38
    else: 
        return asciiVal - 96

def main():
    input = read_input_into_list('input3.txt')
    # halves = halve_lines(input)
    groups = group_lines(input)
    items = []
    # for rucksack in halves:
    #     items.append(find_common(thing))
    for group in groups:
        items.append(find_common(group))
    totalValue = 0
    print(len(items))
    for item in items:
        totalValue += rel_value_of_item(item)
    print(totalValue)

main()