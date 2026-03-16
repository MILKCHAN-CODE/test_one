import numpy as np
import math
import csv
import time
from time import sleep
import random
import requests
from lxml import etree
import re
import csv
import os

file_path = r'C:\Users\14494\Desktop\bugall_books.csv'

def save_all_books_to_csv():
    with open(file_path,'w',encoding = 'utf_8_sig',newline = '') as file_books:
        writer = csv.writer(file_books)
        writer.writerow(['页数','序号','书名'])
        for page in range(1,3):
            catch(page,writer)


def catch(pagenum,writer):
    url = f'https://books.toscrape.com/catalogue/page-{pagenum}.html'
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    }
    response = requests.get(url,headers=headers,timeout = 10)
    html = response.text
    parse = etree.HTML(html)
    all_tr = parse.xpath('//h3/a/@title')
    for index,title in enumerate(all_tr):
        writer.writerow([pagenum, index+1, title.strip()])
        print(f"正在爬取中，第{pagenum}页，第{index}个是：{title.strip()}")
        # writer.writerow([pagenum,index,all_tr.strip()])

if __name__ == "__main__":
    save_all_books_to_csv()
    print('finish')
    


