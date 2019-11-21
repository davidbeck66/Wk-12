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
