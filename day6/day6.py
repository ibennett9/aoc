def read_input(file_path:str)->str:
    with open(file_path, 'r') as file:
         return file.read().splitlines()[0]

def find_packet_start(stream: str) -> int:
    index = 3
    currentCounter = 0
    streamLength = len(stream)
    while index < streamLength and currentCounter < 4:
        new_var = stream[index]
        new_var1 = stream[index-3]
        if new_var == new_var1:
            index += 3
            currentCounter = 0
        else:
            index += 1
            currentCounter += 1
        print (index)
    return -1

def brute(stream:str, markerLength:int)->int:
    index = 0
    currentToken = []
    streamLength = len(stream)
    while index < streamLength:
        new_var = stream[index]
        if new_var not in currentToken:
            currentToken.append(stream[index])
        else:
            currentToken = [stream[index]]
        if len(currentToken) == markerLength:
            break
        index += 1
    return index + 1

def main():
    input = read_input("day6/input6.txt")
    print(brute(input, 4))
    print(brute(input, 14))

main()