import random
'''思路：1.生成一个基于cct字符串长度的随机数
        2.遍历氨基酸列表，从中取出每一个元素，替换cct列表中的元素
        3.替换后的字符串，形成新的列表
        4.其实单点突变可以从头开始逐个遍历字符串替换
        5.加入随机数为了方便以后写n个点突变
        6.n个点突变可以使用随机替换n次的方法，在替换一次的文件列表中，引入另n个随机点突变'''
# 打开cct文件
with open('ORI.txt') as f:
    lines = f.readlines()
    strip_lines = [s.replace('\n', '') for s in lines]  # 去除列表中元素的'\n'
    # print(strip_lines)
    cct_seq = strip_lines[1]
    # myset = set(cct_seq)
    # for item in myset:
    #     print(item, cct_seq.count(item))
print(cct_seq)
# print(strip_lines)
print(len(cct_seq))
# new = cct_seq.replace('A','a')
# print(new)

# 生成随机数列表
def rl():
    # print(random_list)
    # print(len(random_list))
    list_aa = ['G','A','V','L','I','F','W','Y','D','N','E','K','Q','M','S','T','C','P','H','R']
    # print(len(list_aa))
    # print(list_aa)
    aa_list = []
    all_list = []
    for i in range(1,len(cct_seq)-1):# 不包括起始和终止密码子
        for k in list_aa:
            new = cct_seq.replace(cct_seq[i], k)
            all_list.append('>CCT-'+ cct_seq[i]+str(i+1)+ str(k)) #注释信息
            all_list.append(new)
    # print(all_list)
    # print(len(all_list))
    file = open('seq.txt', 'w')
    for i in range(len(all_list)):
        # 列表写入txt进行格式修改
        s = str(all_list[i]).replace('{', '').replace('}', '').replace("'", '').replace(':', ',') + '\n'
        file.write(s)
    file.close()
    print('单点随机突变序列生成完成')

rl()
