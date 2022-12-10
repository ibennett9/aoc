def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()

def calculate_perimeter_trees(rows:list[str])->int:
    perimeterTrees = len(rows) * 2
    perimeterTrees += (len(rows[0]) - 2) * 2
    return perimeterTrees 

# def calculate_row_trees(rows:list[str], lToR:bool)->int:
#     visibleTrees = 0
#     for row in rows:
#         if !lToR:
#             row = row.reverse()
#         currentHighest = row.pop(0)
#         for tree in row:
#             if tree > currentHighest:
#                 visibleTrees += 1
#                 currentHighest = tree
#     return visibleTrees 

def calculate_row_trees(rows:list[str], lToR:bool)->int:
    visibleTrees = 0
    for row in rows:
        if !lToR:
            row = row.reverse()
        currentHighest = '.'
        for tree in row:
            if tree > currentHighest:
                visibleTrees += 1
                currentHighest = tree
    return visibleTrees 

def calculate_column_trees(grid:list[str], tToB:bool)->int:
    visibleTrees=0
    if tToB:
        checkGrid=grid #might need shallow copy
    else:
        checkGrid=grid.reverse()
    currentColumn = 0
    while currentColumn < len(checkGrid[0]):
        currentHighest = '.'
        for row in checkGrid:
            if row[currentColumn] > currentHighest:
                visibleTrees+=1
                currentHighest=row[column]
        currentColumn+=1
     return visibleTrees 

def main():
    input = read_input_into_list("day8/input8.txt")
    numberOfTreesOutside = calculate_perimeter_trees(input)
    numberOfTreesLR = calculate_row_trees(rows=input, lToR=True)
    numberOfTreesRL = calculate_row_trees(rows=input, lToR=False)
    numberOfTreesTB = calculate_column_trees(grid=input, tToB=True)

main()
