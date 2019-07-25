def continue_num_sum():
    num = int(input("输入一个要验证的数: "))  # 这里的话注意数据类型转换
    n = int(num ** 0.5)   # 这里直接开根号，缩小循环范围
    res = []
    # 前可以转化成中间项的倍数，所以下面for循环求得是中间项的值
    for i in range(2, n+1):
        if num % i == 0:
            mid_01 = i  # 中间数
            mid_02 = int(num / i)  # 项数
            # 分解出来为mid_01*mid_02的形式，
            if mid_02 % 2 == 1:  # mid_02为奇数
                first_1 = (mid_01 - mid_02 // 2)
                last_1 = (mid_01 + mid_02 // 2)
                if first_1 >= 0:
                    res.append('+'.join([str(j) for j in range(first_1, last_1 + 1) if j > 0]))
            else:  # mid_02 为偶数，拆分mid_01 比如：125拆成62+63
                if mid_01 % 2 == 1:
                    t_01 = int((mid_01 - 1) / 2)
                    t_02 = int((mid_01 + 1) / 2)
                    if t_01 - mid_02 >= 0:
                        lists_01 = [str(i) for i in range(t_01 - mid_02 + 1, t_01 + 1) if i > 0]
                        lists_02 = [str(i) for i in range(t_02, t_02 + mid_02) if i > 0]
                        res.append('+'.join(lists_01 + lists_02))
            # 此处仅仅将上面的mid_01*mid_02 调换成mid_02*mid_01 中间值和项数对调
            if mid_01 % 2 == 1:
                first_2 = (mid_02 - mid_01 // 2)
                last_2 = (mid_02 + mid_01 // 2)

                if first_2 >= 0:
                    res.append('+'.join([str(j) for j in range(first_2, last_2 + 1) if j > 0]))
            else:  # mid_02 为偶数，拆分mid_01:125拆成62+63
                if mid_02 % 2 == 1:
                    t_01 = int((mid_02 - 1) / 2)
                    t_02 = int((mid_02 + 1) / 2)
                    if t_01 - mid_01 >= 0:
                        lists_01 = [str(i) for i in range(t_01 - mid_01 + 1, t_01 + 1) if i > 0]
                        lists_02 = [str(i) for i in range(t_02, t_02 + mid_01) if i > 0]
                        res.append('+'.join(lists_01 + lists_02))
    # 奇数特殊解
    if num % 2 == 1:
        mid = int((num + 1) / 2)
        res.append('+'.join([str(mid - 1), str(mid)]))
    if res:
        return res
    else:
        return [None]


res = continue_num_sum()
for i in res:
    if i:
        # print(eval(i),end='=')
        print(i)
    else:
        print(i)
