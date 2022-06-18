# -*- coding: utf-8 -*-
"""
Day 2
"""
#/////////////Part0//////////////////
with open('input.txt', 'r') as data_file:
    data = [str(d) for d in data_file.read().split('\n')]
    print("there are",len(data), "commands in total")    
    
#/////////////Part1//////////////////    
def part1(data):
    for i in range(len(data)):                
        
        if 'up' in data[i]: #UP COMMAND DETECTED
            #print(data[i])
            for x in data[i]:
                #print(x)
                if x.isdigit():
                    step = int(x)
                    operations1['Depth'] -= step
            print('submarine goes UP      by', step)
           
        elif 'down' in data[i]: #DOWN COMMAND DETECTED 
            #print(data[i])
            for x in data[i]:
                #print(x)
                if x.isdigit():
                    step = int(x)
                    operations1['Depth'] += step
            print('submarine goes DOWN    by', step)                       
            
        elif 'forward' in data[i]: #FORWARD COMMAND DETECTED
            #print(data[i])
            for x in data[i]:
                #print(x)
                if x.isdigit():
                    step = int(x)
                    operations1['H_pos'] += step
            print('submarine goes FORWARD by', step) 
    print("\nFinal depth :", operations1['Depth'])
    print("Final horizontal position is :", operations1['H_pos'])
    print("Final part 1 answer is", operations1['Depth'] * operations1['H_pos'] )
    
#/////////////Part2//////////////////     
def part2(data):
    for i in range(len(data)):                
        
        if 'up' in data[i]: #UP COMMAND DETECTED
            for x in data[i]:
                if x.isdigit():
                    step = int(x)
                    operations2['Aim'] -= step
            
        elif 'down' in data[i]: #DOWN COMMAND DETECTED
            for x in data[i]:
                if x.isdigit():
                    step = int(x)
                    operations2['Aim'] += step                      
            
        elif 'forward' in data[i]: #FORWARD COMMAND DETECTED
            for x in data[i]:
                if x.isdigit():
                    step = int(x)
                    operations2['H_pos'] += step
                    operations2['Depth'] += step * operations2['Aim']                          
    print("\nFinal DEPTH :", operations2['Depth'])
    print("Final HORIZONTAL POSITION is :", operations2['H_pos'])
    print("Final AIM is :", operations2['Aim'])
    print("Final part 2 answer is", operations2['Depth'] * operations2['H_pos'] )

#/////////////testing////////////////         
test=["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
step = 0 #"step" can be replaced by "x" in code for improved performance  
operations1 = {"H_pos": 0, "Depth": 0}
operations2 = {"Aim": 0, "H_pos": 0, "Depth": 0}
part1(data)
part2(data)