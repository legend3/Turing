#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2022-08-17 18:29:15
lastTime: 2022-10-07 03:24:49
LastAuthor: Do not edit
FilePath: /Turing/algorithm/algorithm_test.py
Description:
version: 
'''

import pytest


# 冒泡排序
@pytest.mark.parametrize('arr', [[123,123234,24,5,234,0,234]])
def test_baobao(arr):
    n = len(arr) # 数组长度
    for i in range(n): # 遍历多少轮
        for j in range(0, (n - i - 1)): # 比较多少次
            if arr[j] > arr[j+1]: # 前 > 后
                arr[j], arr[j+1] = arr[j+1], arr[j] # 前与后交换位置
    print(arr)


# @pytest.fixture()
# def start(request):
#     return request.config.getoption("--start")  # 命令行中传入参数的方式


# 快速排序
@pytest.mark.parametrize('arr', [[34,56,43,5,7,453,5,6453,265424,35,5475]])
def test_quick_sort(arr):
    start = 0
    end = len(arr) - 1
    
    def quick_sort(start, end) -> list:
        if start >= end:
            return
        mid = arr[start]
        left = start
        right = end
        while left < right:
            while arr[right] >= mid and left < right:
                right -= 1
            arr[left] = arr[right]
            while arr[left] < mid and left < right:
                left += 1
            arr[right] = arr[left]
            arr[left] = mid
        quick_sort(start, left - 1)
        quick_sort(right + 1, end)
        quick_sort(0, len(arr) - 1)
        return arr
    print(quick_sort(start, end))


# 插入排序
@pytest.mark.parametrize('arr', [[34,56,43,5,7,453,5,6453,265424,35,5475]])
def test_insert_sort(arr):
    for i in range(len(arr)):  # 比较多少轮次
        sos = i
        while arr[sos - 1] >= arr[sos] and sos - 1 >= 0:
            arr[sos - 1], arr[sos] =  arr[sos], arr[sos - 1]
            sos -= 1
    print(arr)


#月 1 2 3 4 5 6 7 8
#   1 1 1 1 1
#   0 0 1 1 1
#   0 0 0 1 1
#   0 0 0 0 1
#   0 0 0 0 1


# 兔子窝：[1,1,2,3,5] # 斐波那契额数列
@pytest.mark.parametrize('num', [6])
def test_rabbitBabies(num):
    def rabbitBabies(num):
        if num == 1:
            return 1
        if num == 2:
            return 1
        return rabbitBabies(num - 1) + rabbitBabies(num - 2)
    print(rabbitBabies(num))


# 明明的随机数
import random
@pytest.mark.parametrize('num_count', [3], ids=["明明的随机数"]) # 生成多少个随机数
def test_randomNum(num_count: int):
    # num_set = set() # 1.去重
    # for n in range(num_count):
    #     num_set.add(random.randint(num_count,1000)) # 生成随机数
    # for i in sorted(num_set):
    #     print(i)

    # 牛客网标准答案
    while True:
        try:
            # num_count = int(input())
            sample = set()
            for i in range(num_count):
                sample.add(int(input()))
            for j in sorted(sample):
                print(j)
        except:
            break


# 进制换算
@pytest.mark.parametrize('n, m', [('0xA', 16),('100', 2),('100', 10),('100', 8)]) # 生成多少个随机数
def test_jinzhi(n: str, m: int):
    print(int(n, base=m))


# 质数: 除了1和它本身以外不再有其他因数的自然数
# 质因子: 
    # 255的因子: 1、3、5、15、17、51、85、255
    # 255的质因子: 1、3、5、17
    # 质因子特性: 一个整数只有一个质因子大于质数的平方根
import math
@pytest.mark.parametrize('n', [255])
def test_zhiyinzi(n):
    for i in range(2, int(math.sqrt(n)) + 1): # 如果到sqrt(n)后还是没找到质因子，当再往上找时不会再有质因子
        while n % i == 0: # i是否是能被整除的
            print(int(i), end=" ")
            n /= i # 除以i,缩小
    if n > 1: # 跳出for循环时，如果(最后的)n>1,说明还有一个质因子没有输出就是当前n本身，继续输出这个n
        print(int(n), end=" ")


# 取近似值
@pytest.mark.parametrize('n', [45.46])
def test_qujinsizhi(n):
    # print(round(n))
    
    sn = str(n).split(".")
    if int(sn[1][0]) >= 5:
        print(int(sn[0])) + 1
    else:
        print(int(n))
    
# 合并表记录
@pytest.mark.parametrize('n', [4])
def test_hebingbiaojilu(n):
    pass

# 提取不重复整数
@pytest.mark.parametrize('string', ['11223344'])
def test_buchongfuzhengshu(string):
    c = ''
    r = string[::-1]
    for i in range(len(string)): # 遍历字符串每个字符
        if r[i] not in c: # 判断被遍历出的字符是否在拼接字符串c中
            c += r[i] # 没有就拼接入字符串c
    print(c)

# 字符个数统计
@pytest.mark.parametrize('string', ['fd\nsf 3\n'], ids=['字符个数统计'])
def test_tongjizifu(string: str):
    a = ''
    for i in string.strip('\n'): # 换行符不在ASCII中
        if i not in a:
            a = a + i
    print(len(a))
    
# 数字颠倒
@pytest.mark.parametrize('n', [1234567, 100])
def test_shuzidiandao(n):
    print(str(n)[::-1])


# 字符串中字符出现次数
@pytest.mark.parametrize('strings, target', [('hello23@$$#51sss', 's')])
def test_stringCounts(strings: str, target: str) -> int:
    # print('ab242  ccc'.count('s'))
    strings = strings.strip()
    num = 0
    if(len(strings) > 0 and len(target) == 1):
        for i in strings.lower():
            if i == target.lower():
                num += 1
        print(num)
    else:
        print(0)

# 单词倒排序
@pytest.mark.parametrize('words', ['i1am2legend3'])
def test_reverseString(words):
    words.strip()
    for w in words:
        if not w.isalpha(): # 不是字母
            words = words.replace(w, " ")

    words = words.split(" ")
    words = words[::-1]
    print(' '.join(words))
    
# print(ord('a'),ord('z'))
# print(ord('A'),ord('Z'))
# print(ord('1'), ord('9'))

# 输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
# @pytest.mark.parametrize('words', ('He12llo*&(&(8') # 当每个字符为一个case
@pytest.mark.parametrize('words', ['He12llo*&(&(8'])
def test_charNumber(words):
    # l = lambda: [i for i in words]
    # print(l())
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for w in words:
        if ord(w) in range(96, 121):
            l1.append(w)
            # print(l1)
        elif ord(w) in range(65, 90):
            l2.append(w)
            # print(l2)
        elif ord(w) in range(49, 57):
            l3.append(w)
            # print(l3)
        else:
            l4.append(w)
    print(len(l1), len(l2), len(l3), len(l4))

# 字符串最后一个单词的长度
@pytest.mark.parametrize('string', ['  hello world  '])
def test_gen_len(string: str) -> int:
    string_list = string.strip().split() # 默认空格分隔
    if(len(string) == 0) or (len(string) >= 5000):
        return 0
    else:
        print(len(string_list[-1]))


# 字符串分割
@pytest.mark.parametrize('string', [pytest.param('  hello sdfd 543 ')])
def test_split_string(string):
    l = []
    while len(string) > 8:
        l.append(string[:8])
        string = string[8:]
    l.append("{:<8}".format(string))
    #l.append('{:a<8}'.format(string))    # a补全
    print(l)
    return l
# print(test_split_string('  hello sdfd 543 '))


# 字符串加解密
@pytest.mark.parametrize('string', ['ASDSZAFazf123SFafd4sf553mk35zjjfhuer'], ids=['加密'])
def test_encrypt_decrypt(string):
    res = ''
    for i in string:
        if i.isupper(): # 大写字母
            if i == 'Z':
                res += 'a'
            else:
                res += chr(ord(i.lower()) + 1)
        elif i.islower(): # 小写字母
            if i == 'z':
                res += 'A'
            else:
                res += chr(ord(i.upper()) + 1)
        elif i.isdigit(): # 数字
            if i == '9':
                res += '0'
            else:
                res += str(int(i) + 1)
    print(res)
    
# 字符串排序
'''
输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述：
数据输出n行,输出结果为按照字典序排列的字符串。'''
@pytest.mark.parametrize('word', [['cap',
                                    'to',
                                    'cat,'
                                    'card',
                                    'two',
                                    'too',
                                    'up',
                                    'boat',
                                    'boot']], ids=['字符串排序'])
def test_stringsort(word):
    
    n = int(input())
    a = ['cap',
        'to',
        'cat',
        'card',
        'two',
        'too',
        'up',
        'boat',
        'boot']
    # for i in range(n):
    #     b = word
    #     a.append(b)
    a.sort() # 对所有输入进行排序
    for i in range(n):
        print(a[i])



@pytest.mark.parametrize('string', ['ASDSZAFazf123SFafd4sf553mk35zjjfhuer'], ids=['字符串分隔'])
def test_stringApart(string):
    # string = input()
    print("\n")
    c = ''
    t = 0
    for i in string:
        c += i
        if len(c) == 8:
            print(c)
            c = ''
            t += 1
        
        if 0 < len(string[t*8:]) < 8:
            print(string[t*8:] + '0'*(8 - len(string[t*8:])))
            break

@pytest.mark.parametrize('string', ['i am a man'], ids=['句子逆序'])
def test_juzinixu(string):
    l = string.split(" ")
    l.reverse()
    print(' '.join(l))


@pytest.mark.parametrize('num', ['5'], ids=['二进制中1的个数'])
def test_erjinzhizhongyidegeshu(num):
    # n = int(input())
    nn = bin(int(num))[2:].count('1') # 转二进制，寻找二进制1的个数
    print(nn)


@pytest.mark.parametrize('num', ['5'], ids=['购物车'])
def test_gouwuche(num):
    pass


@pytest.mark.parametrize('coordinates', ['A10;S20;W10;D30;X;A1A;B10A11;;A10;'], ids=['坐标移动'])
def test_coordinates(coordinates):
    coordinates_list = coordinates.split(";")
    # print(coordinates_list) # ['A10', 'S20', 'W10', 'D30', 'X', 'A1A', 'B10A11', '', 'A10', '']
    coordinates_dict = {'A': 1, 'D': 2, 'W': 3, 'S': 4}
    x, y = 0, 0 # 纵、横坐标
    
    for coordinate in coordinates_list:
        if not coordinate: # 坐标为空时
            continue
        judge = coordinates_dict.get(coordinate[0], 0) # 获取坐标方向
        if judge and len(coordinate) <= 3: # 符合的坐标
            number = -1
            try:
                number = int(coordinate[1:]) # 获取坐标位移长度
            except: # 可能不是数字，int()会异常
                pass
            if number >= 0:
                if judge == 1:
                    x -= number
                elif judge == 2:
                    x += number
                elif judge == 3:
                    y += number
                else:
                    y -= number
    # print(x, y, sep=',')
    assert (x, y) == (10, -10)


@pytest.mark.parametrize('strings', [''], ids=['识别有效的IP地址和掩码并进行分类统计'])
def test_coordinates(strings):
    pass


@pytest.mark.parametrize('', [''], ids=[''])
def test_coordinates():
    pass