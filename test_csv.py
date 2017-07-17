# -*- coding: utf-8 -*-

"test if list.csv is a validated csv file."

import csv

def test_csv_file():
    with open('list.csv') as list_file:
        csv_file = csv.reader(list_file)
        row_len = 3
        for row in csv_file:
            for col in csv_file:
                assert len(col) == 3
