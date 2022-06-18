# -*- coding: utf-8 -*-
"""
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
Code to find solution to the fist day enigma in Advent of Code
Made by Dave
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
"""

"""        
def part1REDDIT(data):    
    print( len([data[i] for i in range(len(data)-1) if data[i] < data[i + 1]]))
"""
    
#/////////////Part1//////////////////   
def part1(source, counter):
    previous = 0
    for i in range(1,len(data)):
        if data[i] > previous:
            counter += 1
            #print(data[i], "(increased)")
        #else:
            #print(data[i])
        previous = data[i]
    print("\n////////////////////////////////////\n  ", len(data), "measures were analyzed \n////////////////////////////////////\n")
    print(counter, "values were greater than their previous one")
        

#/////////////Part2//////////////////
def part2(data):
    previous_depth = 0
    increases = 0
    for i in range(len(data)-3):
        depth = sum(data[i:i+3])

        if depth > previous_depth:
            increases += 1
        previous_depth = depth
    print(increases)
    
    
#/////////////Part0//////////////////
#Seperate values stored in input file (they're speraated by /n)
with open('input.txt', 'r') as data_file:
    data = [int(d) for d in data_file.read().split('\n')]
    print(data)
    print("there are",len(data), "measures available")    
    
    
#/////////////testing//////////////////
cpt = 0

part1(data, cpt)
#part1REDDIT(data) source from REDDIT
part2(data)