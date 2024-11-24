###
# Quest 7
# 11/19/2024
###
from itertools import permutations


def traverse_track(track):
    inputArray = [line for line in track.split("\n") if line]
    rows, cols = len(inputArray), len(inputArray[0])
    result = []
    visited = [[False] * cols for _ in range(rows)]  # Track visited cells

    # Directions: right, down, left, up (clockwise)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize traversal
    row, col = 0, 0

    hasNextMove = True
    while hasNextMove:
        # Add the current cell to the result
        result.append(inputArray[row][col])
        visited[row][col] = True
        # print("".join(result))

        hasNextMove = False
        for dir_index in range(4):
            # Try to move in the current direction
            next_row, next_col = (
                row + directions[dir_index][0],
                col + directions[dir_index][1],
            )

            # Check if the move is valid (within bounds, unvisited, and part of the loop)
            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and not visited[next_row][next_col]
                and inputArray[next_row][next_col] != " "
            ):
                row, col = next_row, next_col  # Move to the next cell
                hasNextMove = True
                break

    return result[1:] + ["S"]


def solve1(input):
    result = 0
    chariots = {}
    inputArray = [line for line in input.split("\n") if line]
    for line in inputArray:
        [name, plans] = line.split(":")
        plan = [char for char in plans.split(",") if char]
        chariots[name] = plan
    print(chariots)

    finalPower = {}
    for chariot in chariots.keys():
        plan = chariots[chariot]
        powerSum = 0
        curPower = 10
        for i in range(10):
            char = plan[i % len(plan)]
            if char == "+":
                curPower += 1
            elif char == "-":
                curPower -= 1
            powerSum += curPower
        finalPower[chariot] = powerSum
    print(finalPower)

    result = sorted(finalPower.keys(), key=lambda k: finalPower[k], reverse=True)
    return result


def solve2(input, inputTrack):
    result = 0
    chariots = {}
    inputArray = [line for line in input.split("\n") if line]
    for line in inputArray:
        [name, plans] = line.split(":")
        plan = [char for char in plans.split(",") if char]
        chariots[name] = plan
    print(chariots)
    track = traverse_track(inputTrack)
    print(track)

    finalPower = {}
    for chariot in chariots.keys():
        plan = chariots[chariot]
        powerSum = 0
        curPower = 10
        for i in range(len(track) * 10):
            char = plan[i % len(plan)]
            trackChar = track[i % len(track)]
            if trackChar == "+":
                curPower += 1
            elif trackChar == "-":
                curPower -= 1
            elif char == "+":
                curPower += 1
            elif char == "-":
                curPower -= 1
            powerSum += curPower
        finalPower[chariot] = powerSum
    print(finalPower)

    result = sorted(finalPower.keys(), key=lambda k: finalPower[k], reverse=True)
    return result


def solve3(input, inputTrack):
    result = 0
    chariots = {}
    inputArray = [line for line in input.split("\n") if line]
    for line in inputArray:
        [name, plans] = line.split(":")
        plan = [char for char in plans.split(",") if char]
        chariots[name] = plan
    print(chariots)
    track = traverse_track(inputTrack)
    print(track)

    actions = "+++++---==="
    possiblePlans = list(set("".join(p) for p in permutations(actions)))
    print(len(possiblePlans))
    for i in range(len(possiblePlans)):
        chariots[str(i)] = possiblePlans[i]

    plan = chariots["A"]
    targetSum = 0
    curPower = 10
    for i in range(len(track) * 2024):
        char = plan[i % len(plan)]
        trackChar = track[i % len(track)]
        if trackChar == "+":
            curPower += 1
        elif trackChar == "-":
            curPower -= 1
        elif char == "+":
            curPower += 1
        elif char == "-":
            curPower -= 1
        targetSum += curPower

    for chariot in chariots.keys():
        if chariot == "A":
            continue

        plan = chariots[chariot]
        powerSum = 0
        curPower = 10
        for i in range(len(track) * 2024):
            char = plan[i % len(plan)]
            trackChar = track[i % len(track)]
            if trackChar == "+":
                curPower += 1
            elif trackChar == "-":
                curPower -= 1
            elif char == "+":
                curPower += 1
            elif char == "-":
                curPower -= 1
            powerSum += curPower
        if powerSum > targetSum:
            result += 1

    return result


def main():
    inputExample = """
A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+
"""
    input = """
C:-,=,+,+,-,+,+,-,=,=
G:-,-,=,+,-,=,=,+,+,+
D:=,-,-,+,+,+,-,=,=,+
J:-,+,+,=,=,=,+,+,-,-
E:-,=,+,+,-,-,+,=,=,+
I:+,=,-,=,-,-,=,+,+,+
H:-,=,-,+,+,=,=,-,+,+
F:-,-,=,+,-,+,=,+,=,+
B:+,+,=,-,-,+,-,=,=,+
"""
    print("Part 1 answer:")
    print(solve1(input))
    exampleTrack = """
S+===
-   +
=+=-+
"""
    input = """
A:=,+,-,+,-,+,=,-,-,-,=,+,+,=,+,+,+,+,+,=,-,-,=,+,+,-,+,=,=,=,+,+,+,+,-,=,-,+,+,+
D:=,-,=,+,=,+,+,-,+,+,=,=,=,+,-,-,+,-,+,-,+,-,+,+,+,-,=,+,+,-,+,+,+,+,=,=,=,+,+,-
E:+,=,=,+,-,=,+,=,+,=,+,+,-,-,+,-,=,+,+,-,+,-,+,-,+,+,+,+,=,+,+,+,+,-,-,=,=,=,-,+
H:=,+,-,+,+,+,-,-,+,+,+,=,-,-,=,+,=,=,+,+,-,=,+,=,+,+,-,-,+,+,+,-,+,=,+,+,=,+,=,-
G:+,+,+,-,+,+,-,+,=,-,-,=,+,+,+,-,-,+,-,=,-,+,+,=,+,=,=,=,+,+,=,+,+,=,-,+,=,+,-,+
B:=,+,+,+,+,=,-,-,+,+,+,=,+,+,-,+,=,+,-,+,=,+,-,=,+,+,=,-,=,=,-,+,-,+,+,+,-,=,-,+
C:-,+,-,=,+,+,=,=,=,+,+,+,-,=,+,-,+,-,+,+,+,=,-,+,+,-,+,+,=,=,+,-,+,+,+,+,=,-,=,-
I:+,=,-,=,+,=,+,-,-,+,-,=,+,+,+,-,+,-,+,+,-,-,=,+,-,+,+,=,+,-,=,=,=,+,+,+,+,=,+,+
J:-,+,=,=,-,+,+,+,-,-,+,=,=,-,+,+,-,=,+,+,-,+,+,=,-,=,=,-,+,+,+,+,+,-,+,=,+,+,+,=
"""
    inputTrack = """
S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-
"""
    print("Part 2 answer:")
    print(solve2(input, inputTrack))
    input = """
A:=,+,+,-,=,=,+,-,-,+,+
"""
    inputTrack = """
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=       
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =          
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-
"""
    print("Part 3 answer:")
    print(solve3(input, inputTrack))


if __name__ == "__main__":
    main()
