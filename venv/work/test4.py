T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int,input().split(" "))
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    carryed = 0

    wi.sort()
    ti.sort()
    print(wi)
    print(ti)

    max_loop1 = len(wi)
    max_loop2 = len(ti)
    wi_max_index = len(wi) - 1
    ti_max_index = len(ti) - 1

    for i in range(max_loop1):
        for j in range(max_loop2):
            while wi_max_index >= 0 and ti_max_index >= 0 :
                if wi[wi_max_index] > ti[ti_max_index]:
                    wi_max_index = wi_max_index-1
                elif wi[wi_max_index] <= ti[ti_max_index]:
                    carryed += wi[wi_max_index]
                    wi_max_index = wi_max_index-1
                    ti_max_index=ti_max_index-1
                    break
                else:
                    ti_max_index=ti_max_index-1
    print("#"+str(test_case),carryed)