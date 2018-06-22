def find_dup(list_in):
    '''
    :param list_in:
    :return:
    输入数组长度为n,所有数字都在0-n-1范围内
    找出数组中任意一个重复的数字

    分析：长度为n,范围0-n-1，如果不重复，则下标必定对应数字，
        对每个数字检查，下标与内容不符合就与内容对应的下标交换
        交换过程中如果发现有相等，则重复
    '''
    if list_in == []:
        print("长度不可为0")
        exit(-1)

    n = len(list_in)
    for count_i in range(n):
        if list_in[count_i] >= n or list_in[count_i] < 0:
            print("元素不规范")
        while count_i != list_in[count_i]:
            if list_in[list_in[count_i]] == list_in[count_i]:
                return list_in[count_i]

            list_in[list_in[count_i]],list_in[count_i] = list_in[count_i],list_in[list_in[count_i]]

    print("没有重复元素")

def find_dup_2(list_in):
    '''
    :param list_in:
    :return:
    输入数组长度为n,所有数字都在0-n-1范围内
    找出数组中所有重复的数字

    分析：同上
    '''
    if list_in == []:
        print("长度不可为0")
        exit(-1)
    list_dup = []
    n = len(list_in)
    for count_i in range(n):
        if list_in[count_i] >= n or list_in[count_i] < 0:
            print("元素不规范")
        while count_i != list_in[count_i]:
            if list_in[list_in[count_i]] == list_in[count_i]:
                list_dup.append(list_in[count_i])
                break

            list_in[list_in[count_i]],list_in[count_i] = list_in[count_i],list_in[list_in[count_i]]

    if len(list_dup) == 0:
        print("没有重复元素")
    return list_dup

def find_dup_3(list_in):
    '''
    :param list_in:
    :return:
    如果不允许修改数组的话
    '''
    if list_in == []:
        print("长度不可为0")
        exit(-1)
    n = len(list_in)
    list_dup = []
    list_s = [0]
    list_s = list_s*n
    for list_i in list_in:
        if list_i >= n or list_i < 0:
            print("元素不规范")
        if list_s[list_i] == 0:
            list_s[list_i] = 1
        else:
            list_dup.append(list_i)
            continue
    return list_dup

if __name__ == '__main__':
    lista = [1,3,2,0,2,5,3]
    dup = find_dup_3(lista)
    print(dup)
