#
# David Beck
# CSCI 102
# Week 12 - Part A

def PrintOutput(string="string"):
    return print("OUTPUT", string)

def LoadFile(file):
    with open (file) as f:
        data = [line.strip() for line in open(file, 'r')]
        return data
def UpdateString(str1,str2,index):
    s = list(str1)
    s[index] = str2
    return ''.join(s)
def FindWordCount(string,lis):
    lis = LoadFile("sample_file.txt")
    return sum(string in i for i in lis)
