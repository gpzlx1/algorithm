import createString
import readSize
import os
import time
import sys
import LCS

if __name__ == '__main__':
    size = readSize.readSize('input/size.txt')
    
    inputA = open('input/inputA.txt','w')
    inputB = open('input/inputB.txt','w')
    timeTXT = open('output/time.txt', 'w')
    for key, value in size.items():
        for m,n in value:
            str1 = createString.createString(m)
            str2 = createString.createString(n)
            if(key == str('A')):
                inputA.writelines(str1+'\n')
                inputA.writelines(str2+'\n')
            else:
                inputB.writelines(str1+'\n')
                inputB.writelines(str2+'\n')
            t1 = time.time()
            b, c = LCS.LCS(str1, str2)
            print('{}组规模为({}, {})的字符串组的LCS长度为：{}，其中一个解为：'.format(key,m,n,c[-1][-1]), end='')
            LCS.print_LCS(b, str1, m,n)
            print()
            t2 = time.time()
            timeTXT.writelines(str(t2-t1)+' ms\n' )
    