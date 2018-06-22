def replace(str_in,target,str_replace):
    '''
    :param str_in: 输入字符串
    :param target: 待替换的字符
    :param str_replace: 替换成的字符
    :return:
    遍历，找出一共多少个target，预留长度，从后往前替换
    '''
    count_t = 0
    len_old = len(str_in)

    for char_in in str_in:
        if char_in == target:
            count_t +=1

    len_replace = len(str_replace)
    str_tail = '%'*(len_replace-1)*count_t#原来target有一位，所以只要len-1就好
    str_in = str_in + str_tail

    len_new = len(str_in)

    i_old = len_old-1
    i_new = len_new-1


    while(i_old>=0 and i_new>=0):
        while(i_old>=0 and str_in[i_old] != target):#这段里i变化，注意条件i>0
            str_in = list(str_in)#string不能直接修改
            str_in[i_new] = str_in[i_old]
            str_in = ''.join(str_in)#不能直接修改，要先转为list修改之后再用join连接
            i_new -=1
            i_old -=1
        if (str_in[i_old] == target):
            for i in range(len_replace,0,-1):
                str_in = list(str_in)
                str_in[i_new] = str_replace[i-1]
                i_new -= 1
            i_old -= 1
            str_in = ''.join(str_in)
        continue
    return str_in


if __name__ == '__main__':
    str = 'i love nju!'
    print(replace(str,' ','%20'))
