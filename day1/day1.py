
def part1():
    file = open("input")
    list1 = []
    list2 = []
    
    for line in file.readlines():
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))
    list1.sort()
    list2.sort()

    print(sum([abs(x1 - x2) for x1, x2 in zip(list1, list2)]))

if __name__ == "__main__":
    file = open("input")
    list1 = []
    dict_column2 = {}
    
    for line in file.readlines():
        num1, num2 = line.split()
        list1.append(int(num1))
        dict_column2[int(num2)] = dict_column2.get(int(num2), 0) + 1

    answer = 0
    for num in list1:
        answer += num * dict_column2.get(num, 0)
    
    print(answer)