an = [1,2,3]
tr = [0,0,0]

def comb(n,r):
    if r==0 : print(tr)
    elif n < r: return
    else :
        tr[r-1] = an[n-1]
        comb(n-1,r-1)
        comb(n-1,r)

# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     maps =  [[0]*N for x in range(N)]
#     for i in range(N):
#       maps[i] = list(map(int,input().split()))
#     area = [ i for i in range(1,N+1)]
#     sequence(area)
#     print(area)

comb(3,2)