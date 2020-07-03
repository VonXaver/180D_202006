# Filename

def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# 获取用户输入

'''
if __name__ = main()
    recur_fibo()
    pass
20
'''
if __name__ == '__main__':
    nterms = int(input("您要输出几项? "))

    # 检查输入的数字是否正确
    if nterms <= -1:
        print("输入正数")
    else:
        print("斐波那契数列:")
        for i in range(nterms):
            print(recur_fibo(i))
    pass