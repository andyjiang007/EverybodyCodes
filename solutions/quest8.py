###
# Quest 8
# 11/20/2024
###


def solve1(input):
    result = 0
    layer = 0
    totalStones = 0
    for layer in range(1, 10000):
        curLayer = layer * 2 - 1
        totalStones += curLayer
        if totalStones >= input:
            break
    result = (totalStones - input) * (layer * 2 - 1)
    return result


def solve2(input):
    result = 0
    layer = 2
    totalStones = 1
    thickness = 1
    for layer in range(2, 10000):
        curThinkness = (thickness * input) % 1111
        # print(curThinkness)
        curLayer = curThinkness * (layer * 2 - 1)

        totalStones += curLayer
        thickness = curThinkness
        if totalStones >= 20240000:
            break

    print(totalStones)
    print(layer)
    result = (totalStones - 20240000) * (layer * 2 - 1)
    return result


def solve3(input):
    result = 0
    HIGH_PRIEST_ACOLYTES = 10
    TOTAL_SUPPLY = 202400000
    layer = 2
    totalStones = 1
    thickness = 1
    pastThickness = [1]
    for layer in range(2, 10000):
        curThinkness = (thickness * input) % HIGH_PRIEST_ACOLYTES + HIGH_PRIEST_ACOLYTES
        # print(curThinkness)
        curLayer = curThinkness * (layer * 2 - 1)
        pastThickness.insert(0, curThinkness)

        removedBlocks = 0
        for col in range(1, layer):
            curHeight = sum(pastThickness[: col + 1])
            # print("curHeight: " + str(curHeight))
            removedBlocks += (
                (layer * 2 - 1) * input * curHeight
            ) % HIGH_PRIEST_ACOLYTES
            if col != layer - 1:
                removedBlocks += (
                    (layer * 2 - 1) * input * curHeight
                ) % HIGH_PRIEST_ACOLYTES
        # print(removedBlocks)
        totalStones += curLayer
        thickness = curThinkness
        if totalStones - removedBlocks >= TOTAL_SUPPLY:
            totalStones = totalStones - removedBlocks
            break

    print(totalStones)
    print(layer)
    result = totalStones - TOTAL_SUPPLY
    return result


def main():
    inputExample = 13
    input = 4099239
    print("Part 1 answer:")
    print(solve1(input))

    input = 397
    print("Part 2 answer:")
    print(solve2(input))

    input = 978167
    print("Part 3 answer:")
    print(solve3(input))


if __name__ == "__main__":
    main()
