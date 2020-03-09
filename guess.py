import random
r=random.randint(1,100)

i=1
while True:
	num = input('請猜猜1~100中任一數字')
	num = int(num)
	if num ==  r:
		print('終於答對了')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是第', i, '次')
	i=i+1
    