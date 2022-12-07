import re
def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()

def parse_rows(rows: list[str]) -> list[list[int]]:
    parsedRows = []
    for row in rows:
        allTerms = re.split("-|,", row)
        parsedRows.append([int(allTerms[0]), int(allTerms[1]), int(allTerms[2]), int(allTerms[3])])
    return parsedRows

def compute_problem_1(rows:list[list[int]])->int:
    totalCount = 0
    for row in rows:
        if ((row[0]>=row[2] and row[1]<=row[3]) or (row[0]<=row[2] and row[1]>=row[3])):
            totalCount += 1
    return totalCount

def compute_problem_2(rows:list[list[int]])->int:
    totalCount = 0
    for row in rows:
        if row[1] - row [0] > row[3] - row[2]:
            testRange = range(row[0], row[1]+1)
            for number in range(row[2], row[3]+1):
                if number in testRange:
                    totalCount+=1
                    break
        else:
            testRange = range(row[2], row[3]+1)
            for number in range(row[0], row[1]+1):
                if number in testRange:
                    totalCount+=1
                    break
    return totalCount
    

def main():
    input = read_input_into_list('day4/input4.txt')
    parsedRows = parse_rows(input)
    print(compute_problem_2(parsedRows))

main()