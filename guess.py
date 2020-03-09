import random
start = input('請決定數字範圍開始值')
end = input('請決定數字範圍結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
i=1
while True:
	num = input('請猜猜數字')
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
    