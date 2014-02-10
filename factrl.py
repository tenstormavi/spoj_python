#!/usr/bin/env python

t = int(raw_input())
while t:
	num = int(raw_input())
	count = 0
	while num:
		num = num / 5
		count = count + num
	print count
	t = t - 1
	
