#!/bin/python
numbers = [2,3,4,5,6,7,8,9]
y = 0
for x in numbers:
	y = x * x
	if y % 8 == 0:
		print(y)
		
