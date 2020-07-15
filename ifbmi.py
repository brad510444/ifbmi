weight = input('請問你的體重多少cm？')
height = input('請問你的身高多少kg？')
weight = float(weight)
height = float(height)
bmi = (weight/(height/100))/(height/100) #使用平方產生錯誤，調查原因

if bmi < 18.5 :
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24 :
	print('正常範圍')
elif bmi >= 24 and bmi < 27 :
	print('過重')
elif bmi >= 27 and bmi <30 :
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35 :
	print('中度肥胖')
else :
	print('重度肥胖') #else需要加冒號：