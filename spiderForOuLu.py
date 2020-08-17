import re
import requests
from lxml import etree
import threading

# 将单词解释写入外部文件
def write_answer_to_file(explanation='', words=''):
    with open('/Users/bowenkei/Desktop/WordSix.txt', 'a+') as file_object:
        if words == '' and explanation == '':
            file_object.write("💗💗💗💗💗💗💗💗💗💗💗💗💗💗\n")
        elif words == '':
            file_object.write(str(explanation) + '\n')
        elif explanation == '':
            file_object.write(str(words) + '\n')

        else:
            file_object.write(str(words) + '-->' + str(explanation) + '\n')


# 爬虫 + 解析
def search_word(s, word):
    pass
    headers = {'User-Agent': 'Mozilla/5.0'}
    #  'https://dict.eudic.net/dicts/en/attr'
    r = requests.get(s, headers=headers)
    x = etree.HTML(r.text)

    all_exp = x.xpath('//*[@id="ExpFCChild"]/div')
    print(len(all_exp))
    if len(all_exp) == 1:

        if len(x.xpath('//*[@id="ExpFCChild"]/i')) == 1:
            write_answer_to_file()
            write_answer_to_file(word)

            write_answer_to_file(
                str(x.xpath('//*[@id="ExpFCChild"]/i')[0].text) + str(x.xpath('//*[@id="ExpFCChild"]/text()')[0]))
            print(x.xpath('//*[@id="ExpFCChild"]/i')[0].text,
                  x.xpath('//*[@id="ExpFCChild"]/text()')[0])  # part_of_speech, answer
        elif len(x.xpath('//*[@id="ExpFCChild"]/ol')) == 1:
            if len(x.xpath('//*[@id="ExpFCChild"]/ol/*[i]')) >= 2:
                write_answer_to_file()
                write_answer_to_file(word)
                len_of_i = len(x.xpath('//*[@id="ExpFCChild"]/ol/*[i]'))
                all_i = x.xpath('//*[@id="ExpFCChild"]/ol/li/i')
                all_li = x.xpath('//*[@id="ExpFCChild"]/ol/li')
                s_of_li = '//*[@id="ExpFCChild"]/ol/li'
                for i in range(len_of_i):
                    write_answer_to_file(
                        str(all_i[i].text) + str(x.xpath(s_of_li + '[' + str(i + 1) + ']' + '/text()')))
                    print(all_i[i].text, end='')
                    print(x.xpath(s_of_li + '[' + str(i + 1) + ']' + '/text()'))
            elif len(x.xpath('//*[@id="ExpFCChild"]/ol/*[i]')) == 1:
                print("have one ol")
                li_collect = x.xpath('//*[@id="ExpFCChild"]/ol/li')
                part_of_speech = x.xpath('//*[@id="ExpFCChild"]/ol/li[1]/i')
                part_answer = x.xpath('//*[@id="ExpFCChild"]/ol/li[1]/text()')
                write_answer_to_file()
                write_answer_to_file(word)
                write_answer_to_file((part_of_speech[0].text + part_answer[0]))
                print(part_of_speech[0].text, part_answer[0])
                for i in range(1, len(li_collect)):
                    write_answer_to_file(li_collect[i].text)
                    print(li_collect[i].text)


    elif len(all_exp) == 2:

        if len(x.xpath('//*[@id="ExpFCChild"]/div[2]/ol/li')) != 0:

            all_exp = x.xpath('//*[@id="ExpFCChild"]/div[2]/ol/li')
            print(len(all_exp))
            for i in range(len(all_exp)):
                all_exp[i] = all_exp[i].text
            write_answer_to_file()
            write_answer_to_file(word)
            write_answer_to_file(all_exp)
            print(all_exp)
        elif len(x.xpath('//*[@id="ExpFCChild"]/ol')) != 0:
            print(len(x.xpath('//*[@id="ExpFCChild"]/ol/li')))
            write_answer_to_file()
            write_answer_to_file(word)
            for i in range(1, len(x.xpath('//*[@id="ExpFCChild"]/ol/li')) + 1):
                strs = '//*[@id="ExpFCChild"]/ol/li' + '[' + str(i) + ']'
                print("---------------")
                if len(x.xpath(strs + '/i')) != 0:  # x.xpath(strs + '/i') != 0:
                    write_answer_to_file(str(x.xpath(strs + '/i/text()')) + str(x.xpath(strs + '/text()')))
                    print(x.xpath(strs + '/i/text()'))
                    print(x.xpath(strs + '/text()'))
                else:
                    write_answer_to_file(x.xpath(strs + '/text()'))
                    print(x.xpath(strs + '/text()'))
        elif len(x.xpath('//*[@id="ExpFCChild"]/i')) != 0:

            write_answer_to_file()
            write_answer_to_file(word)
            write_answer_to_file(
                str(x.xpath('//*[@id="ExpFCChild"]/i/text()')) + str(x.xpath('//*[@id="ExpFCChild"]/text()')))
            print(x.xpath('//*[@id="ExpFCChild"]/i/text()') + x.xpath('//*[@id="ExpFCChild"]/text()'))
        else:
            write_answer_to_file()
            write_answer_to_file(word)
            write_answer_to_file(str(x.xpath('//*[@id="ExpFCChild"]/div[2]/text()')))
            print(x.xpath('//*[@id="ExpFCChild"]/div[2]/text()'))

    # //*[@id="ExpFCChild"]/ol/li[2]

    elif len(all_exp) == 3:
        if len(x.xpath('//*[@id="ExpFCChild"]/div[2]/ol')) == 0:
            write_answer_to_file()
            write_answer_to_file(word)
            write_answer_to_file(x.xpath('//*[@id="ExpFCChild"]/div[2]/text()'))
            print(x.xpath('//*[@id="ExpFCChild"]/div[2]/text()'))
        else:
            # print("has three divs")
            write_answer_to_file()
            all_exp = x.xpath('//*[@id="ExpFCChild"]/div[2]/ol/li')
            write_answer_to_file(word)
            for i in range(1, len(all_exp) + 1):
                strs = '//*[@id="ExpFCChild"]/div[2]/ol/li' + '[' + str(i) + ']' + '/text()'

                write_answer_to_file(x.xpath(strs))
                print(x.xpath(strs))



# Enter all words that you want to look up
# words = 'slave'
# list_of_words = re.split(r'[\s\,\;]+', words)
def start(list_of_words):
    print(list_of_words)
    print(len(list_of_words))
    for i in range(len(list_of_words)):
        s = 'https://dict.eudic.net/dicts/en/' + list_of_words[i]
        search_word(s, list_of_words[i])

if __name__ == '__main__':
    pass
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

2020.8.16 
已经实现前述功能。
下一步：
设计一个GUI界面
2020.8.17 
GUI实现中，目前问题： 
GUI调用过程中，是不会执行爬取任务的，只有等GUI关闭之后才能继续爬取。
似乎解决途径只有一个，那就是使用多线程或者多进程

后来发现tkinter无法使用多线程，最终解决方案是在实现GUI的py文件里面调用此py文件。
GUI文件是OuLuGUI.py
"""
