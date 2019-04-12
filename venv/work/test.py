def search(maps, row, col, limits):
    current = 0;
    sum_a = 10000000;
    sum_b = 10000000
    if row + 1 < limits and col + 1 < limits:
        sum_a = search(maps, row + 1, col, limits)
        sum_b = search(maps, row, col + 1, limits)
    elif row + 1 >= limits and col + 1 < limits:
        sum_b = search(maps, row, col + 1, limits)
    elif col + 1 >= limits and row + 1 < limits:
        sum_a = search(maps, row + 1, col, limits)
    current += maps[row][col]
    if sum_a > sum_b and sum_b < 10000000:
        current += sum_b
    elif sum_a <= sum_b and sum_a < 10000000:
        current += sum_a
    return current

T = int(input())

for test_case in range(1, T + 1):
    limits = int(input())
    maps = [[0] * 3 for x in range(limits)]
    for i in range(limits):
        maps[i] = list(map(int, input().split()))
    sums = 0;
    sums = search(maps, 0, 0, limits)
    print("#" + str(test_case), sums)