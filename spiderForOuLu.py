from lxml import etree
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get('https://dict.eudic.net/dicts/en/frustration', headers=headers)

x = etree.HTML(r.text)
all_exp = x.xpath('//*[@id="ExpFCChild"]/div')
print(len(all_exp))
if len(all_exp) == 1:
    print("there1")
    if len(x.xpath('//*[@id="ExpFCChild"]/i')) == 1:
        print("there2")
        print(x.xpath('//*[@id="ExpFCChild"]/i')[0].text,
              x.xpath('//*[@id="ExpFCChild"]/text()')[0])  # part_of_speech, answer
    elif len(x.xpath('//*[@id="ExpFCChild"]/ol')) == 1:
        print("have one ol")
        li_collect = x.xpath('//*[@id="ExpFCChild"]/ol/li')
        part_of_speech = x.xpath('//*[@id="ExpFCChild"]/ol/li[1]/i')
        part_answer = x.xpath('//*[@id="ExpFCChild"]/ol/li[1]/text()')
        print(part_of_speech[0].text, part_answer[0])
        for i in range(1, len(li_collect)):
            print(li_collect[i].text)

elif len(all_exp) == 2:
    print("there3")
    if len(x.xpath('//*[@id="ExpFCChild"]/div[2]/ol/li')) != 0:
        print("ol在div下面")
        all_exp = x.xpath('//*[@id="ExpFCChild"]/div[2]/ol/li')
        print(len(all_exp))
        for i in range(len(all_exp)):
            all_exp[i] = all_exp[i].text
        print(all_exp)
    elif len(x.xpath('//*[@id="ExpFCChild"]/ol')) != 0:
        print(len(x.xpath('//*[@id="ExpFCChild"]/ol/li')))
        for i in range(1, len(x.xpath('//*[@id="ExpFCChild"]/ol/li')) + 1):
            strs = '//*[@id="ExpFCChild"]/ol/li' + '[' + str(i) + ']'
            print("---------------")
            if len(x.xpath(strs + '/i')) != 0:# x.xpath(strs + '/i') != 0:
                print(x.xpath(strs + '/i/text()') )
                print(x.xpath(strs + '/text()'))
            else:
                print(x.xpath(strs + '/text()'))
    elif len(x.xpath('//*[@id="ExpFCChild"]/i')) != 0:
       print(x.xpath('//*[@id="ExpFCChild"]/i/text()') + x.xpath('//*[@id="ExpFCChild"]/text()'))
    else:
        print(x.xpath('//*[@id="ExpFCChild"]/div[2]/text()'))

# //*[@id="ExpFCChild"]/ol/li[2]


elif len(all_exp) == 3:
    if len(x.xpath('//*[@id="ExpFCChild"]/div[2]/ol')) == 0:
        print(x.xpath('//*[@id="ExpFCChild"]/div[2]/text()'))
    else:
        print("has three divs")
        all_exp = x.xpath('//*[@id="ExpFCChild"]/div[2]/ol/li')
        for i in range(1, len(all_exp) + 1):
            strs = '//*[@id="ExpFCChild"]/div[2]/ol/li' + '[' + str(i) + ']' + '/text()'
            print(x.xpath(strs))



"""
开发总结： 
2020.8.14
欧路词典上，单词分好几种；
有的单词只有一个解释； √
有的单词只有一个词性； √
有的单词有很多词性，每一个词性都有一个解释: ps: 这一种情况下面还要继续细分下去。√
有三个div √

2020.8.15
基本功能已经实现，下一步计划是：
实现输入一系列单词，程序则获取单词相应的解释后将单词和解释一起写入到外部文件，省去了查六级词汇是每次搜索复制粘贴的麻烦
"""