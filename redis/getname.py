# -*- coding: utf-8 -*-

import os
import csv
# 比较已下载和未下载的文档
if __name__ == '__main__':
    file_dir = "name.csv"
    file_list = os.listdir('papers')
    with open(file_dir, 'w', encoding='utf-8') as f:
        # csv_write = csv.writer(f, lineterminator='\n')
        for item in file_list:
            doi = item.split('%')[-2] + '/' + item.split('%')[-1]
            text = os.path.splitext(doi)[0]
            print(text)
            f.write('\n' + text)
