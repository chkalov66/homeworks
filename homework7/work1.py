# -*- coding: utf-8 -*-

def cancel_action(func):
	def inner(*args, **kwargs):
		result = func(*args, **kwargs)
		print('{} is canceled!'.format(func.__name__))
	return inner

"""def sum(x, y):
	return x + y

def mult(x, y):
    return x * y
s = cancel_action(sum)
s_result = s(9, 12)
print(s_result)
#s1 = sum(9, 12)
#print(s1)

m = cancel_action(mult)
m(2, 5)
"""
@cancel_action
def sum(x, y):
	return x + y

print(sum(3, 9))

@cancel_action
def mult(x, y):
	return x*y

print(mult(5, 7))