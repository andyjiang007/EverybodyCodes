###
# Quest 5
# 11/17/2024
###


def solve1(input):
    result = 0
    inputArray = [line.split(" ") for line in input.split("\n") if line]
    numCol = len(inputArray[0])
    curCol = 0
    inputArray = [
        [int(inputArray[j][i]) for j in range(len(inputArray))]
        for i in range(len(inputArray[0]))
    ]
    # print(inputArray)

    for turn in range(10):
        # pop first item of curren col
        curClapper = inputArray[curCol][0]
        inputArray[curCol].pop(0)
        # do high-fives
        endRow = 0
        endCol = curCol + 1
        if endCol >= numCol:
            endCol = 0
        endColSize = len(inputArray[endCol])
        endHighFive = (curClapper - 1) % (2 * endColSize)
        for highFives in range(endHighFive):
            endRow += 1

        if endRow > endColSize:
            endRow = endColSize - endRow
        inputArray[endCol].insert(endRow, curClapper)

        curCol += 1
        if curCol >= numCol:
            curCol = 0
        result = [line[0] for line in inputArray]
        # print(inputArray)
        # print(result)

    return result


def solve2(input):
    result = 0
    inputArray = [line.split(" ") for line in input.split("\n") if line]
    numCol = len(inputArray[0])
    curCol = 0
    inputArray = [
        [int(inputArray[j][i]) for j in range(len(inputArray))]
        for i in range(len(inputArray[0]))
    ]
    print(inputArray)
    shoutCount = {}

    for turn in range(10000000):
        # pop first item of curren col
        curClapper = inputArray[curCol][0]
        inputArray[curCol].pop(0)
        # do high-fives
        endRow = 0
        endCol = curCol + 1
        if endCol >= numCol:
            endCol = 0
        endColSize = len(inputArray[endCol])
        endHighFive = (curClapper - 1) % (2 * endColSize)
        for highFives in range(endHighFive):
            endRow += 1

        if endRow > endColSize:
            endRow = endColSize - endRow
        inputArray[endCol].insert(endRow, curClapper)

        curCol += 1
        if curCol >= numCol:
            curCol = 0
        # print(inputArray)
        digits = [str(line[0]) for line in inputArray]
        digits = "".join(digits)
        curNum = int(digits)
        if curNum in shoutCount:
            shoutCount[curNum] += 1
            if shoutCount[curNum] == 2024:
                print("Turn: " + str(turn + 1) + " Num: " + str(curNum))
                return (turn + 1) * curNum
        else:
            shoutCount[curNum] = 1

        # print(inputArray)
        # print(shoutCount)

    return result


def solve3(input):
    result = 0
    inputArray = [line.split(" ") for line in input.split("\n") if line]
    numCol = len(inputArray[0])
    curCol = 0
    inputArray = [
        [int(inputArray[j][i]) for j in range(len(inputArray))]
        for i in range(len(inputArray[0]))
    ]
    print(inputArray)

    for turn in range(10000000):
        # pop first item of curren col
        curClapper = inputArray[curCol][0]
        inputArray[curCol].pop(0)
        # do high-fives
        endRow = 0
        endCol = curCol + 1
        if endCol >= numCol:
            endCol = 0
        endColSize = len(inputArray[endCol])
        endHighFive = (curClapper - 1) % (2 * endColSize)
        for highFives in range(endHighFive):
            endRow += 1

        if endRow > endColSize:
            endRow = endColSize - endRow
        inputArray[endCol].insert(endRow, curClapper)

        curCol += 1
        if curCol >= numCol:
            curCol = 0
        # print(inputArray)
        digits = [str(line[0]) for line in inputArray]
        digits = "".join(digits)
        curNum = int(digits)
        result = max(result, curNum)

        # print(inputArray)

    return result


def main():
    inputExample = """
2 3 4 5
3 4 5 2
4 5 2 3
5 2 3 4
"""
    input = """
2 4 3 2
5 3 3 5
2 4 4 5
3 3 2 2
5 5 4 4
"""
    print("Part 1 answer:")
    print(solve1(input))
    inputExample = """
2 3 4 5
6 7 8 9
"""
    input = """
14 94 59 16
26 21 61 44
34 71 50 32
86 25 62 30
60 90 96 60
11 69 91 66
75 83 43 71
36 67 64 18
26 77 42 40
82 12 88 34
33 10 66 52
73 46 22 10
72 90 80 49
47 19 88 26
84 79 41 87
51 45 35 24
75 69 69 61
44 16 52 35
63 71 25 77
67 15 78 39
15 31 33 92
97 79 11 94
47 71 28 18
24 99 70 50
38 84 32 29
36 20 20 53
20 78 59 72
58 74 93 19
54 79 74 92
15 27 38 99
33 78 70 43
68 74 65 25
24 62 90 19
72 37 54 15
91 42 36 81
52 56 98 81
27 19 96 22
87 24 27 38
45 29 79 59
34 83 96 43
40 19 16 81
42 25 76 91
85 36 27 62
95 14 57 43
23 10 48 73
60 28 10 73
15 98 13 70
39 94 45 51
40 63 31 82
34 86 51 41
93 14 30 95
68 66 98 33
48 96 62 85
84 95 17 12
48 30 89 77
55 16 17 95
23 49 41 28
94 22 50 75
38 23 20 89
57 70 11 20
86 37 35 12
11 57 64 76
53 55 76 77
83 34 47 58
56 46 32 97
24 80 74 91
44 27 80 89
83 80 26 37
40 46 46 65
68 97 72 47
98 93 23 54
82 40 93 49
68 85 46 97
88 41 85 18
14 17 23 21
61 42 86 22
37 22 99 81
88 13 66 48
39 14 17 11
87 18 92 57
64 63 58 17
89 30 45 31
60 44 36 13
65 28 21 61
39 13 69 51
59 65 54 31
78 12 64 18
55 25 92 29
35 53 87 84
28 82 75 12
52 29 33 44
99 45 58 30
13 32 42 39
38 16 29 55
41 56 90 73
49 37 67 35
32 67 63 50
76 31 21 53
56 43 26 21
"""
    print("Part 2 answer:")
    print(solve2(inputExample))
    inputExample = """
2 3 4 5
6 7 8 9
"""
    input = """
1006 1008 1004 1009
1002 1002 1003 6830
1007 1004 6399 1004
1004 8266 5014 1001
1006 1008 1006 1002
1000 1004 1008 1000
1008 1003 1009 1006
1006 1002 1006 1009
6281 1005 1005 1006
1006 1005 1007 1004
1000 5562 1000 1002
1005 1003 1008 1001
1005 1005 1002 1005
1004 1006 1003 1007
1006 1003 1007 1002
1000 1008 1001 1005
1007 1009 1001 1000
1006 1009 1009 1003
1006 1000 1007 1005
1005 1006 3947 1003
1001 1006 1004 1006
1005 1006 1002 1002
1006 1004 1005 1002
1002 6988 1007 6744
1009 1000 1000 1005
1000 1001 1006 1003
3163 1000 1005 1004
1004 1007 9279 1006
1006 1006 1004 1000
1001 1001 1004 3449
1000 1004 1001 1009
1008 1002 1006 1005
1005 1006 1005 1006
1003 1009 1007 1009
1003 1005 1003 1007
9575 1004 1007 1008
1002 1003 1007 1007
1008 1004 1001 1006
1009 1007 4139 1006
1009 1001 9682 1008
1007 1000 1002 1006
1006 1005 1009 1001
5349 1000 1008 1008
1009 1002 1008 1000
1002 1000 1005 1006
5826 1001 1002 1004
1009 1003 1008 1001
3059 1003 1000 8602
1003 7336 1006 1000
1003 1009 1001 1009
"""
    print("Part 3 answer:")
    print(solve3(input))


if __name__ == "__main__":
    main()
