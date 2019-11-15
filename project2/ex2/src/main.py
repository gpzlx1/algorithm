import createString
import readSize
import os
import time
import sys
import LCS

if __name__ == '__main__':
    size = readSize.readSize('input/size.txt')
    #每轮都会随机产生字符串，所以这里写入时为了保存，而不是读取
    inputA = open('input/inputA.txt','w')
    inputB = open('input/inputB.txt','w')
    timeTXT = open('output/time.txt', 'w')
    for key, value in size.items():
        for m,n in value:
            str1 = createString.createString(m) #产生指定长度的字符串
            str2 = createString.createString(n)
            if(key == str('A')):                #将产生的字符串保存起来
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
    