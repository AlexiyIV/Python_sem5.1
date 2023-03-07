

#  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
#  с помощью рекурсии.

def rec(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*rec(a,b-1)
print(rec(int(input()),int(input())))