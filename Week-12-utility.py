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
def ScoreFinder(players, scores, name):
    if name in players:
        a = players.index(name)
        print("OUTPUT", players[a],"got a score of", scores[a])
def Union(lis1,lis2):
    return lis1 + list(set(lis2) - set(lis1))
def Intersection(lis1,lis2):
    inter = [i for i in lis1 if i in lis2]
    return inter
def NotIn(lis1, lis2):
    List = list(set(lis1) - set(lis2))
    return List
