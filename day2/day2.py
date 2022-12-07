def read_input_into_list(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
         return file.read().splitlines()

def split_lines(input:list[str]) -> list[list[int]]:
    splitLines = []
    for line in input:
        splitLine = line.split(" ")
        opp = 0
        match splitLine[0]:
            case "A":
                opp = 1
            case "B":
                opp = 2
            case "C":
                opp = 3
        score = 0
        match splitLine[1]:
            case "X":
                score = 1
            case "Y":
                score = 2
            case "Z":
                score = 3
        splitLines.append([opp, score])
    return splitLines

def calc_score_of_round(strat:list[int]) -> int:
    opp = strat[0]
    score = strat[1]
    if score == opp:
        return score + 3
    elif (score == 3 and opp == 1) or opp == score + 1:
        return score
    else:
         return score + 6

def calc_round_2(strat:list[int]) -> int:
    opp = strat[0]
    result = strat[1]
    match result:
        case 1:
            return 3 if opp == 1 else opp - 1
        case 2:
            return opp + 3
        case 3:
            return 7 if opp == 3 else opp + 1 + 6

def main():
    input = read_input_into_list('input2.txt')
    rounds = split_lines(input)
    firstStratTotal = 0
    secondStratTotal = 0
    for round in rounds:
        firstStratTotal += calc_score_of_round(round)
        secondStratTotal += calc_round_2(round)
    print(firstStratTotal)
    print(secondStratTotal)

main()