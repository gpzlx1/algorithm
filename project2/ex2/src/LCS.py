import numpy as np
#coding=utf-8
''' 
1 代表左上
2 代表上
3 代表左
'''
def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    b = np.zeros((m+1,n+1),dtype=int)
    c = np.zeros((m+1, n+1),dtype=int)
    for i in range(0,m):
        for j in range(0, n):
                if str1[i] == str2[j]:
                    c[i+1][j+1] = c[i][j] + 1
                    b[i+1][j+1] = 1  
                elif c[i][j+1] >= c[i+1][j]:
                    c[i+1][j+1] = c[i][j+1] 
                    b[i+1][j+1] = 2   
                else:
                    c[i+1][j+1] = c[i+1][j]
                    b[i+1][j+1] = 3   

    return b,c


#b LCS产生的b
#str1 字符串1
#(x,y) root坐标
def print_LCS(b,str1,x,y):
    if x == 0 or y == 0:
        return ''
    if b[x][y] == 1:
        print_LCS(b,str1,x-1, y-1)
        print(str1[x-1], end='')
    elif b[x][y] == 2:
        print_LCS(b,str1,x-1,y)
    else:
        print_LCS(b, str1, x, y-1)

