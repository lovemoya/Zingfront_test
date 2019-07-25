def get_second_word(str1, str2):  # 第二公共单词
    # 判断字符串是否为空
    if not str1.strip():
        return 'Null'
    if not str2.strip():
        return 'Null'
    # 将字符串变成数组来进行比较
    arr1 = str1.split(' ')
    arr2 = str2.split(' ')
    # 判断单词是否够长度
    if len(arr1) < 2:
        return 'Null'
    if len(arr2) < 2:
        return 'Null'
    # 如果两个句子一样则返回第二个的第二位
    if arr1 == arr2:
        return arr2[1]
    # 新建一个空数组
    arr = []
    # 循环他们 进行比较
    for i in arr1:
        for j in arr2:
            if i == j:
                # 放到数组中
                arr.append(i)
    # 判断数组中是否有值
    if len(arr) > 1:
        print("两个字符串的第二公共单词是：", arr[0])
        return arr[0]
    else:
        return 'Null'


if __name__ == '__main__':
    str1 = input("请输入第一组字符串，空格隔开：")
    str2 = input("请输入第二组字符串：")
    get_second_word(str1, str2)
