# _*_ coding:utf-8 _*_

import re

import requests

qqs = []

headers = {
    "Cookie": "",
    "referer": "https://mail.qq.com/zh_CN/htmledition/ajax_proxy.html?mail.qq.com&v=140521",
}

url = "https://mail.qq.com/cgi-bin/laddr_lastlist?sid=7uHFDstWQVhlK10-&encode_type=js&t=addr_datanew&s=AutoComplete&category=hot&resp_charset=UTF8&ef=js&r=0.17002957703427835"

response = requests.get(url, headers=headers).text

friend_info = re.findall('sortbyupdatetime(.*?)qqgroups', response, re.S)[0]
friend_info = friend_info.strip(" :,[]").split('],[')

# 将编号跟QQ号保存到字典中
dic = {}
for i in friend_info:
    i = i.split(',')
    dic[i[0].strip('""')] = i[2].strip('@qq.com"')

# 将分组中的编号转化为列表形式
qqgroups = re.findall('qqgroups(.*?)groups', response)[0]
qqgroups = qqgroups.strip(" :,[]")[1:-1].split('],[')

# 根据编号提取QQ号
for i in qqgroups:
    find_numbers = re.findall(r'\[(.*?)\]', str(i))[0].split(',')
    for find_number in find_numbers:
        if find_number in dic:
            qqs.append(dic[find_number])

# 保存到文本文件中
with open('qq.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(qqs))

