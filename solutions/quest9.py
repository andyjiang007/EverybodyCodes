###
# Quest 9
# 11/22/2024
###


def solve1(input):
    result = 0
    STAMPS = [1, 3, 5, 10]
    targets = [int(line) for line in input.split("\n") if line]
    print(targets)

    beetlesNeeded = [0]
    maxTarget = max(targets)
    for step in range(1, maxTarget + 1):
        minNeeded = maxTarget
        for stamp in STAMPS:
            if step - stamp >= 0:
                minNeeded = min(minNeeded, beetlesNeeded[step - stamp] + 1)
        beetlesNeeded.append(minNeeded)
    print(beetlesNeeded)
    for target in targets:
        result += beetlesNeeded[target]
    return result


def solve2(input):
    result = 0
    STAMPS = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    targets = [int(line) for line in input.split("\n") if line]
    print(targets)

    beetlesNeeded = [0]
    maxTarget = max(targets)
    for step in range(1, maxTarget + 1):
        minNeeded = maxTarget
        for stamp in STAMPS:
            if step - stamp >= 0:
                minNeeded = min(minNeeded, beetlesNeeded[step - stamp] + 1)
        beetlesNeeded.append(minNeeded)
    print(beetlesNeeded)
    for target in targets:
        result += beetlesNeeded[target]
    return result


def solve3(input):
    result = 0
    STAMPS = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    targets = [int(line) for line in input.split("\n") if line]
    print(targets)

    targetRange = []
    for target in targets:
        targetRange.append((target - 100) // 2)
        targetRange.append((target + 100) // 2 + 1)

    beetlesNeeded = [0]
    maxTarget = max(targetRange)
    for step in range(1, maxTarget + 1):
        minNeeded = maxTarget
        for stamp in STAMPS:
            if step - stamp >= 0:
                minNeeded = min(minNeeded, beetlesNeeded[step - stamp] + 1)
        beetlesNeeded.append(minNeeded)
    print(beetlesNeeded)
    for target in targets:
        minNeeded = target
        for firstTarget in range(target + 1):
            secondTarget = target - firstTarget
            if secondTarget - firstTarget > 100:
                continue
            elif secondTarget < firstTarget:
                break
            minNeeded = min(
                minNeeded, beetlesNeeded[firstTarget] + beetlesNeeded[secondTarget]
            )
        # print(minNeeded)
        result += minNeeded
    return result


def main():
    inputExample = """
2
4
7
16
"""
    input = """
12511
16396
11345
10000
10059
18375
17124
10099
10107
10571
"""
    print("Part 1 answer:")
    print(solve1(input))
    inputExample = """
33
41
55
99
"""
    input = """
1854
1615
1814
1437
1978
1164
1799
1523
1936
1511
1712
1427
1577
1780
1665
1335
1424
1198
1837
1515
1736
1039
1082
1423
1480
1038
1997
1358
1156
1688
1893
1530
1447
1371
1838
1265
1813
1209
1332
1620
1706
1852
1968
1015
1241
1222
1306
1964
1795
1313
1662
1753
1511
1494
1541
1591
1023
1570
1603
1500
1854
1650
1602
1829
1502
1445
1638
1639
1098
1634
1318
1224
1156
1522
1161
1860
1199
1098
1786
1431
1079
1202
1517
1294
1905
1331
1691
1699
1080
1570
1671
1193
1503
1028
1137
1732
1574
1275
1789
1050
"""
    print("Part 2 answer:")
    print(solve2(input))
    inputExample = """
156488
352486
546212
"""
    input = """
186212
189238
128007
187182
151585
168524
187485
196495
199164
113926
161041
188334
180115
135481
102807
131708
143856
123816
129153
166142
187596
139100
116590
127838
132680
186094
188900
129952
165895
123571
106748
198798
173209
113981
107791
102075
179171
169560
157450
127909
189003
195678
155035
137606
156207
189591
168021
134740
130817
141380
100526
101132
104122
107150
158267
171750
142087
139232
162637
155077
106261
143946
149687
155020
126466
141454
190799
117620
108539
170314
122370
199103
187971
144189
133174
143672
166274
192708
147481
116208
178034
117052
101688
113188
101023
128809
100953
137407
150906
119189
173750
148009
104035
103279
146587
132017
195839
157696
113138
188241
"""
    print("Part 3 answer:")
    print(solve3(input))


if __name__ == "__main__":
    main()
