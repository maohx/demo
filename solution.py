#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# author: kimmyzhang
# email: kimmyzhang@outlook.com
# time: 2018-06-25
# brief: Leetcode806. 写字符串需要的行数

def solution(widths, string):
	row = 1

	# 存储当前的行数
	temp_length = 0
	for s in string:
		temp_length += widths[ord(s) - ord('a')] 

		# 如果行数在100之类继续加
		if temp_length <= 100:
			continue

		# 否则的话，行数加1
		else:
			row += 1
			temp_length = widths[ord(s) - ord('a')]
	
	return row, temp_length


if __name__ == "__main__":
	widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] 
	string = 'bbbcccdddaaa'
	a, b = solution(widths, string)
	print a, b