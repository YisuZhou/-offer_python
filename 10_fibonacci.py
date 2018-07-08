'''
斐波那契数列
f(n)=f(n-1)+f(n-2)
递归实现与循环实现两种版本
'''
class solution:
    def __init__(self):
        self.result_0 = 0
        self.result_1 = 1


    def fibo_digui(self,input_num) :
        if input_num == 0:
            return 0
        elif input_num == 1 :
            return 1
        else:
            return (self.fibo_digui(input_num-1)+self.fibo_digui(input_num-2))

    def fibo_iter(self,input_num):
        if input_num < 0:
            print('您输入的是负数，请输入一个正整数')
            return -1
        elif input_num <= 1:
            return input_num
        else:
            for iter_num in range(input_num-1):
                self.result = self.result_0 + self.result_1
                self.result_0 = self.result_1
                self.result_1 = self.result

            return self.result






if __name__ == '__main__':
    num_fibo = 4
    solu = solution()
#    result_fibo = solu.fibo_digui(num_fibo)
    result_fibo = solu.fibo_iter(num_fibo)
    print(result_fibo)
