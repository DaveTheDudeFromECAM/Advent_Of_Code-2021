# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:35:53 2022

@author: Dave
"""
def get_data(day=1):
    """
    Returns test and real data in list format.
    Raw data should be maintained as:
        [test data]
        Split From Here
        [actual data]
    """
    file_name = f"data/day{day}.txt"

    with open(file_name) as fp:
        data = fp.read().strip().split("Split From Here")
        data = [d.strip().split("\n") for d in data]
        return data
get_data()

data,data1 = get_data() 
data = list(map(int, data))
data1 = list(map(int, data1))



print('input.txt')
print(min('input.txt'))

#Part 1
data,data1 = get_data(day=7)

data = [int(d) for d in data[0].split(",")]
data1 = [int(d) for d in data1[0].split(",")]

l = len(data1)
f = []

for v in range(l):
    f.append((sum([abs(d-v) for d in data1])))
print(min(f))        



min([sum([abs(d-v) for d in data1]) for v in range(len(data1))])




#Part 2
l = len(data1)
f = []

for v in range(l):
    diff = [abs(d-v) for d in data1]
    diffs = sum([sum(list(range(dif+1))) for dif in diff])
    f.append(diffs)
print(min(f))   




min([sum([sum(list(range(abs(d-v)+1))) for d in data1]) for v in range(len(data1))])
