W=input()
N=int(input())
L=len(W)
print(W[:N] != W[L-N:L])
