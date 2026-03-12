class solution:
    def printAscendingNumberTriangle(self, n):
        num = 1
        for row in range(1,n+1):
            for col in range(1,row+1):
                print(num,end=' ')
                num += 1 
            print()
