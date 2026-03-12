class solution:
    def printUppercaseLetterPyramid(self, n):
        space = n-1
        cols = 1 
        
        for row in range(1,n+1):
            for sp in range(1,space+1):
                print(' ',end='')
            char = ord('A') #65
            for ch in range(1,cols+1):
                print(chr(char),end='')
                if ch <= cols//2:
                    char += 1 
                else:
                    char -= 1 
            print()
            cols += 2
            space -= 1

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
