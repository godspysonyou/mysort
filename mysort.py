import random
'''
直接插入排序，原数组上排序，稳定，O(n2)
'''
def insert_sort(l):
    assert(type(l)==type(['']))
    length = len(l)
    if length<2:
        return l

    for i in range(1,length):
        j = i-1             # 将下标从移到i前面一位
        value = l[i]        # 哨兵，每次比较需要
        while j>=0 and value<l[j]:
            l[j+1]=l[j]     # 比哨兵大的数就要往前放
            j = j-1         # 下标继续往前
        l[j+1] = value      # 记住在j+1插入哨兵
    return l

'''
插入排序-希尔排序,原数组上排序，不稳定，O(n1.3)~O(n2)
'''
def shell_sort(l):
    assert(type(l)==type(['']))
    length =len(l)
    if length<2:
        return l

    step = 2    # 我们固定step=2，简单处理增量
    group = int(length/2)    # 分为几组，增量就是几
    while group>0:           # 直到增量为1
        for i in range(group): # 为每一组进行插入排序
            #j = i + group      # 这里的插入排序，增量(间隔)不在是1，而是group了
            #while j < length:  # j是不会超过length的
            for j in range(i+group,length,group):
                value = l[j]   # 设置哨兵
                k = j - group  # 从哨兵前一个位置开始比较
                while k>=0 and value<l[k]:
                    l[k+group]=l[k]
                    k = k - group
                l[k+group] = value
                #j = j + group
        group = int(group/step)
    return l

'''
选择排序-简单选择排序，原数组上排序，不稳定，O(n2)
'''
def select_sort(l):
    assert(type(l)==type(['']))
    length = len(l)
    if length<2:
        return l

    for i in range(length-1):
        minvalue=min(l[i:])  # 找出当前最小的数，以及下标
        ind=l.index(minvalue)
        l[i],l[ind] = l[ind],l[i] # 与第一个交换
    return l

'''
选择排序-堆排序，原数组上排序，不稳定，O(nlogn)
'''
def heap_sort(l):
    assert(type(l)==type(['']))
    size = len(l) #堆大小命名用size，不用length
    if size<2:
        return l

    def adjust_heap(l,i,size): # i父亲节点
        lchild = 2*i+1
        rchild = 2*i+2
        max = i
        if i < size/2: # 判断i是否为可能的父节点
            if lchild<size and l[lchild]>l[max]: # 第一个条件用来判断子节点是否存在
                max = lchild
            if rchild<size and l[rchild]>l[max]:
                max = rchild
            if max != i: # 这里如果max=i则默认其孩子节点都已经成堆
                l[max],l[i] = l[i],l[max]
                adjust_heap(l,max,size)

    def build_heap(l,size):
        for i in range(0,int(size/2))[::-1]: # 从最后一个父节点开始调整
            adjust_heap(l,i,size)

    #size = len(l)  #堆大小命名用size，不用length
    build_heap(l,size)
    for i in range(0,size)[::-1]:
        l[0],l[i] = l[i],l[0]
        adjust_heap(l,0,i)
    return l

'''
交换排序-冒泡排序,原数组上排序，稳定，O(n2)
'''
def bubble_sort(l):
    assert(type(l)==type(['']))
    length=len(l)
    if length<2:
        return l
    for i in range(length-1):            # n-1趟
        for j in range(length-1-i):      # 比较n-1-i次
            if l[j]>l[j+1]:
                l[j+1],l[j] = l[j],l[j+1]
    return l

'''交换排序-快速排序，原数组上排序，不稳定，平均O(nlogn)，最坏O(n2)'''
def quick_sort_use_space(l):
    assert(type(l)==type(['']))
    length = len(l)
    if length<2:
        return l
    left = [i for i in l[1:] if i <= l[0]]  #简化了代码书写，但是却牺牲了空间资源，空间复杂度为O(nlogn)，而下面的算法则为O（1）
    right = [j for j in l[1:] if j > l[0]]
    return quick_sort_use_space(left) +[l[0],]+quick_sort_use_space(right)

def quick_sort(l,left,right):
    assert(type(l)==type(['']))
    length = len(l)
    if length<2:
        return l
    def partition(l,start,end):
        pivot = l[start]     # 以第一个为key
        while start<end:
            while start<end and l[end]>pivot:  # 找出右边比key小的交换
                end-=1
            l[start] = l[end]
            while start<end and l[start]<=pivot:
                start+=1
            l[end] = l[start]
        l[start] = pivot
        return start

    #random pivot
    def random_partition(l,start,end):
        i = random.randint(start,end)
        l[i],l[start] = l[start],l[i]
        return partition(l,start,end)

    if left<right:
        m = partition(l,left,right)
        quick_sort(l,left,m-1)
        quick_sort(l,m+1,right)
    return l

'''归并排序，非原数组上排序，稳定，O(nlogn),空间复杂度O(n)'''
def merge_sort(l):
    assert(type(l)==type(['']))
    length = len(l)
    if length<2:
        return l
    def merge(left,right):
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result+=left[i:]
        result+=right[j:]
        return result
    n=int(length/2)
    left = merge_sort(l[:n])
    right = merge_sort(l[n:])
    merge(left,right)

'''
基数排序，非原数组上排序，稳定，时间复杂度O(d(n+r)),空间复杂度O(n+r)
'''
import math
def radix_sort(l,radix=10):
    assert(type(l)==type(['']))
    length = len(l)
    if length<2:
        return l
    k=math.ceil(math.log(max(l),radix))   # 对数字排序，按位，lsd,其实就是最高位
    buckets = [[] for i in range(radix)]  # 分配桶数
    for i in range(k):                    # K次分配
        for j in l:
            s = int(j/(radix**(i)))%radix # 找到低位的值
            buckets[s].append(j)
        del l[:]
        for bucket in buckets:
            l+=bucket
            del bucket[:]
    return l








