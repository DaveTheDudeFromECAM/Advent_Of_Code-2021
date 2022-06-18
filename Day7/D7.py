# -*- coding: utf-8 -*-
"/////////////////////////////DAY 7//////////////////////////////////"
import numpy as np


"////////////////////////////PART 1//////////////////////////////////"


def consumption_p1(moves):
    
    min_pos = -1
    least_consummed = np.infty    
    for x in range(min(moves), max(moves)+1):        
        fuel_needed = (np.abs(moves - x)).sum()        
        if fuel_needed < least_consummed:            
            least_consummed = fuel_needed            
            min_pos = x            
    print('best option : ', min_pos)
    print('fuel consumption : ', least_consummed)

def part1():
    with open('input.txt', 'r') as i:
        lines = i.readlines()
        moves = [int(entry) for entry in lines[0].strip().split(',')]
    consumption_p1(np.array(moves))
    
    
    
"////////////////////////////PART 2//////////////////////////////////"    
def consumption_p2(moves):
    min_pos = -1
    least_consummed = np.infty
    for x in range(min(moves), max(moves)+1):
        distances = (np.abs(moves - x))
        fuel_needed = sum([(n*(n+1))/2 for n in distances])
        if fuel_needed < least_consummed:
            least_consummed = fuel_needed
            min_pos = x
    print('best option :', min_pos)
    print('fuel consumption : ', least_consummed)

def part2():
    with open('input.txt', 'r') as i:
        lines = i.readlines()
        moves = [int(entry) for entry in lines[0].strip().split(',')]
    consumption_p2(np.array(moves))



"///////////////////////////RESULT///////////////////////////////////"    
part1()
part2()