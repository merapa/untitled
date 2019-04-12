def perm(temp,target_list, n, r):
    if (r == n):
        temp.append(list(target_list))
    else:
        for i in range(r, n):
            target_list[r], target_list[i] = target_list[i], target_list[r]
            temp = perm(temp, target_list, n, r + 1)
            target_list[r], target_list[i] = target_list[i], target_list[r]
    return temp

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rooms = [x for x in range(1,N)]
    maps=[]
    for i in range(N):
        maps.append(list(map(int, input().split())))
    temp = perm([],rooms, len(rooms), 0)

    for i in range(len(temp)):
        temp[i].insert(0,0)
        temp[i].append(0)
        print(temp[i])

    min = 10000000; sum = 0
    for i in range(len(temp)):
        for j in range(len(rooms)+1):
            sum += maps[temp[i][j]][temp[i][j+1]]
        if sum < min :
            min = sum
        sum=0
    print("#"+str(test_case),min)