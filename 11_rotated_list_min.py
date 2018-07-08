'''
递增的旋转数列，找出最小值
'''
class solution:

    def find_min(self,input_list):
        len_list = len(input_list)
        inx_head = 0
        inx_tail = len_list-1
        inx_mid = (len_list-1)//2
        head = input_list[inx_head]
        tail = input_list[inx_tail]
        mid = input_list[inx_mid]
        if len_list<=2:
            return min(head,tail)
        elif (mid > head and tail > head) :
            return self.find_min(input_list[inx_head:inx_mid])
        elif (mid>head and head>=tail):
            return self.find_min(input_list[inx_mid:inx_tail+1])
        elif (mid<head):
            return self.find_min(input_list[inx_mid:inx_tail+1])
        elif  mid == head and tail < head:
            return self.find_min(input_list[inx_mid:inx_tail + 1])
        elif mid == head and tail > head:
            return mid
        else:#都相等，判断不出来
            return self.min_ordered(input_list[:])

    def min_ordered(self,list_ordered):
        min_list = list_ordered[0]
        for num_list in list_ordered:
            if (min_list > num_list):
                min_list = num_list
        return min_list


if __name__ =='__main__':
    list_in =[1,2,1,1,1,1]
    solu = solution()
    min_list = solu.find_min(list_in)
    print(min_list)