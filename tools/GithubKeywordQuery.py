#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Meow J
Licensed separately under The MIT License<https://opensource.org/licenses/MIT>

这是一个非常简陋的查询工具，它可以从GitHub上搜索某一关键字的翻译，供统计或者翻译参考使用
由于GitHub API的代码搜索功能有限制，必须要指定repo或者作者，只好硬解析HTML了
GitHub代码搜索有点缺陷，即使文件名限定了还是能搜索到其它的文件，所以如果有无关的词条那也没办法啦

运行环境需要Python 3.4+，在运行之前需要先安装BeautifulSoup库：
    pip install beautifulsoup4

运行之后会让你输入需要查询的关键字，注意最好只输入1个单词，否则搜索结果量可能会很大
输出文件的文件名为output.lang
对了，如果结果很多的话，429 Error是正常的，毕竟请求太快了，慢慢等它恢复就行
"""

from re import compile
from time import sleep
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen
from html import unescape


def make_url(page_num, _keyword):  # query 'filename:zh_CN.lang keyword'
    return 'https://github.com/search?p=' + str(
        page_num) + '&q=filename%3A.zh_CN.lang+' + _keyword + '&type=Code&utf8=%E2%9C%93'


def open_url_retry(url):
    try:
        return urlopen(url)
    except HTTPError as e:
        if e.code == 429:  # Too many requests
            sleep(10)
            print("[429 Error] Too many requests, retry in 10 secs")
            return open_url_retry(url)
        raise


keyword = input("Keyword: ")

i = 1
html_tags = compile(r'<.*?>')
content = BeautifulSoup(open_url_retry(make_url(i, keyword)), 'html.parser')

output_file = open('output.lang', 'w', encoding='UTF-8')

while True:
    print("Page: " + str(i))
    i += 1

    for line in content.findAll('td', {'class': ['blob-code', 'blob-code-inner']}):
        if keyword.lower() in str(line).lower() and '\\u' not in str(line):
            result = unescape(html_tags.sub('', str(line))).strip()
            if result:
                print(result)
                print(result, file=output_file)

    if not content.find('a', {'class': 'next_page'}):  # The next_page button of the last page is next_page.disabled
        break
    content = BeautifulSoup(open_url_retry(make_url(i, keyword)), 'html.parser')

output_file.close()
