T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    application = []

    for i in range(N):
        s,e = map(int,input().split())
        application.append([s,e,e-s])

    time_table = [ [x,0] for x in range(0,24)]
    print(time_table)
print(application)