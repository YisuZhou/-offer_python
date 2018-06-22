import numpy as np

def find_2d(arr_2d,target):
    '''
    :param arr_2d:
    :param target:
    :return:
    从左到右，从上到下，都递增，找到目标元素
    '''
    [row,col] = arr_2d.shape
    start_i=0
    start_j=0
    while( arr_2d[start_i][0] < target and start_i <= row-1):
        start_i +=1
    while (arr_2d[0][start_j] < target and start_j <= col-1):
        start_j += 1
    if (start_i==0 and start_j==0):
        print("找不到目标")
        exit(-1)
    else:
        start_i -=1
        start_j -=1
    for i in range(start_i,row):
        for j in range(start_j,col):
            if arr_2d[i][j] != target:
                j +=1
            else:
                print("%d位于%d行%d列,起始索引号为0" % (target,i,j))
                return 0

if __name__ == '__main__':
    a = np.array([[1,2,3,4],[4,5,6,7]])
    t = 3
    find_2d(a,t)