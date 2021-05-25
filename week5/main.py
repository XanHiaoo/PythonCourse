num=int(input())
for i in range(num):
    try:
        print('%.2f' % (eval(input())))
        eval()
        # 函数将字符串str当成有效的表达式来求值并返回计算结果。结合math当成一个计算器很好用
        # eval(expression[, globals[, locals]])
    except Exception as e:  #抛出异常
        # try except Exception as e 检查异常
        print(repr(e).split('(')[0])