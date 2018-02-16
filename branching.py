number = 1;

if number > 0:
	print('positive')
elif number < 0:
	print('negative')
else:
	print('nuetral')
	
	
# ranges
my_list = [0,1,2,3,4,5,6,7,8,9]
for i in range(0, len(my_list)):
	print(my_list[i])
	

# foreach i,plementation
my_list = ['10 Home', '20 Sweet', '6 my home'];
for i in my_list:
	print(i)
	
	
# While loop implemetation
j = 0
while j < 10:
	# string concatenation
	print('j is', j)
	j = j + 1
	
#Infinite loop
while True:
	print(j)
	j = j + 1
	
#Infinite loop 2
while True:
	number = int(input('enter a number'))
	if number == -1:
		break