# author: SangHyeon (Alex) Ahn
# email: alexahn917@gmail.com

import sys
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import itertools
import re
import time

def main():
#    if len(sys.argv) < 2:
#        print("USAGE: python parse_opinion.py [opinion_file_name]")
#        exit(1)
    document = split_by_sentence("1.txt")
    search(document)

def split_by_sentence(file_path):
    # read file
    with open(file_path, "r") as f:
        lines = f.read().split('\n')
        data = []
        for line in lines:
            data.append(line)
    data = pd.DataFrame(data)
    return data


def search(document):
    document_blocks = []
    block = []
    for i, row in document.iterrows():
        line = str(row[0])
        line = line.strip()
        if '______________________' in line:
            document_blocks.append(block)
            line = line[len('______________________'):]
            block = []
        block.append(line.strip())
    for word in document_blocks[4]:
        print(word)


def lawyer_n_firm(text):
    pattern = r'(\w+.?,?\s)*(\bfor plaintiff\b)'
    finder = re.compile(pattern)
    found = finder.search(text).group(0).split(', ')
    lawyer = found[0]
    law_firm = found[1]
    return lawyer, law_firm

def cheif_judge(text):
    pattern = r'(\bBefore\b) (\w+)(, )(Chief Judge)'
    finder = re.compile(pattern)
    found = finder.findall(text)
    return (found[0][1])

def circuit_judges(text):
    pattern = r'(\bChief Judge, \b)+(.*)(\bCircuit Judges\b)+'
    finder = re.compile(pattern)
    found = finder.findall(text)
    names = found[0][1]
    names = names.split(',')
    judges = []
    for name in names:
        processed = name.strip()
        processed = re.sub(r'[a-z]', "", processed)
        judges.append(processed.strip())
    return judges

def find_exact_word(word, text):
    finder = re.compile(word)
    found = finder.findall(text)
    print(found)    

if __name__ == '__main__':
    main()




