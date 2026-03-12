class solution:
    def printRightAngledNumberTriangle(self, n):
        #Write your code here...
        # for row in range(1,n+1):
        #     for col in range(1,row+1):
        #         print(row,end=' ')
        #     print()
        for i in range(1,n+1):
            print((str(i) + ' ')*i)
