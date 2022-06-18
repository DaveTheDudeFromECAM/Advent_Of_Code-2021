# -*- coding: utf-8 -*-
"/////////////////////////////DAY 4//////////////////////////////////"
import numpy as np
matrix_size = 5



"////////////////////////////PART 1//////////////////////////////////"
# Class used to make bingo grids
class Grid:
    
    # Create empty matrices
    def __init__(self): 
        self.grid = np.zeros((5,5), dtype=int)
        self.draw = np.zeros((5,5))
        
    # Fill the matrix with proper values from 'puzzle input'
    def fill(self, channels): 
        for x in range(matrix_size):
            data = [int(element) for element in channels[x].split(' ') if element != '']
            self.grid[x] = data
            
    # Check if matrix has a number from raffle 
    def contains(self, item):
        if item in self.grid:
            #locate the item from raffle in the matrix
            location = np.where(self.grid == item)
            #put a trace where we spot a number from raffle
            self.draw[location[0], location[1]] = 1
            
    # Check if matrix has any row/column full of ones        
    def wins(self):
        return self.draw.all(axis=0).any() or self.draw.all(axis=1).any()
    
    # Compute earned points
    def points(self, last_draw):
        unmarked_numbers = (self.grid * (self.draw==0)).sum()
        return last_draw * unmarked_numbers
    
# Bingo baord which will be the first to get a whole row/column
def first(batch, grids):
    for item in batch:
        for x in range(len(grids)):
            grids[x].contains(item)
            if grids[x].wins():
                print(f"The winner is grid n°{x+1}")
                print(grids[x].draw)
                return x, item

def part1():
    
    # Retrieve puzzle input file data
    with open('input.txt', 'r') as i:
        channels = [element.strip() for element in i.readlines()]
        
    # Convert 1st input's line to integer list
    batch = [int(element) for element in channels[0].split(',')]
    
    # Create grids and fill them with input file data
    grids = dict()
    for x in range((len(channels)-1)//6):
        start = (2 + x*6)   #where a matrix starts in puzzle input
        end = (2+5+(x+1)*6) #where a matrix ends in puzzle input
        grids[x] = Grid()
        grids[x].fill(channels[start :end])
        
    # Establish the winner    
    best_idx, last_draw = first(batch, grids)
    
    # Get the score    
    print('Your score is :', grids[best_idx].points(last_draw))
    
    
    
"////////////////////////////PART 2//////////////////////////////////"
def last(batch, grids):
    winners = []
    winner_call = 0
    for item in batch:
        for x in range(len(grids)):
            if x not in winners:
                grids[x].contains(item)
                if grids[x].wins():
                    winners.append(x)
                    print(f"Grid {x+1} won!")
                    winner_call = item
    return winners[-1], winner_call

def part2():
    
    # Retrieve puzzle input file data
    with open('input.txt', 'r') as i:
        channels = [element.strip() for element in i.readlines()]
        
    # Convert 1st input's line to integer list
    batch = [int(element) for element in channels[0].split(',')]
    
    # Create grids and fill them with input file data
    grids = dict()
    for x in range((len(channels)-1)//6):
        start = (2 + x*6)   #where a matrix starts in puzzle input
        end = (2+5+(x+1)*6) #where a matrix ends in puzzle input
        grids[x] = Grid()
        grids[x].fill(channels[start :end])
        
     # Establish the loser
    worst_idx, last_draw = last(batch, grids)  
    
    # Get the score     
    print('Your score is :', grids[worst_idx].points(last_draw))



"///////////////////////////RESULT///////////////////////////////////"
part1()
part2()

